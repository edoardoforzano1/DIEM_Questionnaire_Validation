# GeoPoll Logic (Step by Step)

**Use this page while reading a real GeoPoll report.**
Read each section in order and open the matching sheet in Excel.

## GeoPoll Pipeline Context

**Before any report row is produced, the validator does three preparation blocks:**

1. **Configuration and reference resolution**: load active config, resolve `latest_template` or `previous_round` baseline.
2. **Extraction and normalization**: parse survey/questions/options/codes and normalize text patterns to reduce false positives.
3. **Issue synthesis**: convert raw diffs into standardized `issue_type` rows with severity and row metadata.

<div class="img-note"><strong>Image to add:</strong> if useful, add one screenshot of terminal run summary at <code>docs/assets/images/reports/geopoll-run-summary.png</code>.</div>

## 1. Summary Sheet

**What it is doing in code**

- Aggregates all issue rows by severity and by major check groups.
- Produces fast pass/fail/warn signals for deployment triage.
- Highlights whether blockers exist before analysts inspect detailed sheets.

**How to interpret**

1. **If any `HIGH` issue is present, treat deployment as blocked.**
2. Use Summary as a triage map, not as root-cause detail.
3. Move to the linked detailed sheet for every failing line.

<div class="img-note"><strong>Image to add:</strong> replace with your real Summary screenshot at <code>docs/assets/images/reports/geopoll-summary.png</code>.</div>

![GeoPoll Summary](../assets/images/reports/geopoll-summary.png){: .sheet-placeholder }

## 2. Critical Sets Sheet

**What it is doing in code**

- Checks whether all expected critical questions exist.
- Checks mandatory-category consistency for critical questions.
- Applies count thresholds for configured prefixes/groups.
- Applies crop-harvest completeness logic.

**Why this matters**

**This sheet protects structural comparability** across rounds/countries. A structurally incomplete questionnaire can pass superficial checks and still break core indicators.

**Typical issue families**

- <span class="issue-tag issue-high"><code>missing_critical_question</code></span> HIGH: A required critical question is missing from the current questionnaire.
- <span class="issue-tag issue-high"><code>critical_mandatory_mismatch</code></span> HIGH: A critical question exists, but its mandatory behavior no longer matches configured expectation.
- <span class="issue-tag issue-high"><code>partial_critical_set</code></span> HIGH: Part of a required critical set is present, but the full required set is incomplete.
- <span class="issue-tag issue-high"><code>below_minimum_count</code></span> HIGH: A configured prefix/group contains fewer questions than the minimum count rule.
- <span class="issue-tag issue-medium"><code>advisory_question</code></span> MEDIUM: A non-required advisory question is missing (`required: false` in critical sets).
- <span class="issue-tag issue-high"><code>crop_harvest_violation</code></span> HIGH: Crop/harvest structure is incomplete or inconsistent with allowed composition rules.

<div class="img-note"><strong>Image to add:</strong> replace with your real Critical Sets screenshot at <code>docs/assets/images/reports/geopoll-critical-sets.png</code>.</div>

![GeoPoll Critical Sets Placeholder](../assets/images/reports/placeholders/geopoll-critical-sets-placeholder.svg){: .sheet-placeholder }

## 3. Questionnaire Structure Sheet

**What it is doing in code**

- Validates skip-pattern consistency between current and baseline forms.
- Detects skip references pointing to missing/invalid option codes.
- Detects duplicate question names and unsafe q-type transitions.

**Why this matters**

**Structure errors often create silent data corruption**: routing may skip the wrong households or record data under incompatible question semantics.

**Typical issue families**

- <span class="issue-tag issue-high"><code>skip_consistency_error</code></span> HIGH: Skip logic changed in a way that is not semantically equivalent to baseline.
- <span class="issue-tag issue-high"><code>skip_range_mismatch</code></span> HIGH: A numeric/code range condition in skip logic no longer matches baseline behavior.
- <span class="issue-tag issue-medium"><code>default_skip_modified</code></span> MEDIUM: Default skip statement changed and may alter routing for unanswered or edge cases.
- <span class="issue-tag issue-high"><code>skip_pattern_invalid_option_code</code></span> HIGH: Skip condition references option codes not valid in current option set.
- <span class="issue-tag issue-info"><code>potential_skip_pattern_option_drift</code></span> INFO: Skip expression still parses, but option drift indicates potential routing instability.
- <span class="issue-tag issue-high"><code>duplicate_qname</code></span> HIGH: Duplicate `Q Name` creates reference collisions for skips and downstream mappings.
- <code>qtype_changed</code>: severity is dynamic.
  `HIGH`: mandatory baseline question changed across incompatible type modes.
  `MEDIUM`: non-mandatory question type changed.

<div class="img-note"><strong>Image to add:</strong> replace with your real Questionnaire Structure screenshot at <code>docs/assets/images/reports/geopoll-structure.png</code>.</div>

![GeoPoll Questionnaire Structure Placeholder](../assets/images/reports/placeholders/geopoll-structure-placeholder.svg){: .sheet-placeholder }

## 4. Replacement Issues Sheet

**What it is doing in code**

- Validates placeholder token replacement coverage.
- Checks Additional Information replacement readiness.
- Detects unresolved tokens that would leak template placeholders to final form.

**Why this matters**

**Replacement issues are quality and trust issues**: unresolved placeholders reduce enumerator clarity and can invalidate downstream interpretation.

**Typical issue families**

