# KoBo Logic (Step by Step)

**Use this page while reading a real KoBo report.**
Read each section in order and open the matching sheet in Excel.

## KoBo Pipeline Context

**Before report sheets are populated, the validator performs these blocks:**

1. **Configuration and reference resolution**: load active run config and pick template/previous-round baseline.
2. **Survey/choices parsing**: normalize field structures and map language-specific labels.
3. **Placeholder and logic integrity checks**: evaluate `relevant`, placeholder syntax, and replacement readiness.
4. **Issue synthesis and export**: write standardized issue rows and workbook sheets.

<div class="img-note"><strong>Image to add:</strong> if useful, add one screenshot of terminal run summary at <code>docs/assets/images/reports/kobo-run-summary.png</code>.</div>

## 1. Summary Sheet

**What it is doing in code**

- Aggregates issue rows by severity and major control groups.
- Shows critical-set status and structure/replacement health indicators.
- Gives immediate deployment decision support.

**How to interpret**

1. **Any `HIGH` issue means deployment is blocked until addressed.**
2. Use Summary to prioritize investigation, not to finalize root cause.
3. Move to detail sheets for exact question/field evidence.

<div class="img-note"><strong>Image to add:</strong> replace with your real Summary screenshot at <code>docs/assets/images/reports/kobo-summary.png</code>.</div>

![KoBo Summary Placeholder](../assets/images/reports/placeholders/kobo-summary-placeholder.svg){: .sheet-placeholder }

## 2. Critical Sets Sheet

**What it is doing in code**

- Validates required critical question presence.
- Checks mandatory behavior consistency for critical items.
- Applies minimum-count and crop-harvest structural rules.

**Why this matters**

**Critical sets guard indicator integrity.** If this layer fails, downstream analysis can be statistically or conceptually inconsistent.

**Typical issue families**

- <span class="issue-tag issue-high"><code>missing_critical_question</code></span> HIGH: Required critical question is missing from current form.
- <span class="issue-tag issue-high"><code>critical_mandatory_mismatch</code></span> HIGH: Critical question is present but mandatory category differs from rule.
- <span class="issue-tag issue-high"><code>partial_critical_set</code></span> HIGH: Only part of a required critical set is present.
- <span class="issue-tag issue-high"><code>below_minimum_count</code></span> HIGH: Configured critical prefix/group is below minimum-count threshold.
- <span class="issue-tag issue-medium"><code>advisory_question</code></span> MEDIUM: Non-required advisory question is missing (`required: false` in critical sets).
- <span class="issue-tag issue-high"><code>crop_harvest_violation</code></span> HIGH: Crop/harvest structural completeness rule failed.

<div class="img-note"><strong>Image to add:</strong> replace with your real Critical Sets screenshot at <code>docs/assets/images/reports/kobo-critical-sets.png</code>.</div>

![KoBo Critical Sets Placeholder](../assets/images/reports/placeholders/kobo-critical-sets-placeholder.svg){: .sheet-placeholder }

## 3. Questionnaire Structure Sheet

**What it is doing in code**

- Validates `relevant` expression references.
- Detects modified relevant expressions against baseline.
- Flags duplicate question names and duplicate choice names.
- Flags broken or non-standard KoBo variable reference syntax.

**Why this matters**

**Logic and naming integrity prevents silent routing errors.** A single broken reference can hide entire question groups in field collection.

**Typical issue families**

- <span class="issue-tag issue-high"><code>broken_relevant_reference</code></span> HIGH: `relevant` expression references a question/variable not present in the form.
- <span class="issue-tag issue-high"><code>relevant_inexact_reference</code></span> HIGH: Reference tokenization is ambiguous and may resolve incorrectly at runtime.
- <span class="issue-tag issue-medium"><code>relevant_modified</code></span> MEDIUM: `relevant` logic changed from baseline and may alter routing paths.
- <span class="issue-tag issue-high"><code>duplicate_qname</code></span> HIGH: Duplicate question names break deterministic referencing and joins.
- <span class="issue-tag issue-medium"><code>duplicate_choice_name</code></span> MEDIUM: Duplicate choice names in one list can cause option collisions.
- <span class="issue-tag issue-medium"><code>kobo_ref_loose_syntax</code></span> MEDIUM: Reference syntax is loose/non-standard and should be normalized.
- <span class="issue-tag issue-high"><code>kobo_ref_missing_variable</code></span> HIGH: `${var}` reference points to variable not defined in survey.

<div class="img-note"><strong>Image to add:</strong> replace with your real Questionnaire Structure screenshot at <code>docs/assets/images/reports/kobo-structure.png</code>.</div>

![KoBo Questionnaire Structure Placeholder](../assets/images/reports/placeholders/kobo-structure-placeholder.svg){: .sheet-placeholder }

## 4. Replacement Issues Sheet

**What it is doing in code**

- Checks placeholder consistency between template/current/additional information.
- Flags unresolved placeholders.
- Flags text that should be a KoBo variable reference (`${var}`) instead of plain token text.

**Why this matters**

**Replacement errors are deployment quality errors.** Enumerators can receive unresolved technical placeholders or wrong localized values.

**Typical issue families**

