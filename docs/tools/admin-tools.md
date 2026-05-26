# Admin Tools

Two standalone utilities for checking and updating the administrative boundary lists (admin1, admin2, admin3) in a validated questionnaire. Both tools read their configuration from `configuration/admin_tools_config.yaml` and fetch the reference data live from ArcGIS Online (AGOL).

---

## tool_admin_check

Compares the admin codes currently in a questionnaire against the official AGOL reference and produces a detailed mismatch report. Use this to find out whether your questionnaire's admin lists are up to date before a round launch.

### What it checks

The tool reads the `choices` sheet of the questionnaire, extracts all rows belonging to `admin1`, `admin2`, and optionally `admin3`, and compares them against the live AGOL data for the configured country.

| Issue type | Severity | What it means |
|---|---|---|
| `missing_in_questionnaire` | MEDIUM | Code exists in AGOL but not in the questionnaire |
| `extra_in_questionnaire` | MEDIUM | Code exists in the questionnaire but not in AGOL |
| `label_mismatch` | LOW | Same code found in both, but the label text differs |
| `parent_mismatch` | MEDIUM | Same code found in both, but the parent admin code differs |
| `blank_code` | HIGH | An admin row has no name/code — the cell is empty |
| `duplicate_code` | HIGH | The same code appears more than once in the same list |

Severity LOW means the questionnaire will work but labels are out of date. MEDIUM means there is a structural difference that needs review. HIGH means the questionnaire has a data quality problem that should be fixed before use.

### Output files

The tool writes two files to the configured `output_dir`:

- **`admin_check_report_{source_name}_{timestamp}.xlsx`** — Excel workbook with two sheets:
    - *Summary* — one row per admin level, showing total counts for the questionnaire and AGOL, and a count of each issue type
    - *Details* — one row per individual issue, with the code, both labels, both parent codes, and the source row in the questionnaire
- **`admin_check_report_{source_name}_{timestamp}.csv`** — the same Details rows in CSV format for easier filtering

### How to run

From the repository root with the `diem-validation` environment active:

```powershell
tool_admin_check
```

Optional overrides:

```powershell
# Use a specific questionnaire file instead of the auto-detected latest one
tool_admin_check --source-file "my_questionnaire_en_NGA_20260501.xlsx"

# Use a different config file
tool_admin_check --config "C:/path/to/admin_tools_config.yaml"
```

---

## tool_admin_sync

Creates a new questionnaire file with the admin lists updated from AGOL. It does not modify the original file — it always writes a new timestamped copy. Use this after running `tool_admin_check` to apply the corrections.

### Sync modes

| Mode | What it does |
|---|---|
| `subset_from_agol` | For every code already in the questionnaire, update the label and parent from AGOL if that code exists there. Codes that exist in the questionnaire but not in AGOL are kept as-is. Removes duplicate codes. |
| `full_from_agol` | Replaces the admin lists entirely with everything fetched from AGOL for the configured country. Codes that were in the questionnaire but not in AGOL are removed. |
| `keep_previous` | Copies the file without making any admin changes. Useful when you want a timestamped copy for audit purposes without modifying content. |

**`subset_from_agol`** is the default and the recommended starting point. It corrects labels and parent codes for codes the questionnaire already uses, but does not add or remove entire admin units — so the geographic scope of the questionnaire stays exactly as the country team defined it.

**`full_from_agol`** should be used when you are building or rebuilding admin lists from scratch, or when the country's admin structure has changed significantly and you want the questionnaire to reflect the full current AGOL picture.

### Preserving sample filters

When `preserve_my_filter_sample` is `true` (the default), the tool copies the value in the `my_filter_sample` column from each original row into the corresponding row in the output file. This column controls sample-based filtering in the questionnaire, so preserving it means the sync does not accidentally wipe out filter configuration.

### Output file

The tool writes a single Excel file to the configured `output_dir`:

```
{source_name}_adminsync_{mode}_{timestamp}.xlsx
```

Cell formatting and styles from the original file are preserved where possible.

### How to run

From the repository root:

```powershell
tool_admin_sync
```

Optional overrides:

```powershell
# Use a specific questionnaire file
tool_admin_sync --source-file "my_questionnaire_en_NGA_20260501.xlsx"

# Override the sync mode without editing the config file
tool_admin_sync --sync-mode full_from_agol

# Use a different config file
tool_admin_sync --config "C:/path/to/admin_tools_config.yaml"

# Skip writing output (useful for confirming the source file resolves correctly)
# Set dry_run: true in admin_tools_config.yaml instead
```

---

## Configuration

Both tools read `configuration/admin_tools_config.yaml`. If a setting is missing from that file, the tool falls back to the corresponding value in `configuration/validation_config.yaml`.

```yaml
tool: kobo          # "kobo" or "geopoll"
iso3: NGA           # Three-letter ISO country code
language: en        # Language code for label column detection: en, fr, ar, es
include_admin3: false  # Set to true to also check/sync the admin3 level
dry_run: false      # Set to true to skip writing the output file (sync only)

# Optional folder overrides. Leave blank to use the defaults from validation_config.yaml.
validated_dir: ""
output_dir: "C:/Temp/questionnaire_validation/admin_tools_output"

source:
  mode: standard    # "standard" or "custom" — see below
  file_name: ""     # Filename to use in custom mode
  custom_dir: "C:/Temp"  # Extra folder to search in custom mode

sync:
  mode: subset_from_agol        # subset_from_agol, full_from_agol, or keep_previous
  preserve_my_filter_sample: true
```

### Source selection

**`source.mode: standard`** (default) — the tool automatically picks the most recently modified file matching the pattern `validated_questionnaire_{tool}_*.xlsx` in the configured `validated_dir`. If `language` and `iso3` are set, they are used to narrow the search.

**`source.mode: custom`** — the tool looks for the file named in `source.file_name`. It searches the following locations in order:
1. `source.custom_dir` (if set)
2. `validated_dir`
3. `working_dir` from validation config
4. Repository root

You only need to provide the filename, not the full path, and the tool will find it across those locations.

---

## AGOL connection

Both tools query two ArcGIS Online FeatureServer endpoints:

- **Admin1 and Admin2** — fetched from the *Administrative Boundaries Reference* service
- **Admin3** — fetched from the *Reference Admin 3* service (only when `include_admin3: true`)

All queries filter by ISO3 country code. The tools require an internet connection. Queries time out after 40 seconds. There is no caching — each run fetches fresh data.
