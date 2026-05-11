# Getting Started

## 1. Create and Activate Conda Environment

An `environment.yml` is included in the repository root. Run once:

```powershell
conda env create -f environment.yml
conda activate diem-validation
```

This installs Python 3.12, all validator dependencies (`polars`, `openpyxl`, `pyyaml`, `xlsxwriter`), and the documentation packages (`mkdocs`, `mkdocs-material`).

> **Already have the environment?** Update it instead:
> ```powershell
> conda env update -f environment.yml --prune
> ```

## 2. Launch Interactive Documentation (Recommended)

From the repository root, with the environment activated:

```powershell
.\documentation
```

Opens the local docs site at `http://127.0.0.1:8000/`.

### Optional: install a global `documentation` command

Run once to register the command inside the conda env:

```powershell
.\install-documentation-command.cmd
```

After that, with `diem-validation` active, you can run `documentation` from any folder.

## 3. Configure and Run Validation

Edit `configuration/validation_config.yaml`, then from the repository root:

```powershell
validate
```

### Key settings to change each run

| Setting | What it controls | Notes |
|---|---|---|
| `tool` | Which validator to run | `kobo` or `geopoll` |
| `language` | Language code for label comparison | `en`, `fr`, `ar`, `es` |
| `iso3` | Country code | Three-letter ISO code (e.g. `YEM`, `AFG`) |
| `reference_mode` | Which baseline to compare against | `latest_template` or `previous_round` |
| `working_dir` | Folder where your input questionnaire file lives | Set to the folder on your machine that contains the questionnaire |
| `questionnaire_file` | Filename of the questionnaire to validate | Filename only — the file must be inside `working_dir` |
| `previous_round_file` | Filename of the previous-round baseline | Only used when `reference_mode: previous_round` |

### Path settings that are specific to each user

These two paths differ for every user and must be set once on first setup:

`templates_dir` — the folder containing all official template Excel files. This is a shared drive or local mirror of the templates repository. Set it to wherever those files are on your machine:

```yaml
templates_dir: "C:/Users/yourname/path/to/Questionnaire Templates"
```

`output_dir` — where reports are written. Each tool writes to its own subfolder:

```yaml
output_dir: "C:/Temp/questionnaire_validation"
# reports land in:
#   output_dir/geopoll_output/   (GeoPoll)
#   output_dir/kobo_output/      (KoBo)
```

You can set this to any folder that exists on your machine.

### Where to put the input file

Place the questionnaire file you want to validate inside the folder set as `working_dir`, then set `questionnaire_file` to its filename:

```yaml
working_dir: "C:/Temp"
questionnaire_file: "my_questionnaire_en_AFG_20260101.xlsx"
```

The validator reads the file from `working_dir/questionnaire_file`. If the file is not found at that path, the run will stop with an error.

## Environment Contents

| Package | Purpose |
|---|---|
| `polars` | DataFrame engine used throughout the validation pipeline |
| `openpyxl` | Read/write Excel questionnaire and report files |
| `pyyaml` | Parse `validation_config.yaml` and `critical_sets.yaml` |
| `xlsxwriter` | Write formatted Excel report workbooks |
| `mkdocs` + `mkdocs-material` | Local documentation site |