- <span class="issue-tag issue-high"><code>placeholder_not_found</code></span> HIGH: Placeholder token exists in survey text but has no usable replacement mapping.
- <span class="issue-tag issue-medium"><code>placeholder_should_use_kobo_ref</code></span> MEDIUM: Text looks like a variable reference and should be explicit KoBo `${var}` syntax.

<div class="img-note"><strong>Image to add:</strong> replace with your real Replacement Issues screenshot at <code>docs/assets/images/reports/kobo-replacement-issues.png</code>.</div>

![KoBo Replacement Issues Placeholder](../assets/images/reports/placeholders/kobo-replacement-placeholder.svg){: .sheet-placeholder }

## 5. Question Changes Sheet

**What it is doing in code**

- Compares question presence and mandatory status.
- Compares labels, type, required flag, filter/appearance/calculation/constraint/hint fields.
- Flags round-parameter dependent differences in structured way.

**Why this matters**

**Question-level changes drive comparability risk** between template and production or between consecutive rounds.

**Typical issue families**

- <code>removed_question</code>: severity is dynamic.
  `HIGH`: removed question is mandatory in reference (`mandatory` / `mandatory-panel`).
  `INFO`: removed question is optional, or downgraded by passing prefix-count set logic.
- <span class="issue-tag issue-info"><code>added_question</code></span> INFO: Question exists in current questionnaire but not in baseline.
- <span class="issue-tag issue-high"><code>mandatory_to_optional</code></span> HIGH: Mandatory baseline question moved to optional counterpart.
- <span class="issue-tag issue-high"><code>mandatory_column_mismatch</code></span> HIGH: Mandatory column/category differs from baseline expectation.
- <span class="issue-tag issue-medium"><code>label_mismatch</code></span> MEDIUM: Question label text changed after normalization.
- <span class="issue-tag issue-medium"><code>type_changed</code></span> MEDIUM: Question type changed relative to baseline.
- <span class="issue-tag issue-medium"><code>required_modified</code></span> MEDIUM: `required` field changed and may affect completeness.
- <span class="issue-tag issue-medium"><code>choice_filter_modified</code></span> MEDIUM: `choice_filter` logic changed and may alter shown options.
- <span class="issue-tag issue-medium"><code>appearance_modified</code></span> MEDIUM: Appearance metadata changed and should be reviewed for enumerator UX differences.
- <span class="issue-tag issue-medium"><code>calculation_modified</code></span> MEDIUM: Calculation expression changed and may alter derived values.
- <span class="issue-tag issue-medium"><code>constraint_modified</code></span> MEDIUM: Constraint rule changed and may alter validation behavior.
- <span class="issue-tag issue-medium"><code>hint_changed</code></span> MEDIUM: Hint text changed and may alter guidance quality.
- <span class="issue-tag issue-medium"><code>choices_list_changed</code></span> MEDIUM: Linked choices list changed for the question.

??? info "Previous-round remap note"

    In `previous_round` mode, some question/option deltas tied to round-parameter replacement are remapped to `round_parameter_change (...)` with `INFO` severity.

<div class="img-note"><strong>Image to add:</strong> replace with your real Question Changes screenshot at <code>docs/assets/images/reports/kobo-question-changes.png</code>.</div>

![KoBo Question Changes Placeholder](../assets/images/reports/placeholders/kobo-question-changes-placeholder.svg){: .sheet-placeholder }

## 6. Choice Changes Sheet

**What it is doing in code**

- Compares option additions/removals for shared questions.
- Compares option label drift for stable options.

**Why this matters**

**Choice drift alters respondent interpretation** even if question stems look unchanged.

**Typical issue families**

- <span class="issue-tag issue-medium"><code>removed_option</code></span> MEDIUM: Baseline option was removed from current choice list.
- <span class="issue-tag issue-medium"><code>added_option</code></span> MEDIUM: New option exists only in current choice list.
- <span class="issue-tag issue-medium"><code>option_label_mismatch</code></span> MEDIUM: Option label text changed while option identity still matches.

??? warning "Important interpretation rule"

    If a question is removed, its missing choices may not appear as separate choice removals.
    Always interpret Question Changes and Choice Changes together.

<div class="img-note"><strong>Image to add:</strong> replace with your real Choice Changes screenshot at <code>docs/assets/images/reports/kobo-choice-changes.png</code>.</div>

![KoBo Choice Changes Placeholder](../assets/images/reports/placeholders/kobo-choice-changes-placeholder.svg){: .sheet-placeholder }

## 7. Validated Questionnaire Output (Previous-Round Workflow)

**What it is doing in code**

- Rebuilds crop choice lists from current `Crop list` sheet.
- Refreshes admin lists from AGOL where available.
- Applies placeholder replacements in workbook text fields.
- Re-checks unresolved placeholders before saving final validated output.

**Why this matters**

**This is the handoff-quality gate** for deployment-ready questionnaire files.

<div class="img-note"><strong>Image to add:</strong> replace with your real validated output summary screenshot at <code>docs/assets/images/reports/kobo-validated-output.png</code>.</div>

![KoBo Validated Output Placeholder](../assets/images/reports/placeholders/kobo-validated-output-placeholder.svg){: .sheet-placeholder }

## Recommended Review Sequence

1. Summary
2. Critical Sets
3. Questionnaire Structure
4. Replacement Issues
5. Question Changes
6. Choice Changes
7. Validated Questionnaire Output checks (if previous-round workflow)

