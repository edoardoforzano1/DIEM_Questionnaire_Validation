from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
import shutil
from typing import Iterable


_REPORT_RE = re.compile(
    r"^report_(kobo|geopoll)_([a-z]{2})_([A-Z]{3})(?:_(R\d{1,3}))?_(\d{8})\.xlsx$"
)
_VALIDATED_RE = re.compile(
    r"^validated_questionnaire_(kobo|geopoll)_([a-z]{2})_([A-Z]{3})(?:_(R\d{1,3}))?_(\d{8})\.xlsx$"
)
_CONFIG_RE = re.compile(
    r"^config_(kobo|geopoll)_([A-Za-z]{2})_([A-Za-z0-9]{3})_(\d{8}_\d{6})\.ya?ml$"
)


@dataclass
class _ParsedFile:
    path: Path
    category: str
    group_key: tuple[str, str, str, str, str]
    stamp: datetime


def _as_bool(value, default: bool) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    txt = str(value).strip().lower()
    if txt in {"1", "true", "yes", "y", "on"}:
        return True
    if txt in {"0", "false", "no", "n", "off"}:
        return False
    return default


def _as_int(value, default: int, minimum: int = 0) -> int:
    try:
        out = int(value)
    except Exception:
        out = default
    return max(minimum, out)


def _safe_resolve(path: Path) -> Path:
    try:
        return path.resolve()
    except Exception:
        return path.absolute()


def _iter_files(root: Path) -> Iterable[Path]:
    if not root.exists():
        return []
    return (p for p in root.rglob("*") if p.is_file())


def _classify_file(path: Path) -> _ParsedFile | None:
    name = path.name
    m = _REPORT_RE.match(name)
    if m:
        tool, lang, iso3, rnd, ymd = m.groups()
        stamp = datetime.strptime(ymd, "%Y%m%d")
        return _ParsedFile(
            path=path,
            category="report",
            group_key=("report", tool, lang.lower(), iso3.upper(), (rnd or "").upper()),
            stamp=stamp,
        )

    m = _VALIDATED_RE.match(name)
    if m:
        tool, lang, iso3, rnd, ymd = m.groups()
        stamp = datetime.strptime(ymd, "%Y%m%d")
        return _ParsedFile(
            path=path,
            category="validated",
            group_key=("validated", tool, lang.lower(), iso3.upper(), (rnd or "").upper()),
            stamp=stamp,
        )

    m = _CONFIG_RE.match(name)
    if m:
        tool, lang, iso3, ts = m.groups()
        stamp = datetime.strptime(ts, "%Y%m%d_%H%M%S")
        return _ParsedFile(
            path=path,
            category="config_snapshot",
            group_key=("config_snapshot", tool, lang.upper(), iso3.upper(), ""),
            stamp=stamp,
        )
    return None


def _build_archive_target(archive_root: Path, output_root: Path, file_path: Path, stamp: datetime) -> Path:
    month_bucket = stamp.strftime("%Y-%m")
    rel = file_path.relative_to(output_root)
    target = archive_root / month_bucket / rel
    if not target.exists():
        return target

    stem = target.stem
    suffix = target.suffix
    idx = 1
    while True:
        alt = target.with_name(f"{stem}__{idx}{suffix}")
        if not alt.exists():
            return alt
        idx += 1


def _get_file_stamp(path: Path) -> datetime:
    try:
        return datetime.fromtimestamp(path.stat().st_mtime)
    except Exception:
        return datetime.min


def _limit_for_category(category: str, cfg: dict) -> int:
    if category == "report":
        return _as_int(cfg.get("keep_reports_per_group", 3), 3, minimum=1)
    if category == "validated":
        return _as_int(cfg.get("keep_validated_per_group", 3), 3, minimum=1)
    if category == "config_snapshot":
        return _as_int(cfg.get("keep_config_snapshots_per_group", 30), 30, minimum=1)
    return 0


