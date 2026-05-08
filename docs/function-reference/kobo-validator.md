# KoBo Validator â€” Function Reference

Script: `scripts/kobo_validator.py` Â· ~3,300 lines Â· 88 functions

This page covers the functions that matter for understanding, tracing, and modifying validator behavior. Private helper functions (underscore-prefixed) are listed under the relevant stage but not expanded.

To regenerate the full auto-documented spec after code changes:
```powershell
conda run -n base python scripts/regenerate_function_docs.py
```

---

## Pipeline at a Glance

| Stage | What it does | Key entry points |
|---|---|---|
| 1 Â· Config | Load config + optional profile overlay | `_load_effective_config` |
| 2 Â· Reference resolution | Pick template or previous-round baseline | `find_kobo_template` |
| 3 Â· Reading | Parse survey and choices sheets | `read_kobo_survey`, `read_kobo_choices`, `build_question_options` |
| 4 Â· Placeholders | Apply Additional Information substitutions | `read_additional_info`, `restore_to_vanilla`, `apply_replacements` |
| 5 Â· Choice lists | Rebuild crop/admin choice lists for comparison | `read_crop_choice_rows_for_compare`, `fetch_admin_choice_rows_for_compare`, `replace_choice_lists_for_compare` |
| 6 Â· Normalization | Normalize text and logic expressions | `normalize_text_expr`, `normalize_logic_expr` |
| 7 Â· Comparison | Question/choice diff against reference | `compare_question_presence`, `compare_mandatory_kobo`, `compare_question_labels` and field-level comparators |
| 8 Â· Relevant validation | Validate `relevant` expression references and syntax | `validate_relevant`, `validate_questionnaire_structure` |
| 9 Â· Critical sets | Structural completeness rules | (shared with GeoPoll via config) |
| 10 Â· Export | Write Excel report sheets and validated output | `export_kobo_report`, `write_validated_questionnaire` |

---

## Stage 1 Â· Config

### `_load_effective_config`
Loads `validation_config.yaml` and, if `config_profile` is set, merges the profile overlay on top. Returns the merged config dict used throughout the pipeline.

*Internals: `_reference_scope_label`, `_not_in_reference_text`*

---

## Stage 2 Â· Reference Resolution

### `find_kobo_template`
Scans `templates_dir` for KoBo XLSForm files matching the configured language, extracts dates from filenames, and returns the most recent match.

*Internals: `_write_config_snapshot_kobo`*

---

## Stage 3 Â· Reading

### `read_kobo_survey`
Reads the `survey` sheet of the XLSForm. Resolves the language-specific label column (e.g. `label::English`), normalizes `mandatory` values, and returns a survey DataFrame with consistent column names.

### `read_kobo_choices`
Reads the `choices` sheet and returns a flat choices DataFrame with `list_name`, `name`, and label columns.

### `build_question_options`
Joins the survey and choices tables to produce a per-question option list â€” used downstream for choice comparisons.

*Internals: `_find_label_col`, `_normalize_mandatory`*

---

## Stage 4 Â· Placeholders

### `read_additional_info`
Reads the Additional Information sheet and builds a replacement map. Handles `#placeholder#`-style tokens and language-specific key variants.

### `restore_to_vanilla`
Replaces crop/admin choice lists back to their placeholder state before comparison (the "vanilla" template form). This ensures the comparison is against the unlocalized template, not the filled-in country version.

### `apply_replacements`
Applies the Additional Information replacement map to all text fields in the survey and choices DataFrames.

*Internals: `read_additional_info._placeholder_aliases`, `read_crop_choice_rows_for_compare`, `fetch_admin_choice_rows_for_compare`, `replace_choice_lists_for_compare`*

---

## Stage 5 Â· Choice List Rebuild (Previous-Round Workflow)

### `read_crop_choice_rows_for_compare`
Reads the `Crop list` sheet and builds the crop choice rows that replace placeholders in the choices sheet.

### `fetch_admin_choice_rows_for_compare`
Fetches admin area choice rows from AGOL. Returns an empty result if the connection fails (flagged as `replacement_additional_info_missing` in the report).

