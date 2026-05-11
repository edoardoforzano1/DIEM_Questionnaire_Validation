# KoBo Validator - Function Reference

Script: `scripts/kobo_validator.py` - ~3,300 lines - 88 functions

This page covers the functions that matter for understanding, tracing, and modifying validator behavior. Private helper functions (underscore-prefixed) are listed under the relevant stage but not expanded.

To regenerate the full auto-documented spec after code changes:
```powershell
conda run -n diem-validation python scripts/regenerate_function_docs.py
```

---

## Pipeline at a Glance

| Stage | What it does | Key entry points |
|---|---|---|
| 1 - Config | Load config + optional profile overlay | `_load_effective_config` |
| 2 - Reference resolution | Pick template or previous-round baseline | `find_kobo_template` |
| 3 - Reading | Parse survey and choices sheets | `read_kobo_survey`, `read_kobo_choices`, `build_question_options` |
| 4 - Placeholders | Apply Additional Information substitutions | `read_additional_info`, `restore_to_vanilla`, `apply_replacements` |
| 5 - Choice lists | Rebuild crop/admin choice lists for comparison | `read_crop_choice_rows_for_compare`, `fetch_admin_choice_rows_for_compare`, `replace_choice_lists_for_compare` |
| 6 - Normalization | Normalize text and logic expressions | `normalize_text_expr`, `normalize_logic_expr` |
| 7 - Comparison | Question/choice diff against reference | `compare_question_presence`, `compare_mandatory_kobo`, `compare_question_labels` and field-level comparators |
| 8 - Relevant validation | Validate `relevant` expression references and syntax | `validate_relevant`, `validate_questionnaire_structure` |
| 9 - Critical sets | Structural completeness rules | (shared with GeoPoll via config) |
| 10 - Export | Write Excel report sheets and validated output | `export_report`, `produce_validated_questionnaire` |

---

## Stage 1 - Config

### `_load_effective_config`

```python
def _load_effective_config(cfg_path: Path) -> tuple[dict, Path | None, Path]:
```

Loads `validation_config.yaml` and, if `config_profile` is set, merges the profile overlay on top. Returns the merged config dict used throughout the pipeline.

*Internals: `_reference_scope_label`, `_not_in_reference_text`*

---

## Stage 2 - Reference Resolution

### `find_kobo_template`

```python
def find_kobo_template(language: str, templates_dir: Path) -> Path:
```

Scans `templates_dir` for KoBo XLSForm files matching the configured language, extracts dates from filenames, and returns the most recent match.

*Internals: `_write_config_snapshot_kobo`*

---

## Stage 3 - Reading

### `read_kobo_survey`

```python
def read_kobo_survey(
    path: str,
    language: str = "en",
    _wb=None,
) -> pl.DataFrame:
```

Reads the `survey` sheet of the XLSForm. Resolves the language-specific label column (e.g. `label::English`), normalizes `mandatory` values, and returns a survey DataFrame with consistent column names.

### `read_kobo_choices`

```python
def read_kobo_choices(
    path: str,
    language: str = "en",
    _wb=None,
) -> pl.DataFrame:
```

Reads the `choices` sheet and returns a flat choices DataFrame with `list_name`, `name`, and label columns.

### `build_question_options`

```python
def build_question_options(
    survey_df: pl.DataFrame,
    choices_df: pl.DataFrame,
) -> pl.DataFrame:
```

Joins the survey and choices tables to produce a per-question option list - used downstream for choice comparisons.

*Internals: `_find_label_col`, `_normalize_mandatory`*

---

## Stage 4 - Placeholders

### `read_additional_info`

```python
def read_additional_info(
    country_path: str,
    language: str = "en",
) -> dict[str, str]:
```

Reads the Additional Information sheet and builds a replacement map. Handles `#placeholder#`-style tokens and language-specific key variants.

### `restore_to_vanilla`

```python
def restore_to_vanilla(
    current_df: pl.DataFrame,
    reference_df: pl.DataFrame,
    cols: list[str],
    key_cols: list[str] | None = None,
) -> pl.DataFrame:
```

Replaces crop/admin choice lists back to their placeholder state before comparison (the "vanilla" template form). This ensures the comparison is against the unlocalized template, not the filled-in country version.