def run_output_housekeeping(config: dict) -> dict:
    hk_cfg = dict(config.get("housekeeping") or {})
    enabled = _as_bool(hk_cfg.get("enabled"), False)

    result = {
        "enabled": enabled,
        "dry_run": _as_bool(hk_cfg.get("dry_run"), False),
        "base_output_dir": "",
        "scanned_files": 0,
        "kept_files": 0,
        "candidate_files": 0,
        "archived_files": 0,
        "deleted_files": 0,
        "errors": [],
        "actions": [],
        "archive_deleted_files": 0,
    }
    if not enabled:
        return result

    now = datetime.now()
    protect_today = _as_bool(hk_cfg.get("protect_today_files"), True)
    keep_days = _as_int(hk_cfg.get("keep_all_for_last_days", 14), 14, minimum=0)
    archive_before_delete = _as_bool(hk_cfg.get("archive_before_delete"), True)
    archive_purge_days = _as_int(hk_cfg.get("delete_archives_older_than_days", 180), 180, minimum=0)

    output_base = Path(config.get("output_dir") or config.get("working_dir") or "C:/Temp/questionnaire_validation")
    output_base = _safe_resolve(output_base)
    result["base_output_dir"] = str(output_base)

    archive_root = Path(hk_cfg.get("archive_dir") or (output_base / "archive"))
    archive_root = _safe_resolve(archive_root)

    tool_targets = [
        output_base / "kobo_output",
        output_base / "geopoll_output",
        output_base / "configuration",
    ]

    protected_abs: set[Path] = set()
    prev_round_file = str(config.get("previous_round_file") or "").strip()
    working_dir = Path(config.get("working_dir") or output_base)
    if prev_round_file:
        p = Path(prev_round_file)
        if not p.is_absolute():
            p = working_dir / p
        protected_abs.add(_safe_resolve(p))

    groups: dict[tuple[str, str, str, str, str], list[_ParsedFile]] = {}
    for root in tool_targets:
        if not root.exists():
            continue
        for file_path in _iter_files(root):
            result["scanned_files"] += 1
            parsed = _classify_file(file_path)
            if parsed is None:
                result["kept_files"] += 1
                continue

            f_abs = _safe_resolve(parsed.path)
            if f_abs in protected_abs:
                result["kept_files"] += 1
                continue
            if protect_today and parsed.stamp.date() == now.date():
                result["kept_files"] += 1
                continue
            if keep_days > 0 and (now - parsed.stamp).days < keep_days:
                result["kept_files"] += 1
                continue
            if parsed.path.with_name(f"{parsed.path.name}.keep").exists():
                result["kept_files"] += 1
                continue

            groups.setdefault(parsed.group_key, []).append(parsed)

    candidates: list[_ParsedFile] = []
    for group_key, items in groups.items():
        limit = _limit_for_category(group_key[0], hk_cfg)
        items_sorted = sorted(items, key=lambda x: x.stamp, reverse=True)
        if limit <= 0:
            candidates.extend(items_sorted)
            continue
        for idx, item in enumerate(items_sorted):
            if idx < limit:
                result["kept_files"] += 1
            else:
                candidates.append(item)

    result["candidate_files"] = len(candidates)

    for item in sorted(candidates, key=lambda x: x.stamp):
        src = item.path
        if result["dry_run"]:
            action = "archive" if archive_before_delete else "delete"
            result["actions"].append(f"{action}: {src}")
            continue

        try:
            if archive_before_delete:
                dst = _build_archive_target(archive_root, output_base, src, item.stamp)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                src.unlink(missing_ok=True)
                result["archived_files"] += 1
                result["actions"].append(f"archive: {src} -> {dst}")
            else:
                src.unlink(missing_ok=True)
                result["deleted_files"] += 1
                result["actions"].append(f"delete: {src}")
        except Exception as exc:
            result["errors"].append(f"{src}: {exc}")

    if archive_before_delete and archive_purge_days > 0 and archive_root.exists():
        for ap in _iter_files(archive_root):
            if ap.with_name(f"{ap.name}.keep").exists():
                continue
            stamp = _get_file_stamp(ap)
            if (now - stamp).days < archive_purge_days:
                continue
            if result["dry_run"]:
                result["actions"].append(f"delete-archive: {ap}")
                continue
            try:
                ap.unlink(missing_ok=True)
                result["archive_deleted_files"] += 1
            except Exception as exc:
                result["errors"].append(f"{ap}: {exc}")

    return result
