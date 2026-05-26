from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


LANG_LABEL_COL = {
    "en": "label::English (en)",
    "fr": "label::French (fr)",
    "ar": "label::Arabic (ar)",
    "es": "label::Spanish (es)",
}


def as_bool(value: Any, default: bool = False) -> bool:
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


def read_validation_config(repo_root: Path) -> dict:
    cfg_path = repo_root / "configuration" / "validation_config.yaml"
    if not cfg_path.exists():
        return {}
    return yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}


def read_admin_tools_config(repo_root: Path, cfg_path: Path | None = None) -> dict:
    cfg_file = cfg_path or (repo_root / "configuration" / "admin_tools_config.yaml")
    if not cfg_file.exists():
        return {}
    out = yaml.safe_load(cfg_file.read_text(encoding="utf-8")) or {}
    if not isinstance(out, dict):
        return {}
    return out


def merge_runtime_config(repo_root: Path, explicit_cfg: Path | None = None) -> dict:
    base = read_validation_config(repo_root)
    tool_cfg = read_admin_tools_config(repo_root, cfg_path=explicit_cfg)

    output_base = Path(str(base.get("output_dir") or base.get("working_dir") or "C:/Temp/questionnaire_validation"))
    working_dir = Path(str(base.get("working_dir") or "C:/Temp"))

    source_cfg = dict(tool_cfg.get("source") or {})
    sync_cfg = dict(tool_cfg.get("sync") or {})

    tool = str(tool_cfg.get("tool") or base.get("tool") or "kobo").strip().lower()
    language = str(tool_cfg.get("language") or base.get("language") or "en").strip().lower()
    iso3 = str(tool_cfg.get("iso3") or base.get("iso3") or "").strip().upper()
    source_mode = str(source_cfg.get("mode") or "standard").strip().lower()
    source_file = str(source_cfg.get("file_name") or "").strip()
    source_custom_dir = str(source_cfg.get("custom_dir") or "").strip()
    include_admin3 = as_bool(
        tool_cfg.get("include_admin3"),
        as_bool((base.get("kobo_options") or {}).get("include_admin3"), False),
    )
    sync_mode = str(sync_cfg.get("mode") or "subset_from_agol").strip().lower()
    output_dir = Path(str(tool_cfg.get("output_dir") or (output_base / "admin_tools_output")))
    validated_dir = Path(str(tool_cfg.get("validated_dir") or (output_base / f"{tool}_output")))

    return {
        "repo_root": str(repo_root),
        "tool": tool,
        "language": language,
        "iso3": iso3,
        "source_mode": source_mode,
        "source_file": source_file,
        "source_custom_dir": source_custom_dir,
        "include_admin3": include_admin3,
        "sync_mode": sync_mode,
        "output_dir": str(output_dir),
        "validated_dir": str(validated_dir),
        "working_dir": str(working_dir),
        "output_base_dir": str(output_base),
        "config_path": str(explicit_cfg) if explicit_cfg else str(repo_root / "configuration" / "admin_tools_config.yaml"),
        "preserve_my_filter_sample": as_bool(sync_cfg.get("preserve_my_filter_sample"), True),
        "dry_run": as_bool(tool_cfg.get("dry_run"), False),
    }


def print_runtime_banner(title: str, cfg: dict) -> None:
    print(f"[{title}]")
    print(f"  tool        : {cfg.get('tool')}")
    print(f"  iso3/lang   : {cfg.get('iso3')}/{cfg.get('language')}")
    print(f"  source_mode : {cfg.get('source_mode')}")
    print(f"  validated   : {cfg.get('validated_dir')}")
    print(f"  output      : {cfg.get('output_dir')}")
    print(f"  config      : {cfg.get('config_path')}")


