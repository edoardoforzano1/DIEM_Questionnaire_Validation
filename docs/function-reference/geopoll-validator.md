# GeoPoll Validator  -  Function Reference

Script: `scripts/geopoll_validator.py`  -  ~5,700 lines  -  147 functions

This page covers the functions that matter for understanding, tracing, and modifying validator behavior. Private helper functions (underscore-prefixed) are listed under the relevant stage but not expanded  -  they exist to support the public functions in that stage.

To regenerate the full auto-documented spec after code changes:
```powershell
conda run -n base python scripts/regenerate_function_docs.py
```

---

## Pipeline at a Glance

| Stage | What it does | Key entry points |
|---|---|---|
| 1  -  Config | Load config + optional profile overlay | `_load_effective_config` |
| 2  -  Reference resolution | Pick template or previous-round baseline | `resolve_reference_file`, `find_latest_template` |
| 3  -  Setup | Resolve language, prepare output paths | `prepare_run` |
| 4  -  Reading | Parse survey rows, answer options, code tokens | `read_survey_sheet`, `build_questions_df` |
| 5  -  Options & placeholders | Explode options/codes, apply AI substitutions | `explode_options`, `explode_codes`, `analyze_additional_info_substitutions`, `apply_text_replacements` |
| 6  -  Crop rebuild | Rebuild crop question blocks for validated output | `rebuild_crop_questions_for_deployed_form` |
| 7  -  Normalization | Normalize text, codes, mandatory values before comparison | `normalize_text_expr`, `normalize_code_token_expr`, `normalize_mandatory_expr` |
| 8  -  Skip validation | Three-layer skip-pattern check | `validate_skip_patterns` |
| 9  -  Comparison | Question/option/code diff against reference | `compare_question_presence`, `compare_mandatory`, `build_question_changes_view`, `build_option_changes_view` |
| 10  -  Critical sets | Structural completeness rules | `validate_critical_sets`, `validate_prefix_counts`, `validate_crop_harvest` |
| 11  -  Export | Write Excel report sheets | `export_validation_report` |

---

## Stage 1  -  Config

### `_load_effective_config`
Loads `validation_config.yaml` and, if `config_profile` is set, merges the profile overlay on top. Returns the merged config dict. This is the only place run parameters are resolved  -  everything downstream reads from this dict.

*Internals: `_reference_scope_label`, `_not_in_reference_text` (label/text builders for report metadata)*

---

## Stage 2  -  Reference Resolution

### `resolve_reference_file`
Given the resolved config, returns the path to the baseline questionnaire file. Delegates to `find_latest_template` for `latest_template` mode or reads `previous_round_file` directly for `previous_round` mode.

### `find_latest_template`
Scans `templates_dir` for files matching the configured language and tool, extracts dates from filenames via `extract_date_from_name`, and returns the most recent match.

### `load_critical_sets`
Reads `configuration/critical_sets.yaml` and returns the three rule structures: `exact_sets`, `min_count_sets`, and `crop_harvest`. Used downstream by the critical-set check functions.

*Internals: `_normalize_header_name`, `_header_tokens`, `_is_language_candidate_header`, `resolve_language_column`, `detect_language_from_filename`, `choose_target_language`, `extract_date_from_name`*

---

## Stage 3  -  Setup

### `prepare_run`
Creates output directories, writes a config snapshot to the output folder, and returns a `RunContext` object used throughout the pipeline. Also emits the run banner to the console.

*Internals: `_write_config_snapshot_geopoll`*

---

## Stage 4  -  Reading

### `read_survey_sheet`
Opens the questionnaire Excel file and reads the survey rows using language-aware column resolution. Handles column alias matching (e.g. `Skip Pattern` / `Skip pattern `) and returns a raw DataFrame.

### `build_questions_df`
Cleans and normalizes the raw survey DataFrame: strips whitespace from headers, resolves column aliases, and enforces consistent column names. This is the normalized question table used in all comparisons.

*Internals: `_resolve_column_by_aliases`*

---

## Stage 5  -  Options & Placeholders

### `parse_options`
Extracts numbered options from question text using the `N) Label` format. Returns a list of `(position, label)` tuples per question.

### `explode_options`
Calls `parse_options` for each question and returns an options DataFrame with one row per `(Q Name, position, label)`. This is the flat options table used in option comparisons.

