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

Edit `configuration/validation_config.yaml` to set the tool, language, reference mode, and file paths, then from the repository root:

```powershell
validate
```

Output reports land in `batch_output/<run_name>/`.

## Environment Contents

| Package | Purpose |
|---|---|
| `polars` | DataFrame engine used throughout the validation pipeline |
| `openpyxl` | Read/write Excel questionnaire and report files |
| `pyyaml` | Parse `validation_config.yaml` and `critical_sets.yaml` |
| `xlsxwriter` | Write formatted Excel report workbooks |
| `mkdocs` + `mkdocs-material` | Local documentation site |
