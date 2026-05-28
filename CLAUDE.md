# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Validates DIEM household questionnaire files (KoBo XLSForm or GeoPoll Excel format) against a reference — either the latest official template or the previous round — and produces a structured Excel report classifying every difference by severity. Two standalone tools handle the administrative boundary lists separately.

## Conda environment

All commands must run inside the `diem-validation` conda environment. When running scripts manually:

```powershell
conda activate diem-validation
```

Core dependencies: `polars`, `openpyxl`, `pyyaml`, `xlsxwriter`, `mkdocs-material`.

## Commands

```powershell
# Run validation (reads configuration/validation_config.yaml)
validate

# Check admin boundary lists in a validated questionnaire against AGOL
tool_admin_check

# Create a new questionnaire file with updated admin boundary lists
tool_admin_sync

# Launch local documentation site at http://127.0.0.1:8000/
.\documentation

# Regenerate auto-built function reference pages after editing validator scripts
python scripts/regenerate_function_docs.py

# Smoke test — run the full pipeline and verify output structure
smoke_test
```

Each `.bat` launcher at the repo root simply calls `python "%~dp0<script>.py" %*`.

Optional CLI flags for admin tools:

```powershell
tool_admin_check --source-file "filename.xlsx" --config "path/to/config.yaml"
tool_admin_sync  --source-file "filename.xlsx" --sync-mode full_from_agol
```

## Architecture

### Entry point and dispatch

`validate.py` reads `configuration/validation_config.yaml`, resolves an optional `config_profile` override, then **launches the selected validator as a subprocess** (`subprocess.run([sys.executable, str(script)])`). It does not import the validators — they are not importable modules.

Before dispatch, `validate.py` calls `scripts/output_housekeeping.py` to archive or delete old output files according to retention rules in the `housekeeping:` config block.

### Validator scripts

`scripts/kobo_validator.py` and `scripts/geopoll_validator.py` are **converted Jupyter notebooks**. They execute top-to-bottom when run as scripts. Config is read at module level from `configuration/validation_config.yaml`. They share a common structure:

1. Load config → resolve questionnaire path → resolve reference file
2. Read questionnaire and reference into Polars DataFrames
3. Run comparison functions (one per check type) that each return a list of issue dicts
4. Collect all issues into a single Polars DataFrame
5. Write the Excel report and validated questionnaire output

The `# SECTION: ## Step N` comments in the validators are parsed by `regenerate_function_docs.py` to build the function reference documentation — do not remove or reformat them.

### KoBo placeholder pipeline

KoBo produces a validated output questionnaire in addition to the report. The pipeline for this file runs five steps inside `produce_validated_questionnaire()`:

1. Copy source workbook
2. Inject crop choices from the Crop list sheet
3. Inject admin choices (fetched live from AGOL)
4. Restore `#placeholder#` tokens from the template (runs even when no replacement pairs are available — passes `replacement_pairs=None` to restore all placeholders without replacing)
5. Apply replacements from the Additional information sheet (only runs when pairs are available)

`_can_run_restore` and `_can_run_replace` are the two flags controlling steps 4/5. They are separate — restore always runs unless `skip_restore_and_replacement: true` is set.

### Admin tools

`scripts/admin_tools_common.py` is the shared utilities module. It provides:
- `merge_runtime_config(repo_root, explicit_cfg)` — merges `validation_config.yaml` + `admin_tools_config.yaml` into a single flat dict; this is the config contract for all admin tools
- `fetch_agol_admin_rows(iso3, include_admin3)` — queries two AGOL FeatureServer REST endpoints live; requires internet; 40-second timeout
- `resolve_source_workbook(cfg)` — source file selection in `standard` mode (auto-picks latest matching `validated_questionnaire_{tool}_*.xlsx`) or `custom` mode (searches `custom_dir`, `validated_dir`, `working_dir`, repo root by filename)
- `detect_label_column(headers, language)` — finds the correct `label::Language (xx)` column index

`scripts/tool_admin_check.py` and `scripts/tool_admin_sync.py` each follow the same pattern: `main()` → `merge_runtime_config()` → `run(cfg: dict) → int`.

### Config system

**`configuration/validation_config.yaml`** — main config for the validators. The `config_profile` key can point to a YAML file (filename only, resolved under `output_dir/config_profiles/`, or absolute path) whose keys override the base config. This lets you switch country/language/round without editing the base file.

**`configuration/admin_tools_config.yaml`** — config for the two admin tools. Falls back to `validation_config.yaml` for `tool`, `language`, `iso3` when those keys are absent. The `source:` and `sync:` blocks are admin-tool-specific.

**`configuration/critical_sets.yaml`** — GeoPoll only. Defines `exact_sets`, `min_count_sets`, and `crop_harvest` validation rules. Edit this file when the questionnaire structure changes; no code changes needed.

### Output naming

Reports: `report_{tool}_{lang}_{ISO3}_{timestamp}.xlsx`
Validated questionnaires: `validated_questionnaire_{tool}_{lang}_{ISO3}_{timestamp}.xlsx`
Config snapshots: `config_{tool}_{lang}_{ISO3}_{timestamp}.yaml`
Admin tool outputs: `admin_check_report_{source}_{timestamp}.xlsx`, `{source}_adminsync_{mode}_{timestamp}.xlsx`