### `parse_codes_cell` / `explode_codes`
Same pattern for code tokens  -  parses the Codes column value per question, then explodes into a flat `(Q Name, code_position, token)` table used in code comparisons.

### `read_additional_information`
Reads the Additional Information sheet and returns a raw replacement map. This is the source for all `$...$` placeholder substitutions.

### `analyze_additional_info_substitutions`
Takes the raw Additional Information map and the question DataFrame, and identifies which placeholders have matching replacement keys. Returns a substitution plan including any unmatched tokens that will become `replacement_missing_key` issues.

### `build_additional_info_replacements` / `build_additional_info_replacements_by_language`
Builds the final replacement dict from the substitution plan, handling language-specific key resolution. The `_by_language` variant resolves per-language override keys.

### `apply_text_replacements`
Applies the replacement dict to all text columns in the question DataFrame. Called on both current and reference questionnaires before comparison.

### `apply_placeholder_conversions`
Post-processes any remaining `$...$` tokens that weren't resolved by the replacement map, flagging them for the Replacement Issues sheet.

*Internals: `_normalize_placeholder_token`, `_is_crop_placeholder_token`, `_contains_crop_marker_text`, `_clean_header`, `_find_column`, `read_generic_sheet`, `read_crop_list`, `has_placeholder`, `build_placeholder_restore_map`, `restore_placeholder_cells`, `_normalize_placeholder_key`, `_placeholder_lookup_aliases`, `_build_placeholder_index`, `_lookup_placeholder_replacement`, `_language_code_for_text_column`, `_placeholder_token_explicit_lang`*

---

## Stage 6  -  Crop Rebuild

### `rebuild_crop_questions_for_deployed_form`
Rebuilds the crop question rows in the validated questionnaire output  -  replaces crop-placeholder rows with the actual selected-crop rows from the Crop list sheet. Only runs in `previous_round` mode.

*Internals: `extract_crop_metadata`, `find_crop_placeholder_questions`, `_is_selected_crop_value`, `_build_sorted_crop_entries`, `build_crop_option_block`, `build_crop_code_block`*

---

## Stage 7  -  Normalization

These three functions normalize values before comparison to avoid false positives from harmless formatting differences.

### `normalize_text_expr`
Lowercases, strips, and canonicalizes label text for string comparison.

### `normalize_code_token_expr`
Normalizes code-token strings (trims spaces, lowercases).

### `normalize_mandatory_expr`
Maps mandatory column values to a canonical set (`mandatory`, `mandatory-panel`, `optional`, etc.).

---

## Stage 8  -  Skip Validation

### `validate_skip_patterns`
The main skip-validation entry point. Runs three layers:

**Pre-check (internal consistency only):** if `Specify` is blank and both `Skip Pattern` and `Default` are filled but disagree semantically â†’ `default_skip_modified` INFO. This is a within-questionnaire check, not a reference comparison.

**Layer 1  -  Effective rule comparison against reference:** resolves the effective skip rule per question (priority: `Specify` > `Skip Pattern` > `Default`) on both sides, then calls `_check_skip_consistency`. Produces:

- `skipPattern_invalid_qname` HIGH  -  routing target Q Name doesn't exist in current questionnaire.
- `skipPattern_invalid_qnameCategory` HIGH  -  flexible rule expects an optional target, but Skip Pattern routes to a mandatory question.
- `skip_pattern_empty` HIGH  -  Skip Pattern is empty when Default/Specify expects routing somewhere.
- `skipPattern_changes` INFO  -  effective rule differs from reference (routing target or condition changed).
- `skipPattern_range_mismatch` INFO  -  option code numbers in Skip Pattern differ from what reference specifies for the same target.

**Layer 3  -  Option code existence:** checks that every numeric code referenced in the effective current skip rule exists in the current answer options. Violations â†’ `skipPattern_range_invalid` HIGH.

### `_check_skip_consistency`
Per-question consistency evaluator. Given the current effective skip text and the parsed rules from the reference, checks whether required target Q Names appear in the skip text and whether code ranges match. Returns a list of issue description strings.

### `_parse_default_skip_rules`
Parses the `Default skip patterns & conditional` column value into structured rule objects (`{targets, is_flexible, is_next_question, option_codes, raw}`). Handles compact and verbose styles, including multiple clauses on one line.

*Internals: `_normalize_skip_text`, `_parse_skip_option_codes`, `_extract_referenced_qnames`, `_extract_qname_tokens`, `_extract_qname_like`, `_extract_condition_codes`, `_extract_skip_codes_for_target`, `_semantic_skip_signature`*