- <span class="issue-tag issue-high"><code>replacement_additional_info_missing</code></span> HIGH: Additional Information did not load usable replacement keys for required placeholders.
- <span class="issue-tag issue-medium"><code>replacement_crop_selection_mismatch</code></span> MEDIUM: Crop list selection does not match expected replacement shape (for example expected top-10 selection rule).
- <span class="issue-tag issue-info"><code>replacement_crop_round_delta</code></span> INFO: Selected crop set differs from reference round and may affect comparability.
- <span class="issue-tag issue-high"><code>replacement_missing_key</code></span> HIGH: Placeholder token exists in questionnaire text but no replacement key/value was found.
- <code>replacement_unresolved_placeholder</code>: severity is dynamic.
  `HIGH`: unresolved crop placeholder remains in validated text.
  `MEDIUM`: non-crop placeholder had a mapping but still remained unresolved.
- <span class="issue-tag issue-medium"><code>replacement_malformed_placeholder</code></span> MEDIUM: Placeholder token format is malformed (unbalanced or invalid marker pattern).

<div class="img-note"><strong>Image to add:</strong> replace with your real Replacement Issues screenshot at <code>docs/assets/images/reports/geopoll-replacement-issues.png</code>.</div>

![GeoPoll Replacement Issues Placeholder](../assets/images/reports/placeholders/geopoll-replacement-placeholder.svg){: .sheet-placeholder }

## 5. Question Changes Sheet

**What it is doing in code**

- Compares question presence and mandatory behavior.
- Detects label and metadata column changes.
- Detects operational column changes (`Randomize`, `Conditional`, etc.) relevant to execution semantics.

**Why this matters**

**Question-level drift is the main comparability risk** in longitudinal analysis. Even small wording or behavior changes can alter indicator interpretation.

**Typical issue families**

- <code>removed_question</code>: severity is dynamic.
  `HIGH`: removed question is mandatory in reference (`mandatory` / `mandatory-panel` behavior).
  `INFO`: removed question is optional, or it is downgraded under passing prefix-count downgrade logic.
- <span class="issue-tag issue-info"><code>added_question</code></span> INFO: A new question exists in current questionnaire but not in baseline.
- <span class="issue-tag issue-high"><code>mandatory_to_optional</code></span> HIGH: A mandatory baseline question now appears only as optional counterpart (coverage risk).
- <span class="issue-tag issue-high"><code>mandatory_column_mismatch</code></span> HIGH: Mandatory column/category differs from baseline expectation.
- <span class="issue-tag issue-medium"><code>question_label_mismatch</code></span> MEDIUM: Question wording changed after normalization; verify interpretive equivalence.
- <code>qtype_changed</code>: severity is dynamic.
  `HIGH`: mandatory question changed across incompatible type modes.
  `MEDIUM`: non-mandatory question type changed.
- <span class="issue-tag issue-medium"><code>randomize_changed</code></span> MEDIUM: Randomization metadata changed and should be reviewed for execution impact.
- <code>conditional_changed</code>: severity is dynamic.
  `HIGH`: changed on mandatory question.
  `MEDIUM`: changed on non-mandatory question.
- <span class="issue-tag issue-medium"><code>programming_instructions_changed</code></span> MEDIUM: Programmer instruction text changed; usually operational but traceable.
- <span class="issue-tag issue-medium"><code>core_questions_only_changed</code></span> MEDIUM: Core-only behavior changed and may alter inclusion logic.

<div class="img-note"><strong>Image to add:</strong> replace with your real Question Changes screenshot at <code>docs/assets/images/reports/geopoll-question-changes.png</code>.</div>

![GeoPoll Question Changes Placeholder](../assets/images/reports/placeholders/geopoll-question-changes-placeholder.svg){: .sheet-placeholder }

## 6. Option Changes Sheet

**What it is doing in code**

- Compares option-level additions/removals and label shifts.
- Detects code-token and renumbering inconsistencies.
- Helps isolate answer-set drift even when question text seems unchanged.

**Why this matters**

**Option drift changes respondent meaning**. A stable question with unstable options can still break comparability.

**Typical issue families**

- <span class="issue-tag issue-medium"><code>removed_option</code></span> MEDIUM: Baseline option no longer exists in current questionnaire.
- <span class="issue-tag issue-medium"><code>added_option</code></span> MEDIUM: New option exists only in current questionnaire and should be reviewed.
- <span class="issue-tag issue-medium"><code>option_label_mismatch</code></span> MEDIUM: Option text changed while option identity remained matched.
- <span class="issue-tag issue-info"><code>option_position_renumbered_same_label</code></span> INFO: Option ordering changed without a label-text change.
- <span class="issue-tag issue-high"><code>codes_col_removed</code></span> HIGH: Expected code values were removed from `codes` and can break mappings.
- <span class="issue-tag issue-medium"><code>codes_col_added</code></span> MEDIUM: New code values were added; verify skip/data compatibility.
- <span class="issue-tag issue-medium"><code>codes_col_token_mismatch</code></span> MEDIUM: Code tokens differ for comparable option entries.
- <span class="issue-tag issue-info"><code>codes_col_renumbered_same_token</code></span> INFO: Numeric code positions changed while token semantics stayed stable.

??? warning "Important interpretation rule"

    If a question is removed, disappearing options for that question may not be listed as standalone option removals.
    Always interpret Question Changes and Option Changes together.

<div class="img-note"><strong>Image to add:</strong> replace with your real Option Changes screenshot at <code>docs/assets/images/reports/geopoll-option-changes.png</code>.</div>

![GeoPoll Option Changes Placeholder](../assets/images/reports/placeholders/geopoll-option-changes-placeholder.svg){: .sheet-placeholder }

## Recommended Review Sequence

1. Summary
2. Critical Sets
3. Questionnaire Structure
4. Replacement Issues
5. Question Changes
6. Option Changes

