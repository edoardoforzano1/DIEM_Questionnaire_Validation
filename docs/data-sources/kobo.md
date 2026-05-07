# KoBo Inputs

## Minimum Required Inputs

- Questionnaire XLSX with at least `survey` and `choices` sheets.
- Config with correct `language`, `iso3`, and `reference_mode`.

## Important KoBo Columns

### survey

- `type`
- `name`
- `required`
- `relevant`
- language label columns (`label::...`)

### choices

- `list_name`
- `name`
- language label columns

## Optional but Operationally Important

- `Crop list` sheet for crop options.
- `Additional information` replacements for placeholder resolution.