---

## Stage 9  -  Comparison

### `compare_question_presence`
Returns added and removed questions by comparing Q Name sets between current and reference. Applies the prefix-count downgrade logic: removals whose group still meets the min-count threshold are downgraded from HIGH to INFO.

### `compare_mandatory`
Compares mandatory column values question by question, producing `mandatory_to_optional` and `mandatory_column_mismatch` issues.

### `compare_qtype_changes`
Compares question types, using `_qtype_mode` to classify type transitions as compatible or incompatible. Severity depends on whether the question is mandatory.

### `compare_legacy_text_field_changes`
Compares `Randomize`, `Conditional`, `Programming Instructions`, and `Core questions only` columns. Severity for `Conditional` depends on mandatory status.

### `compare_question_labels_single`
Normalizes and compares label text for a single question. Used within `build_question_changes_view`.

### `build_question_changes_view`
Orchestrates all question-level comparison functions and assembles the Question Changes sheet DataFrame.

### `build_option_changes_view`
Orchestrates option comparisons (`removed_option`, `added_option`, `option_label_mismatch`, `option_position_renumbered_same_label`) and code comparisons (`codes_col_removed`, `codes_col_added`, `codes_col_token_mismatch`, `codes_col_renumbered_same_token`).

*Internals: `make_presence_issues`, `make_mandatory_issues`, `make_option_issues`, `make_option_presence_issues`, `_mandatory_cat_expr`, `_normalize_qtype_value`, `_qtype_mode`, `_qtype_change_severity`, `compare_option_labels_single`, `compare_option_presence_single`, `compare_option_code_renumber_single`, `compare_codes_presence_single`, `compare_codes_token_mismatch_single`, `compare_codes_renumber_single`, `build_codes_changes_view`*

---

## Stage 10  -  Critical Sets

### `validate_critical_sets`
Iterates over `exact_sets` rules from `critical_sets.yaml` and produces `missing_critical_question`, `critical_mandatory_mismatch`, and `advisory_question` issues.

### `validate_prefix_counts`
Iterates over `min_count_sets` rules and produces `missing_critical_question` issues (with `field = count`) when a prefix group has fewer questions than the threshold. For the WEALTH set, both `hh_wealth_*` and `o_hh_wealth_*` are counted.

### `validate_crop_harvest`
Applies the `crop_harvest` completeness rule  -  checks that either the minimal or the full allowed question set is present.

---

## Stage 11  -  Export

### `export_validation_report`
Top-level export function. Creates the output workbook, calls each sheet writer in sequence, auto-fits columns, and saves to the configured output path.

### `write_summary_sheet`
Builds the Summary sheet: critical-set status table, questionnaire structure check table, replacement status table, and question-changes count table.

### `write_structure_skip_sheet`
Writes the Questionnaire Structure sheet from the skip-validation and duplicate-check results.

### `write_replacement_issues_sheet`
Writes the Replacement Issues sheet from placeholder analysis results.

### `write_critical_sets_sheet`
Writes the Critical Sets sheet from `validate_critical_sets` and `validate_prefix_counts` results.

### `write_question_changes_sheet`
Writes the Question Changes sheet with inline word-diff highlights for label and metadata changes.

### `write_option_changes_sheet`
Writes the Option Changes sheet from option and code comparison results.

*Internals: `_header_row`, `_section_header`, `_data_row`, `_autofit`, `_action_for_issue_type`, `_issues_col_map`, `_issues_table`, `_tokenize_for_word_diff`, `_coalesce_segments`, `_build_diff_segments`, `_set_rich_text`, `_apply_inline_diff_for_issue`, `_set_status`, `_cat_counts`, `_tick`, `_add_issue_reason`, `_resolve_survey_sheet`, `_sheet_header_map`, `_count_selected_crops`, `_placeholder_scan_columns`, `_extract_placeholder_tokens`, `_has_broken_placeholder_token`, `_count_unresolved_placeholders`, `_selected_crop_labels`, `_selected_crop_entries`, `_join_short`, `_build_crop_round_delta_issue_rows`, `_build_replacement_issue_rows`, `_fetch_admin_reference`, `_write_table_sheet`, `_apply_admin_sheets`, `_build_replacement_status_rows`, `write_validated_questionnaire`*

