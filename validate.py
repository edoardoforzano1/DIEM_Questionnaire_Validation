"""
DIEM Questionnaire Validation — entry point.

Usage:
    python validate.py

Reads tool: from configuration/validation_config.yaml and dispatches
to the matching validator in scripts/.
"""
import sys
import subprocess
import pathlib
import yaml

ROOT    = pathlib.Path(__file__).parent
CFG     = ROOT / "configuration" / "validation_config.yaml"
SCRIPTS = ROOT / "scripts"

VALIDATORS = {
    "geopoll": SCRIPTS / "geopoll_validator.py",
    "kobo":    SCRIPTS / "kobo_validator.py",
}


def main() -> None:
    if not CFG.exists():
        print(f"ERROR: configuration file not found: {CFG}")
        sys.exit(1)

    raw = yaml.safe_load(CFG.read_text(encoding="utf-8")) or {}

    # Resolve config profile if one is set
    profile_name = str(raw.get("config_profile") or "").strip()
    if profile_name:
        profiles_dir = pathlib.Path(
            raw.get("config_profiles_dir")
            or (pathlib.Path(raw.get("output_dir") or raw.get("working_dir") or "C:/Temp") / "config_profiles")
        )
        candidate = pathlib.Path(profile_name)
        if not candidate.is_absolute():
            candidate = profiles_dir / candidate
        for suffix in ("", ".yaml", ".yml"):
            p = candidate if suffix == "" else candidate.with_suffix(suffix)
            if p.exists():
                override = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
                raw.update(override)
                break

    tool = str(raw.get("tool") or "").strip().lower()

    if tool not in VALIDATORS:
        known = ", ".join(sorted(VALIDATORS.keys()))
        print(f"ERROR: 'tool' in validation_config.yaml must be one of: {known}")
        print(f"       Got: {tool!r}")
        sys.exit(1)

    script = VALIDATORS[tool]
    if not script.exists():
        print(f"ERROR: validator script not found: {script}")
        sys.exit(1)

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(ROOT),
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
