# DIEM Questionnaire Validation v2

Automated validation of DIEM household questionnaires for GeoPoll and KoBo.

## Full Documentation

- GitHub Pages project site (after publish): `https://<your-username>.github.io/DIEM_Questionnaire_Validation/`
- Documentation source in this repo: `docs/`

## Quick Setup

1. Create and activate a virtual environment.
2. Install runtime dependencies.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run Validation

1. Edit `configuration/validation_config.yaml` for your run.
2. Run from the repository root:

```powershell
python validate.py
```

`validate.py` reads `tool:` from config and dispatches to the matching validator.

## Essential Workflow

1. Select tool: `kobo` or `geopoll`.
2. Select reference mode: `latest_template` or `previous_round`.
3. Run validation.
4. Review output reports in `output_dir/<tool>_output`.

## Project Structure

```text
DIEM_Questionnaire_Validation/
|-- validate.py
|-- configuration/
|   |-- validation_config.yaml
|   `-- critical_sets.yaml
|-- scripts/
|   |-- geopoll_validator.py
|   `-- kobo_validator.py
|-- docs/
|   `-- ... full detailed documentation
`-- mkdocs.yml
```

## Local Docs Preview (Optional)

```powershell
pip install -r requirements-docs.txt
mkdocs serve
```

Open `http://127.0.0.1:8000/`.