### `apply_replacements`

```python
def apply_replacements(
    df: pl.DataFrame,
    pairs: dict[str, str],
    cols: list[str],
) -> pl.DataFrame:
```

Applies the Additional Information replacement map to all text fields in the survey and choices DataFrames.

*Internals: `read_additional_info._placeholder_aliases`, `read_crop_choice_rows_for_compare`, `fetch_admin_choice_rows_for_compare`, `replace_choice_lists_for_compare`*

---

## Stage 5 - Choice List Rebuild (Previous-Round Workflow)

### `read_crop_choice_rows_for_compare`

```python
def read_crop_choice_rows_for_compare(
    country_path: str,
    language: str,
) -> dict[str, list[tuple[str, str]]]:
```

Reads the `Crop list` sheet and builds the crop choice rows that replace placeholders in the choices sheet.

### `fetch_admin_choice_rows_for_compare`

```python
def fetch_admin_choice_rows_for_compare(iso3: str) -> dict[str, list[tuple]]:
```

Fetches admin area choice rows from AGOL. Returns an empty result if the connection fails (flagged as `replacement_additional_info_missing` in the report).

### `replace_choice_lists_for_compare`

```python
def replace_choice_lists_for_compare(
    choices_df: pl.DataFrame,
    country_rows: dict[str, list[tuple]],
) -> pl.DataFrame:
```

Applies rebuilt crop and admin rows to the choices DataFrame, replacing placeholder rows with real localized values before comparison.

---

## Stage 6 - Normalization

### `normalize_text_expr`

```python
def normalize_text_expr(col_name: str) -> pl.Expr:
```

Lowercases and strips label text for string comparison.

### `normalize_simple_expr`

```python
def normalize_simple_expr(col_name: str) -> pl.Expr:
```

Strips and normalizes a single expression string (used for `required`, `constraint`, `hint`, etc.).

### `normalize_logic_expr`

```python
def normalize_logic_expr(col_name: str) -> pl.Expr:
```

Canonicalizes `relevant` and `calculation` expressions - normalizes spacing and variable reference formatting before comparing against baseline.

---

## Stage 7 - Comparison

### `compare_question_presence`

```python
def compare_question_presence(
    current: pl.DataFrame,
    reference: pl.DataFrame,
) -> tuple[pl.DataFrame, pl.DataFrame]:
```

Returns added and removed questions by comparing Q Name sets. Applies the prefix-count downgrade logic for `removed_question` severity.

### `compare_mandatory_kobo`

```python
def compare_mandatory_kobo(
    current: pl.DataFrame,
    reference: pl.DataFrame,
) -> pl.DataFrame:
```

Compares the mandatory column question by question, producing `mandatory_column_mismatch` issues. `mandatory_to_optional` is produced during presence issue unification when a removed baseline question is replaced by an optional counterpart (`o_` prefix).

### `compare_question_labels`

```python
def compare_question_labels(
    current_vanilla: pl.DataFrame,
    reference: pl.DataFrame,
    current_orig=None,
) -> pl.DataFrame:
```

Normalizes and compares label text for all questions in common. Produces `label_mismatch` issues.

### `compare_list_name_changes`

```python
def compare_list_name_changes(
    current: pl.DataFrame,
    reference: pl.DataFrame,
) -> pl.DataFrame:
```

Detects questions whose linked choices list (`select_one`/`select_multiple` list name) changed - produces `choices_list_changed`.

### `compare_type_changes`

```python
def compare_type_changes(
    current: pl.DataFrame,
    reference: pl.DataFrame,
    current_options: pl.DataFrame | None = None,
    reference_options: pl.DataFrame | None = None,
) -> pl.DataFrame:
```

Risk-based Q Type comparison with normalization and integrity checks - produces `type_changed` with dynamic severity (HIGH for invalid/incompatible transitions, MEDIUM for compatible changes). Reported under Questionnaire Structure for centralized type-integrity review.

### `compare_required_changes` / `compare_constraint_changes` / `compare_choice_filter_changes` / `compare_appearance_changes` / `compare_calculation_changes` / `compare_hint_changes`

