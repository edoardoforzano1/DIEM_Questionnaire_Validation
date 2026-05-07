# GeoPoll Validator (`scripts/geopoll_validator.py`)

## Functional Blocks

### Configuration and run context

- `_load_effective_config`
- `resolve_reference_file`
- `load_critical_sets`
- `prepare_run`
- `_write_config_snapshot_geopoll`

### Sheet readers and parsing helpers

- `read_survey_sheet`
- `build_questions_df`
- `parse_options`
- `explode_options`
- `explode_codes`

### Placeholder and replacement handling

- `read_additional_information`
- `build_placeholder_restore_map`
- `restore_placeholder_cells`
- `build_additional_info_replacements`
- `apply_text_replacements`

### Logic and structural checks

- `compare_question_presence`
- `compare_mandatory`
- `compare_qtype_changes`
- `compare_option_labels_single`
- `validate_skip_patterns`
- `validate_critical_sets`
- `validate_prefix_counts`
- `validate_crop_harvest`

### Report writers and output

- `write_summary_sheet`
- `write_critical_sets_sheet`
- `write_question_changes_sheet`
- `write_option_changes_sheet`
- `export_validation_report`
