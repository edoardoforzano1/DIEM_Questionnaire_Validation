# GeoPoll Report - Navigation Guide

The GeoPoll validator writes a single Excel workbook (e.g. `validation_report_GeoPoll_EN_<date>.xlsx`) containing the sheets below, in this order.

---

## Report Sheet Overview

| # | Sheet name | What it contains | Read when... |
|---|---|---|---|
| 1 | **Summary** | Severity counts per check group | Always - start here |
| 2 | **Critical Sets** | Mandatory question presence and structural completeness | Summary shows non-PASS |
| 3 | **Questionnaire Structure** | Skip routing, Q type, duplicate names | Summary shows non-PASS |
| 4 | **Replacement Issues** | Placeholder token resolution status | Always (previous-round workflow) |
| 5 | **Question Changes** | Label, mandatory, and metadata drift | Summary shows non-PASS |
| 6 | **Option Changes** | Answer-set drift | Summary shows non-PASS |
| 7 | **[validated questionnaire]** | Filled-in output with replacements applied | Previous-round workflow only |

---

## Column Reference

All detail sheets (Critical Sets, Questionnaire Structure, Replacement Issues, Question Changes, Option Changes) share the same column layout. Not every column is populated for every row — blank cells mean "not applicable" for that issue type.

| Column | Content |
|---|---|
| **Issue type** | Machine identifier for the issue (e.g. `removed_question`, `skip_pattern_empty`). Matches the identifiers used in the Severity Reference and Logic pages. |
| **Type** | Mandatory category of the affected question: `mandatory`, `mandatory-panel`, or `optional`. Blank for issues not tied to a specific question. |
| **Set** | Critical set name, for rows produced by Critical Sets checks. Blank otherwise. |
| **Q Name** | Question identifier from the questionnaire. The same Q Name used in skip patterns and data joins. |
| **Field** | Which column or property was checked (e.g. `Skip Pattern`, `Mandatory`, `label`, `count`). |
| **Current value** | The value found in the current questionnaire being validated. |
| **Reference / rule** | The baseline value from the reference questionnaire, or the rule being violated. |
| **Language scope** | `EN` for English-label checks; the target language code for secondary-language checks. |
| **Current value (EN)** | English label of the affected question, for context. |
| **Reference / rule (EN)** | English baseline label. |
| **Current value (Language)** | Target-language label where applicable. |
| **Reference / rule (Language)** | Target-language baseline label. |
| **Action** | Plain-text recommended action for the issue. |
| **Severity** | `HIGH`, `MEDIUM`, `INFO`, or `PASS`. Cells are color-coded: red/orange/blue/green. |
| **Excel row** | Row number in the source questionnaire Excel file. Use this to jump directly to the row in the input file. |

---

## 1 - Summary Sheet

The Summary sheet is the entry point. It contains four status tables, each covering a check group.

![GeoPoll Summary](../assets/images/reports/geopoll-summary.png)

**How to read it:**

- Each table row is a sub-check with a status cell on the right.
- Status cells are `PASS` (green), `INFO` (blue), `MEDIUM` (orange), or `HIGH` (red).
- A `HIGH` in any table means the questionnaire should not be launched until that issue is resolved.
- Use the table to decide which detail sheets to open. If everything is `PASS`, you are done.

**Status tables:**

| Table | Covers | Detail sheet |
|---|---|---|
| CRITICAL SETS STATUS | Critical question presence | Critical Sets |
| QUESTIONNAIRE STRUCTURE CHECKS | Skip routing, Q type, duplicates | Questionnaire Structure |
| REPLACEMENT STATUS | Placeholder resolution | Replacement Issues |
| QUESTION CHANGES (CORE) | Presence, mandatory, label drift | Question Changes |
| QUESTION CHANGES (OPERATIONAL FIELDS) | Operational metadata drift | Question Changes |
| OPTION CHANGES | Answer-set drift | Option Changes |

---

## 2 - Critical Sets Sheet

Checks whether all structurally required questions are present and correctly flagged as mandatory.

![GeoPoll Critical Sets](../assets/images/reports/geopoll-critical-sets.png)

**How to read it:**

- Each row is one missing or misconfigured question, or a failed count check.
- `Field = count` rows indicate a minimum-count threshold failure for a prefix group.
- For `advisory_question` rows (MEDIUM): the question is recommended but not required.
- `below_minimum_count` rows for a set are suppressed when that set already has `missing_critical_question` rows to avoid double-reporting.

