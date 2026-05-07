# Getting Started

## Prerequisites

- Python 3.10+
- Access to questionnaire and reference files
- Access to template repository path configured in `configuration/validation_config.yaml`

## Runtime Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configure a Run

Edit `configuration/validation_config.yaml` and set at least:

```yaml
tool: "kobo"                # kobo | geopoll
questionnaire_file: "..."
language: "en"              # en | fr | ar | es
iso3: "XXX"
reference_mode: "latest_template"   # or previous_round
```

If `reference_mode` is `previous_round`, set `previous_round_file`.

## Run Validation

```powershell
python validate.py
```

The entrypoint reads `tool:` and dispatches to the corresponding validator script.

## Local Documentation Preview

```powershell
pip install -r requirements-docs.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`.
