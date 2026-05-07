# KoBo Validator (`scripts/kobo_validator.py`)

## Functional Blocks

### Configuration and setup

- `_load_effective_config`
- `find_kobo_template`
- `_write_config_snapshot_kobo`

### Read and normalize workbook structures

- `read_kobo_survey`
- `read_kobo_choices`
- `build_question_options`
- `read_additional_info`
- `restore_to_vanilla`
- `apply_replacements`

### Comparison and validation

- `compare_question_presence`
- `compare_mandatory_kobo`
- `compare_question_labels`
- `compare_option_labels_single`
- `validate_relevant`
- `validate_critical_sets`
- `validate_prefix_counts`
- `validate_crop_harvest`

### Issue shaping and report export

- `make_presence_issues`
- `make_mandatory_issues`
- `make_option_issues`
- `export_report`

### Validated questionnaire generation

- `_read_crop_choices`
- `_fetch_admin_choices`
- `_rebuild_choices_sheet`
- `produce_validated_questionnaire`

??? tip "How to use this page"

    When a KoBo report finding is unclear, search this file for the issue type and inspect the function group above that produces it.
