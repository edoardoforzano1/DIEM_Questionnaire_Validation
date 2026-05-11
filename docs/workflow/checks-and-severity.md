# Severity Reference

## Severity Levels

Every issue row produced by the validator carries one of four severity values. The color coding here matches the Excel report and the issue cards throughout this documentation.

| Severity | Report color | Meaning | Required action |
|---|---|---|---|
| <span class="sev sev-high">HIGH</span> | Red | Blocks round launch  -  must be resolved | Fix before launching the questionnaire |
| <span class="sev sev-medium">MEDIUM</span> | Orange | Significant difference requiring review | Resolve or document rationale |
| <span class="sev sev-info">INFO</span> | Blue | Informational delta  -  tracked for traceability | No action required, but review recommended |
| <span class="sev sev-pass">PASS</span> | Green | Check passed | No action |

**Round launch rule**: if any HIGH-severity issue appears in the report, the questionnaire should not be launched until every HIGH row is resolved or explicitly accepted with documented rationale.

---

## Dynamic Severity Issues

Some issue types do not have a fixed severity  -  the actual severity depends on properties of the affected question or the nature of the detected problem. These are the dynamic-severity issues:

### `skip_pattern_empty` (GeoPoll only)

<div class="logic-box">
<strong>HIGH</strong>  -  Skip Pattern is empty but the Default or Specify column expects routing to a specific question. The respondent flow will not match the intended design.
</div>

---

### `skipPattern_changes` (GeoPoll only)

<div class="logic-box">
<strong>INFO</strong>  -  The effective skip rule differs from the reference (routing target or condition changed). Not a blocking issue, but tracked for round-over-round traceability.
</div>

---

### `removed_question`

<div class="logic-box">
<strong>HIGH</strong> when the removed question is <code>mandatory</code> or <code>mandatory-panel</code> in the reference.<br>
<strong>INFO</strong> when the removed question is optional in the reference, <em>or</em> when it is downgraded by the prefix-count downgrade logic (see below).
</div>

**Prefix-count downgrade logic**: if a removed question belongs to a `min_count_sets` prefix group, and the remaining questions in that group still satisfy the minimum count threshold defined in `critical_sets.yaml`, the removal is downgraded from HIGH to INFO. This avoids noise when a group has more questions than strictly required and one is legitimately removed.

---

### `qtype_changed` / `type_changed`

<div class="logic-box">
<strong>HIGH</strong> when the type transition is incompatible or structurally invalid  -  regardless of whether the question is mandatory. This also includes missing current type while reference has a type, or unknown/unlisted type tokens.<br>
<strong>MEDIUM</strong> when the type change is within compatible variants (e.g. label-only type reclassification).
</div>

Incompatible transitions are those that change the fundamental response structure  -  for example, single-select to multi-select, or numeric to open-text. Compatible transitions (e.g., label-only type variants) are kept at MEDIUM.

---

### `replacement_unresolved_placeholder` (GeoPoll only)

<div class="logic-box">
<strong>HIGH</strong> when the unresolved placeholder is a crop-related token  -  crop placeholders are structural and affect the validated questionnaire content.<br>
<strong>MEDIUM</strong> when the placeholder had a replacement mapping but the token still appeared unresolved in the output (non-crop).
</div>

---

### `missing_critical_question`

<div class="logic-box">
<strong>HIGH</strong> when the critical question has <code>required: true</code> in <code>critical_sets.yaml</code>.<br>
<strong>MEDIUM</strong> (advisory) when it has <code>required: false</code>  -  these appear as <code>advisory_question</code> instead.
</div>

---

## Issue Families by Sheet

A quick lookup: which sheet each issue family appears in and which tool produces it.

| Sheet | Issue families | Tools |
|---|---|---|
| **Critical Sets** | `missing_critical_question` · `critical_mandatory_mismatch` · `advisory_question` · `crop_harvest_violation` | Both |
| **Questionnaire Structure** | `skip_pattern_empty`  -  `default_skip_modified`  -  `skipPattern_invalid_qname`  -  `skipPattern_invalid_qnameCategory`  -  `skipPattern_changes`  -  `skipPattern_range_mismatch`  -  `skipPattern_range_invalid`  -  `duplicate_qname`  -  `qtype_changed` | GeoPoll |
| **Questionnaire Structure** | `broken_relevant_reference`  -  `relevant_inexact_reference`  -  `relevant_modified`  -  `type_changed`  -  `duplicate_qname`  -  `duplicate_choice_name`  -  `kobo_ref_loose_syntax`  -  `kobo_ref_missing_variable` | KoBo |
| **Replacement Issues** | `replacement_additional_info_missing`  -  `replacement_crop_selection_mismatch`  -  `replacement_crop_round_delta`  -  `replacement_missing_key`  -  `replacement_unresolved_placeholder`  -  `replacement_malformed_placeholder` | GeoPoll |
| **Replacement Issues** | `placeholder_not_found`  -  `placeholder_should_use_kobo_ref`  -  `additional_information_replacement_change (...)` | KoBo |
| **Question Changes** | `mandatory_source_missing`  -  `removed_question`  -  `added_question`  -  `mandatory_to_optional`  -  `mandatory_column_mismatch`  -  `question_label_mismatch`  -  `randomize_changed`  -  `conditional_changed`  -  `programming_instructions_changed`  -  `core_questions_only_changed` | GeoPoll |
| **Question Changes** | `removed_question`  -  `added_question`  -  `mandatory_to_optional`  -  `mandatory_column_mismatch`  -  `label_mismatch`  -  `required_modified`  -  `choice_filter_modified`  -  `appearance_modified`  -  `calculation_modified`  -  `constraint_modified`  -  `hint_changed`  -  `choices_list_changed` | KoBo |
| **Option / Choice Changes** | `removed_option`  -  `added_option`  -  `option_label_mismatch`  -  `option_position_renumbered_same_label`  -  `codes_col_removed`  -  `codes_col_added`  -  `codes_col_token_mismatch`  -  `codes_col_renumbered_same_token` | GeoPoll |
| **Choice Changes** | `removed_choice`  -  `added_choice`  -  `choice_label_mismatch` | KoBo |

---

## Deep Dive Pages

- [GeoPoll Logic](geopoll-logic.md)  -  all GeoPoll sheets with full issue cards and screenshots
- [KoBo Logic](kobo-logic.md)  -  all KoBo sheets with full issue cards and screenshots