```python
def compare_required_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
def compare_constraint_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
def compare_choice_filter_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
def compare_appearance_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
def compare_calculation_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
def compare_hint_changes(current: pl.DataFrame, reference: pl.DataFrame) -> pl.DataFrame:
```

Each compares the corresponding XLSForm field against baseline and produces a single MEDIUM-severity issue type per function when the field changed.

### `compare_option_labels_single` / `compare_option_presence_single`

Per-question helpers comparing choice labels and presence (used within the choice comparison pipeline).

*Internals: `_canonical_option_key_expr`*

---

## Stage 8 - Relevant Validation

### `validate_relevant`

```python
def validate_relevant(
    current_survey: pl.DataFrame,
    reference_survey: pl.DataFrame,
) -> pl.DataFrame:
```

The main `relevant` expression validator. For each question with a `relevant` field:

- Extracts all variable references from the expression.
- Checks each reference exists in the survey's Q Name list -> `broken_relevant_reference` HIGH.
- Detects inexact references where the exact variable is missing but a similar optional counterpart exists (e.g. `o_var`) -> `relevant_inexact_reference` HIGH.
- Compares against baseline -> `relevant_modified` MEDIUM.

### `validate_questionnaire_structure`

```python
def validate_questionnaire_structure(
    current_survey: pl.DataFrame,
    current_choices: pl.DataFrame | None = None,
    template_survey: pl.DataFrame | None = None,
    replacement_pairs: dict[str, str] | None = None,
) -> pl.DataFrame:
```

Separate from `validate_relevant`. Scans structure/reference integrity outside relevant-drift comparison:

- `duplicate_qname` HIGH (duplicate Q Names in survey).
- `duplicate_choice_name` HIGH (duplicate names within a choice list).
- `kobo_ref_loose_syntax` HIGH or MEDIUM (loose `$var` instead of `${var}`).
- `kobo_ref_missing_variable` HIGH (`${var}` references undefined variable).
- `placeholder_not_found` HIGH (`#token#` not resolvable via template or Additional information).
- `placeholder_should_use_kobo_ref` HIGH (`#token#` matches a survey variable and should be `${var}`).

Report mapping note:
- Summary/Structure "Skip logic references (relevant)" row comes from `validate_relevant`.
- Summary/Structure "Q type integrity, duplicates and KoBo references" row comes from `STRUCTURE_ISSUE_TYPES` only.
- `placeholder_*` issues are emitted by `validate_questionnaire_structure` but displayed under **Replacement Issues**.

---

## Stage 9 - Critical Sets

Uses the same `validate_critical_sets`, `validate_prefix_counts`, and `validate_crop_harvest` logic as GeoPoll, driven by `critical_sets.yaml`. For the WEALTH set, both `hh_wealth_*` and `o_hh_wealth_*` are counted as valid. See [GeoPoll function reference - Stage 10](geopoll-validator.md#stage-10-critical-sets) for function descriptions.

---

## Stage 10 - Export

### `export_report`

```python
def export_report(
    all_issues,
    result_file,
    found_info=None,
    rules=None,
    critical_issues=None,
    count_issues=None,
    replacement_status=None,
):
```

Top-level export function. Creates the output workbook, calls each sheet writer in sequence, auto-fits columns, and saves the report.

### `produce_validated_questionnaire`

```python
def produce_validated_questionnaire(
    cfg: dict,
    reference_survey: pl.DataFrame,
    replacement_pairs: dict,
) -> tuple[str, dict]:
```

Produces the validated questionnaire output file (previous-round workflow only). Applies all placeholder replacements, rebuilds crop/admin choice rows, and performs a final scan for unresolved tokens.

*Sheet writers: `write_kobo_summary_sheet`, `write_kobo_structure_sheet`, `write_kobo_replacement_sheet`, `write_kobo_critical_sets_sheet`, `write_kobo_question_changes_sheet`, `write_kobo_choice_changes_sheet`*

*Internals: cell formatting helpers (`_header_row`, `_data_row`, `_section_header`, `_autofit`, `_set_status`), issue table builder (`_issues_table`, `_issues_col_map`, `_action_for_issue_type`), replacement builders (`_build_replacement_issue_rows`, `_build_replacement_status_rows`), admin sheet writers (`_apply_admin_sheets`, `_fetch_admin_reference`, `_write_table_sheet`)*
