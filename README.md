# DIEM Questionnaire Validation v2

Automated validation of DIEM household questionnaires for GeoPoll and KoBo.

## Recommended Reading Path

1. Read this `README.md` for setup and run commands.
2. Launch the interactive documentation web view.
3. Read detailed logic pages from the left menu under `Validation Workflow`.

## One-Time Environment Setup (Conda)

An `environment.yml` is included. Create and activate the environment with:

```powershell
conda env create -f environment.yml
conda activate diem-validation
```

This installs everything needed to run the validator and view the documentation locally.

> **Note:** if you already have an older `diem-validation` environment, update it with:
> ```powershell
> conda env update -f environment.yml --prune
> ```

## Launch Interactive Documentation (Recommended)

From the repository root:

```powershell
.\documentation
```

This starts the local docs site and opens `http://127.0.0.1:8000/`.

### Optional: enable plain `documentation` command in this conda env

Run once after activating the environment:

```powershell
.\install-documentation-command.cmd
```

Then you can launch docs from any folder with:

```powershell
documentation
```

## Run Validation

1. Edit `configuration/validation_config.yaml`.
2. Run:

```powershell
python validate.py
```

or

```powershell
.\validate.bat
```

## Essential Workflow

1. Select tool: `kobo` or `geopoll`.
2. Select reference mode: `latest_template` or `previous_round`.
3. Run validation.
4. Review output reports in `batch_output/<run_name>/`.

## Documentation Sources

- Local docs source: `docs/`
- MkDocs config: `mkdocs.yml`