### `replace_choice_lists_for_compare`
Applies rebuilt crop and admin rows to the choices DataFrame, replacing placeholder rows with real localized values before comparison.

---

## Stage 6 Â· Normalization

### `normalize_text_expr`
Lowercases and strips label text for string comparison.

### `normalize_simple_expr`
Strips and normalizes a single expression string (used for `required`, `constraint`, `hint`, etc.).

### `normalize_logic_expr`
Canonicalizes `relevant` and `calculation` expressions â€” normalizes spacing and variable reference formatting before comparing against baseline.

---

## Stage 7 Â· Comparison

### `compare_question_presence`
Returns added and removed questions by comparing Q Name sets. Applies the prefix-count downgrade logic for `removed_question` severity.

### `compare_mandatory_kobo`
Compares the mandatory column question by question, producing `mandatory_to_optional` and `mandatory_column_mismatch` issues.

### `compare_question_labels`
Normalizes and compares label text for all questions in common. Produces `label_mismatch` issues.

### `compare_list_name_changes`
Detects questions whose linked choices list (`select_one`/`select_multiple` list name) changed â€” produces `choices_list_changed`.

### `compare_type_changes`
Detects question type changes â€” produces `type_changed`.

### `compare_required_changes` / `compare_constraint_changes` / `compare_choice_filter_changes` / `compare_appearance_changes` / `compare_calculation_changes` / `compare_hint_changes`
Each compares the corresponding XLSForm field against baseline and produces a single MEDIUM-severity issue type per function when the field changed.

### `compare_option_labels_single` / `compare_option_presence_single`
Per-question helpers comparing choice labels and presence (used within the choice comparison pipeline).

*Internals: `_canonical_option_key_expr`*

---

## Stage 8 Â· Relevant Validation

### `validate_relevant`
The main `relevant` expression validator. For each question with a `relevant` field:
- Extracts all variable references from the expression.
- Checks each reference exists in the survey's Q Name list â†’ `broken_relevant_reference` HIGH.
- Checks for ambiguous tokenization â†’ `relevant_inexact_reference` HIGH.
- Compares against baseline â†’ `relevant_modified` MEDIUM.
- Checks for loose syntax (reference without `${}`) â†’ `kobo_ref_loose_syntax` MEDIUM.

### `validate_questionnaire_structure`
Combines `validate_relevant` with duplicate-name checks:
- `duplicate_qname` HIGH (duplicate Q Names in survey).
- `duplicate_choice_name` MEDIUM (duplicate names within a choice list).
- `kobo_ref_missing_variable` HIGH (`${var}` references undefined variable).

---

## Stage 9 Â· Critical Sets

Uses the same `validate_critical_sets`, `validate_prefix_counts`, and `validate_crop_harvest` logic as GeoPoll, driven by `critical_sets.yaml`. For the WEALTH set, both `hh_wealth_*` and `o_hh_wealth_*` are counted as valid. See [GeoPoll function reference - Stage 10](geopoll-validator.md#stage-10-critical-sets) for function descriptions.

---

## Stage 10 Â· Export

### `export_kobo_report`
Top-level export function. Creates the output workbook, calls each sheet writer in sequence, auto-fits columns, and saves the report.

### `write_validated_questionnaire`
Produces the validated questionnaire output file (previous-round workflow only). Applies all placeholder replacements, rebuilds crop/admin choice rows, and performs a final scan for unresolved tokens.

*Sheet writers: `write_kobo_summary_sheet`, `write_kobo_structure_sheet`, `write_kobo_replacement_sheet`, `write_kobo_critical_sets_sheet`, `write_kobo_question_changes_sheet`, `write_kobo_choice_changes_sheet`*

*Internals: cell formatting helpers (`_header_row`, `_data_row`, `_section_header`, `_autofit`, `_set_status`), issue table builder (`_issues_table`, `_issues_col_map`, `_action_for_issue_type`), replacement builders (`_build_replacement_issue_rows`, `_build_replacement_status_rows`), admin sheet writers (`_apply_admin_sheets`, `_fetch_admin_reference`, `_write_table_sheet`)*