All land in subfolders of `output_dir`: `kobo_output/` or `geopoll_output/` for validators, `admin_tools_output/` for admin tools.

## Working approach

Before making any code change, describe the plan and wait for explicit confirmation. This applies to all edits — new functions, bug fixes, refactors, config changes. The only exception is when the user has explicitly said to go ahead.

## Code conventions

### Polars

Use native Polars patterns throughout. Prefer `pl.Expr`-based operations over row iteration or `.to_pandas()` conversions. Key patterns used in this codebase:

- Column operations are written as expressions: `pl.col("name").str.strip_chars().str.to_lowercase()`
- Aggregations use `group_by().agg()`, not loops
- Functions that operate on a column accept a `col_name: str` parameter and return `pl.Expr`, so callers can compose them — see `normalize_text_expr()`, `_normalized_list_expr()`, `_canonical_option_key_expr()` for the established pattern
- Use `df.filter()`, `df.with_columns()`, `df.join()` rather than conditional Python logic on rows
- Avoid `.to_dicts()` loops except for final output serialization

### Naming

Follow the verb-noun pattern established across both validators:

- `read_*` — load data from a file into a DataFrame or dict
- `compare_*` — take current and reference DataFrames, return a list of issue dicts
- `build_*` — construct a derived DataFrame or structure from inputs
- `normalize_*` / `_normalize_*` — return a cleaned/canonicalized value or `pl.Expr`
- `fetch_*` — retrieve data from an external source (network, AGOL)
- `detect_*` / `resolve_*` — find or determine something from available context
- `_` prefix for private helpers not meant to be called from outside their module

New functions doing the same class of work as an existing function should mirror its name. Check the existing function list before naming.

### Config over hardcoding

No hardcoded paths, column names, list names, country-specific values, or thresholds inside function bodies. These belong in:
- `configuration/validation_config.yaml` — runtime parameters and per-run settings
- `configuration/critical_sets.yaml` — GeoPoll structural rules
- `configuration/admin_tools_config.yaml` — admin tool parameters
- A new config file if neither of the above fits

Functions receive values from config as parameters. If a function needs a value that currently comes from a global `cfg` dict, pass it explicitly rather than reading `cfg` directly inside the function.

## Before adding or changing anything

The validators are large, tightly coupled scripts where a change in one place can silently break something downstream. Before implementing:

1. **Trace the data flow**: find where the value or structure you are changing is produced, then follow every place it is consumed. In `kobo_validator.py` and `geopoll_validator.py` this often spans hundreds of lines because they run top-to-bottom as scripts — a variable set in one section is read in a later section with no import boundary to signal the dependency.

2. **Check both validators**: KoBo and GeoPoll share concepts (module filtering, placeholder handling, output naming) but implement them separately. A change that makes sense for one may need a parallel change in the other, or may conflict with the other's existing logic.

3. **Check the output contract**: functions that return issue dicts must produce the exact columns (`check`, `status`, `details`, `severity`) that the report writer expects. Functions that produce DataFrames for comparison must preserve the column names that downstream `compare_*` functions join on.

4. **Check config-driven behavior**: if you change a function that reads from `cfg`, verify that all config keys it reads are documented in `validation_config.yaml` and that existing config files still work — no silent key renames.

5. **The placeholder pipeline is order-dependent**: steps 1–5 in `produce_validated_questionnaire()` must run in sequence. Adding a step or changing what a step writes to the workbook can corrupt the input to subsequent steps.

## Do not touch

- `docs/function-reference/kobo-validator.md` and `docs/function-reference/geopoll-validator.md` — auto-generated by `regenerate_function_docs.py`; regenerate after editing the validator scripts
- `site/` — MkDocs build output, not source
- `batch_output/` — runtime output, not tracked in git

## Known gotchas

**Hidden Excel sheets**: `openpyxl` reads sheets with `sheet_state='hidden'` or `'veryHidden'` silently — `wb.sheetnames` includes them and `wb["Sheet Name"]` succeeds even though the tab is invisible in Excel. Always check `.sheet_state` if you need to distinguish user-visible from hidden sheets.

**Validator scripts are not importable**: `kobo_validator.py` and `geopoll_validator.py` execute config loading, AGOL fetches, and validation at module level. Never `import` them from another script. Call them via subprocess as `validate.py` does.

**Windows stdout encoding**: running Python scripts via `conda run` on Windows can cause `UnicodeEncodeError` (cp1252) when the script prints non-ASCII characters. Write output to a file and read it back if you need to capture output from a subprocess.

**`my_filter_sample` column**: during admin sync, this column controls sample-based filtering in the questionnaire. `preserve_my_filter_sample: true` (default) carries the original values into the rewritten rows. Do not remove this behavior.

**AGOL fetch is always live**: `fetch_agol_admin_rows()` has no caching. Every run of either admin tool hits the network. Do not add caching without considering that country admin hierarchies change between rounds.