**Key columns:** Set, Q Name, Field, Reference / rule, Severity.

---

## 3 - Questionnaire Structure Sheet

Three sub-blocks: skip pattern issues, Q type integrity, and duplicate Q Name checks.

![GeoPoll Questionnaire Structure](../assets/images/reports/geopoll-structure.png)

**How to read it:**

- **Skip pattern issues**: use `Q Name` + `Field` to locate the question and column. `Current value` shows the skip text that triggered the issue; `Reference / rule` shows what was expected.
- **Q type issues** (`qtype_changed`): `Field = Q Type`, `Current value` is the new type, `Reference / rule` is the original type. Check severity — HIGH means incompatible structural change.
- **Duplicate Q Name**: `Q Name` shows the duplicated identifier. `Excel row` gives the row to edit.

**Key columns:** Issue type, Q Name, Field, Current value, Reference / rule, Severity, Excel row.

---

## 4 - Replacement Issues Sheet

Covers placeholder token status — whether `$token$` values were resolved from the Additional Information sheet.

![GeoPoll Replacement Issues](../assets/images/reports/geopoll-replacement-issues.png)

**How to read it:**

- `replacement_additional_info_missing` HIGH at the top means the whole Additional Information sheet failed to load — all other replacement issues may be secondary to this root cause. Fix this first.
- `replacement_missing_key` HIGH: a placeholder in the questionnaire has no matching key in Additional Information. The `Field` column names the unresolved token.
- `replacement_crop_round_delta` INFO: the crop selection changed between rounds. This is informational — no action required unless the crop change was unintentional.
- `replacement_unresolved_placeholder` HIGH/MEDIUM: a token exists in the output file after replacement was applied. HIGH = crop placeholder (structural); MEDIUM = non-crop.

**Key columns:** Issue type, Q Name, Field (token name), Current value, Severity.

---

## 5 - Question Changes Sheet

Two sub-blocks within this sheet:

### QUESTION CHANGES (CORE)

Presence, mandatory status, labels, and Q type (for context — Q type integrity is in Questionnaire Structure).

![GeoPoll Question Changes](../assets/images/reports/geopoll-question-changes.png)

**How to read it:**

- `removed_question` / `added_question`: presence diff. For removals, `Type` column (mandatory/optional) drives severity.
- `question_label_mismatch`: `Current value (EN)` and `Reference / rule (EN)` show the before/after wording with inline word-diff highlighting in the cells — changed words are underlined or colored.
- `mandatory_source_missing` HIGH: the Mandatory column is largely empty in one file. All mandatory-based results below this row should be treated with caution.

**Key columns:** Issue type, Type, Q Name, Field, Current value (EN), Reference / rule (EN), Severity, Excel row.

### QUESTION CHANGES (OPERATIONAL FIELDS)

Randomize, Conditional, Programming Instructions, Core questions only. All at INFO severity.

**How to read it:**

- These rows track operational metadata drift for traceability. No action required unless the change was unintentional.
- Use `Field` to identify which column changed; `Current value` and `Reference / rule` show the before/after content.

---

## 6 - Option Changes Sheet

Answer-set drift at the option level.

![GeoPoll Option Changes](../assets/images/reports/geopoll-option-changes.png)

**How to read it:**

- Rows are grouped by Q Name. All option rows for a question appear together.
- `removed_option` HIGH/MEDIUM and `added_option` INFO: option presence changes. Removals on mandatory questions are HIGH.
- `option_label_mismatch` MEDIUM: the option wording changed. Inline word-diff highlighting shows the exact change.
- `option_position_renumbered_same_label` INFO: same label, different position number — usually harmless reordering.
- `codes_col_*` rows: parallel checks for the Codes column (answer codes used in skip routing).

**Key columns:** Issue type, Q Name, Field (option position), Current value, Reference / rule, Severity.

!!! tip "Cross-referencing Question Changes and Option Changes"
    If a question shows as `removed_question` in Question Changes, its options won't appear as standalone `removed_option` rows in Option Changes. Always check both sheets when assessing the impact of a removed question.

---

## 7 - Validated Questionnaire Output

*Previous-round workflow only.* This sheet (or file) contains the fully substituted questionnaire — crop and admin placeholders replaced with actual country values.

Use it to verify:
- Crop rows are correctly substituted (no remaining `$crop$` tokens).
- Admin area names are present.
- All `$token$` placeholders are resolved before uploading to the field data collection platform.