def resolve_source_workbook(cfg: dict) -> Path:
    mode = str(cfg.get("source_mode") or "standard").strip().lower()
    source_file = str(cfg.get("source_file") or "").strip()
    source_custom_dir = str(cfg.get("source_custom_dir") or "").strip()
    validated_dir = Path(str(cfg.get("validated_dir") or "."))
    working_dir = Path(str(cfg.get("working_dir") or "."))
    output_base_dir = Path(str(cfg.get("output_base_dir") or "."))
    tool = str(cfg.get("tool") or "kobo").strip().lower()
    lang = str(cfg.get("language") or "").strip().lower()
    iso3 = str(cfg.get("iso3") or "").strip().upper()

    if mode in {"custom", "specific_file"}:
        if not source_file:
            raise FileNotFoundError(
                "source.mode is 'custom' but source.file_name is empty in admin_tools_config.yaml"
            )
        p = Path(source_file)
        if p.is_absolute() and p.exists():
            return p

        candidate_roots = []
        if source_custom_dir:
            candidate_roots.append(Path(source_custom_dir))
        candidate_roots.extend([validated_dir, working_dir, output_base_dir, Path(str(cfg.get("repo_root") or "."))])
        seen = set()
        for root in candidate_roots:
            key = str(root).lower()
            if key in seen:
                continue
            seen.add(key)
            c = root / source_file
            if c.exists():
                return c
        raise FileNotFoundError(
            f"Configured custom source file not found: {source_file}\n"
            f"Searched in: {', '.join(str(r) for r in candidate_roots)}"
        )

    if not validated_dir.exists():
        raise FileNotFoundError(f"Validated output folder not found: {validated_dir}")

    candidates = sorted(validated_dir.glob(f"validated_questionnaire_{tool}_*.xlsx"))
    if lang:
        candidates = [p for p in candidates if f"_{lang}_" in p.name.lower()]
    if iso3:
        candidates = [p for p in candidates if f"_{iso3}_" in p.name.upper()]
    if not candidates:
        raise FileNotFoundError(
            f"No validated questionnaire found in {validated_dir} "
            f"for tool={tool}, language={lang or '*'}, iso3={iso3 or '*'}."
        )
    return max(candidates, key=lambda p: p.stat().st_mtime)


def detect_label_column(headers: list[str], language: str) -> int | None:
    lang = str(language or "en").strip().lower()
    preferred = LANG_LABEL_COL.get(lang)
    if preferred and preferred in headers:
        return headers.index(preferred)

    for h in headers:
        if h.lower().startswith("label::") and f"({lang})" in h.lower():
            return headers.index(h)

    for h in headers:
        if h.lower().startswith("label::"):
            return headers.index(h)
    return None


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def safe_json(text: Any) -> str:
    try:
        return json.dumps(text, ensure_ascii=False)
    except Exception:
        return str(text)


def fetch_agol_admin_rows(iso3: str, include_admin3: bool = False) -> dict[str, list[tuple[str, str, str]]]:
    import json as _json
    import urllib.request as _urlreq

    _BASE_ADMIN12 = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
                     "/Administrative_Boundaries_Reference_(view_layer)/FeatureServer")
    _BASE_ADMIN3 = ("https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services"
                    "/Reference_Admin_3_(view_layer)/FeatureServer")

    def _get_admin12(layer: int, fields: str):
        url = (f"{_BASE_ADMIN12}/{layer}/query"
               f"?where=adm0_ISO3+%3D+%27{iso3}%27"
               f"&outFields={fields}&returnGeometry=false&outSR=4326&f=json")
        with _urlreq.urlopen(url, timeout=40) as r:
            payload = _json.loads(r.read().decode())
        return payload.get("features", [])

    def _get_admin3(fields: str):
        url = (f"{_BASE_ADMIN3}/0/query"
               f"?where=adm0_ISO3+%3D+%27{iso3}%27"
               f"&outFields={fields}&returnGeometry=false&outSR=4326&f=json")
        with _urlreq.urlopen(url, timeout=40) as r:
            payload = _json.loads(r.read().decode())
        return payload.get("features", [])

    adm1 = sorted(
        [
            (
                str(f["attributes"].get("adm1_pcode") or "").strip(),
                str(f["attributes"].get("adm1_name") or "").strip(),
                "",
            )
            for f in _get_admin12(1, "adm1_name,adm1_pcode")
        ],
        key=lambda x: x[0],
    )
    adm2 = sorted(
        [
            (
                str(f["attributes"].get("adm2_pcode") or "").strip(),
                str(f["attributes"].get("adm2_name") or "").strip(),
                str(f["attributes"].get("adm1_pcode") or "").strip(),
            )
            for f in _get_admin12(0, "adm2_name,adm2_pcode,adm1_pcode")
        ],
        key=lambda x: x[0],
    )

    out: dict[str, list[tuple[str, str, str]]] = {
        "admin1": [x for x in adm1 if x[0]],
        "admin2": [x for x in adm2 if x[0]],
    }

    if include_admin3:
        adm3 = sorted(
            [
                (
                    str(f["attributes"].get("adm3_pcode") or "").strip(),
                    str(f["attributes"].get("adm3_name") or "").strip(),
                    str(f["attributes"].get("adm2_pcode") or "").strip(),
                )
                for f in _get_admin3("adm3_name,adm3_pcode,adm2_pcode")
            ],
            key=lambda x: x[0],
        )
        out["admin3"] = [x for x in adm3 if x[0]]
    return out
