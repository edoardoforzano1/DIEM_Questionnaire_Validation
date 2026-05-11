# GeoPoll Validation Logic

**Use this page alongside a real GeoPoll report.** Open the matching Excel sheet for each section.

## Pipeline Context

Before any report row is produced, the validator completes three preparation blocks:

1. **Config and reference resolution** - load active config, resolve `latest_template` or `previous_round` baseline.
2. **Extraction and normalization** - parse survey rows, options, code tokens; normalize text, skip-logic, and placeholders to reduce false positives.
3. **Issue synthesis** - convert raw diffs and rule failures into standardized `issue_type` rows with severity and metadata.

---

## 1 - Summary Sheet

Aggregates all issue rows by severity and by check group. Read this first - it tells you which detail sheets need attention without opening each one.

- If any `HIGH` row is present - the questionnaire should not be launched until resolved.
- Use Summary as a triage map, not for root-cause investigation.
- Open the specific detail sheet for every check group that is not PASS.

The run context block at the top of the sheet records which questionnaire and reference were used, so the report is self-contained for review and audit.

<div class="img-note"><strong>Screenshot to add:</strong> <code>docs/assets/images/reports/geopoll-sum-config-header.png</code> — the run context rows at the top of the Summary sheet</div>

![GeoPoll Summary - Run Context](../assets/images/reports/geopoll-sum-config-header.png){: .sheet-placeholder }

---

## 2 - Critical Sets Sheet

Checks whether all required questions defined in `critical_sets.yaml` are present and have the correct mandatory behavior. A structurally incomplete questionnaire can pass all other checks and still produce broken indicators.

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>missing_critical_question</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A required critical question is absent from the current questionnaire. Min-count deficits are also reported under this type (field = <code>count</code>). For WEALTH checks, <code>o_hh_wealth_*</code> is accepted as an alternative to <code>hh_wealth_*</code>.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Add the missing question back to the questionnaire. The Q Name and expected mandatory value are shown in the Reference column. For count failures, the Reference column shows the minimum required number of questions for that prefix group.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>critical_mandatory_mismatch</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The question exists but its Mandatory column value doesn't match the configured expectation.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Update the Mandatory column for this question to the value shown in the Reference column.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>advisory_question</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A non-required advisory question (<code>required: false</code>) is absent. Not a blocker.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check whether omitting this question affects indicator coverage for this round. No action required if the omission is intentional and documented.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>crop_harvest_violation</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The crop/harvest question set is incomplete - neither the minimal nor the full allowed composition is present.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Ensure the crop/harvest question block is complete. Either the minimal required set or the full allowed set must be present — a partial block is not accepted.
  </div>
</div>

---

## 3 - Questionnaire Structure Sheet

Validates skip routing logic, option-code references, and duplicate Q Names.

### Skip pattern column priority

The validator resolves an **effective skip rule** per question using this column priority:

<div class="logic-box">
<strong>Priority (highest first):</strong><br>
1. <code>Specify skip pattern variable (from blue text)</code> - user-authored override, always authoritative when filled<br>
2. <code>Skip Pattern</code> - the standard routing field<br>
3. <code>Default skip patterns &amp; conditional</code> - fallback rule used when the above two are empty<br><br>
Both the current questionnaire and the reference use the same priority to determine their respective effective rules before comparing them.
</div>

### Skip Pattern Issues

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skip_pattern_empty</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Default column has a routing rule but both Specify and Skip Pattern are empty - the skip routing is not filled in.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Fill in the Skip Pattern column for this question. The Default column shows the intended routing rule — use it as the starting point and confirm it matches the questionnaire design.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>default_skip_modified</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Specify is blank and both Skip Pattern and Default are filled, but they disagree - internal inconsistency within the current questionnaire, not a reference comparison.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Align the Skip Pattern with the Default column rule, or fill in the Specify column to explicitly override both. The two columns should not contradict each other.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skipPattern_invalid_qname</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The effective skip rule routes to a Q Name that doesn't exist in the current questionnaire.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check the Skip Pattern for this question. The target Q Name in the routing instruction doesn't exist — look for a typo, or check if the question was renamed or removed. The Excel row column helps you find the exact cell.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skipPattern_invalid_qnameCategory</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The reference uses a flexible rule ("route to an optional question or non-mandatory alternative") but the Skip Pattern routes to a <strong>mandatory</strong> question.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Change the routing target to the optional counterpart of the question (e.g. if routing to <code>hh_size</code>, route to <code>o_hh_size</code> instead). Flexible rules must point to an optional question.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>skipPattern_changes</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The effective skip rule differs from the reference - the routing target or condition changed.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Compare the Current value and Reference columns to see what changed. Confirm the new routing is intentional and still leads to the correct question. No fix needed if the change is deliberate.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>skipPattern_range_mismatch</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The option code numbers in the Skip Pattern for a given target differ from what the reference specifies.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check whether the answer options for this question were renumbered. If so, update the code range in the Skip Pattern to match the current option numbers.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skipPattern_range_invalid</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The effective skip rule references option codes that don't exist in the current answer options for that question.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Open the Options section for this question and compare the actual option codes against what the Skip Pattern references. Update the code range in the Skip Pattern to match what is actually there.
  </div>
</div>

### Q Type Integrity Issues

<div class="issue-block">
  <div class="issue-block-label"><code>qtype_changed</code> <span class="issue-dynamic-note">- severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Incompatible or structurally invalid type transition (e.g. single-select to multi-select, numeric to open-text). Also includes missing current type when reference has a type, or unknown/unlisted type tokens. Applies regardless of mandatory status.</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Type changed within compatible variants (e.g. label-only type reclassification).</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check the Q Type column for this question. The Current value and Reference columns show the before/after types. If HIGH, the change is structurally incompatible — verify that skip logic, data coding, and any downstream calculations still work correctly. If MEDIUM, confirm the reclassification was intentional.
  </div>
</div>

### Duplicate Q Name Issues

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>duplicate_qname</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Duplicate Q Name values cause reference collisions in skip logic and data joins.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Rename one of the duplicated questions so all Q Names are unique. The Excel row column shows where each duplicate is located in the source file.
  </div>
</div>

---

## 4 - Replacement Issues Sheet

Validates placeholder token coverage. Unresolved placeholders appear as literal `$...$` tokens to the enumerator and invalidate downstream label interpretation.

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>replacement_additional_info_missing</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Additional Information sheet failed to load replacement keys - no placeholder substitution is possible.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check that the Additional Information sheet exists in the questionnaire file, is correctly named, and the file is not open/locked in Excel. Fix this first — all other replacement issues may be side effects of this root cause.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>replacement_crop_selection_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Crop list selection doesn't match the expected shape (e.g. top-10 rule not met).</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Review the Crop list sheet. Check that exactly the required number of crops are selected and the selection flags are set correctly.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>replacement_crop_round_delta</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The selected crop set differs from the reference round. Track for longitudinal comparability.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Confirm the crop change is intentional. If yes, no action needed — this row is for traceability only. If unexpected, review the Crop list sheet and correct the selection.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>replacement_missing_key</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A placeholder token exists in the questionnaire text but no replacement key was found in Additional Information.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    The Field column shows the unresolved token name. Either add a matching key/value row in the Additional Information sheet, or fix the spelling of the token in the questionnaire text so it matches an existing key.
  </div>
</div>

<div class="issue-block">
  <div class="issue-block-label"><code>replacement_unresolved_placeholder</code> <span class="issue-dynamic-note">- severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A <strong>crop placeholder</strong> remains unresolved in the validated text. Crop tokens are structural.</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A <strong>non-crop placeholder</strong> had a mapping but still appears unresolved in the output text.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Find the token shown in the Field column in the Additional Information sheet and make sure its value cell is filled in and not blank. For crop tokens (HIGH), also check that the Crop list sheet is complete and the crop names are populated correctly.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>replacement_malformed_placeholder</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Placeholder token format is malformed - unbalanced markers that cannot be processed.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Fix the placeholder syntax in the questionnaire text. The correct format is <code>$key$</code> — both dollar signs must be present with no extra spaces or characters inside.
  </div>
</div>

---

## 5 - Question Changes Sheet

Compares the current questionnaire against the reference question by question. This is the primary comparability risk layer - even small wording changes can alter indicator interpretation.

### Question Changes (Core)

*Report block: "QUESTION CHANGES (CORE) — Presence, mandatory, Q type, labels"*

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_source_missing</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Mandatory column is largely blank in one of the files - mandatory-based comparisons cannot be trusted. Verify the source column is populated before reviewing other issues.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check that the Mandatory column exists and is filled in the flagged file. Fix this before acting on any other mandatory-related issues in this report — all mandatory comparisons below this row may be unreliable.
  </div>
</div>

<div class="issue-block">
  <div class="issue-block-label"><code>removed_question</code> <span class="issue-dynamic-note">- severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Removed question is <code>mandatory</code> or <code>mandatory-panel</code> in the reference.</span>
  </div>
  <div class="issue-card issue-card-info">
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Removed question is optional, or the group's min-count threshold is still met after removal (prefix-count downgrade).</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Restore the question or document that the removal is approved. For HIGH rows, the question is mandatory and its absence will affect data collection for this round. The Reference column shows the original question label for context.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>added_question</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">New question not in the reference. Track for traceability.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Confirm the addition is intentional. No action needed if it is planned. If unexpected, check whether it was copied from another section of the questionnaire by mistake.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_to_optional</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A mandatory baseline question now appears only as optional - the question may not be collected for all households.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Update the Mandatory column to restore mandatory status, or document clearly why it was intentionally changed to optional for this round.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_column_mismatch</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Mandatory column value differs from the reference.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Correct the Mandatory column value to match what is shown in the Reference column, or document the reason for the deliberate change.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>question_label_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Question wording changed after normalization. Verify interpretive equivalence.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Read the word-diff in the Current value and Reference columns — changed words are highlighted. If the meaning is equivalent (e.g. a minor phrasing refinement), no action needed. If the meaning changed in a way that affects what the respondent is answering, assess comparability with previous rounds.
  </div>
</div>

### Question Changes (Operational Fields)

*Report block: "QUESTION CHANGES (OPERATIONAL FIELDS)"*

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>randomize_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Randomize column changed. Review for execution impact on option ordering.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check whether option order randomization should still apply for this question. Update the Randomize column if the change was unintentional.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>conditional_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Conditional column changed. Track for traceability.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Compare the Current value and Reference columns to see what changed in the conditional routing text. Confirm the new logic is correct and intentional.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>programming_instructions_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Programming Instructions column changed.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Review what changed in the instructions. Confirm the change doesn't affect how the question is programmed or displayed to the enumerator.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>core_questions_only_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Core questions only flag changed, which may alter inclusion logic for core indicator calculations.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Check whether this question should be included in core indicator outputs. Update the flag to match the intended scope for this round.
  </div>
</div>

---

## 6 - Option Changes Sheet

Compares answer sets at the option level. Answer-set drift changes respondent meaning even when the question stem is unchanged.

!!! warning "Read Question Changes and Option Changes together"
    If a question is removed, its options typically won't appear as standalone option removals.

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>removed_option</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A baseline option no longer exists in the current questionnaire.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Add the option back or confirm the removal is intentional. Also check whether any skip patterns reference the removed option's code — if so, those patterns need to be updated too.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>added_option</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A new option exists only in the current questionnaire.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Confirm the new option is intentional. Verify that skip logic and data processing scripts account for the new option code.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>option_label_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Option text changed while the option identity (position or code) still matched.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Read the word-diff in the Current value and Reference columns. If the meaning is equivalent, no action needed. If the wording change alters what the respondent is choosing, assess the comparability impact with previous rounds.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>option_position_renumbered_same_label</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Option ordering changed with no label-text change. Labels are stable.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Labels are the same — this is a reordering only. Verify that any skip patterns referencing this option's code still use the correct updated code number after the reordering.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>codes_col_removed</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Code values removed from the Codes column - breaks downstream data mappings.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Restore the removed code or update all skip patterns and data processing scripts that referenced it. A missing code can break routing silently.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>codes_col_added</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">New code values added. Verify skip-logic and data-coding compatibility.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    Confirm the new code is intentional. Check that skip logic and data processing scripts account for it.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>codes_col_token_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Code tokens differ for the same matched option - the option now maps to a different code.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    The code token changed for this option. Update any skip patterns or processing scripts that reference this code to use the new value.
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>codes_col_renumbered_same_token</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Numeric code positions changed while token semantics stayed stable.</span>
  </div>
  <div class="issue-action">
    <span class="issue-action-label">What to do</span>
    The token meaning is unchanged — just the position number shifted. Verify that skip patterns use the correct updated position number after renumbering.
  </div>
</div>

---

## Recommended Review Sequence

1. **Summary** - triage and identify blocked check groups
2. **Critical Sets** - confirm structural completeness
3. **Questionnaire Structure** - validate skip routing and naming
4. **Replacement Issues** - confirm all placeholders resolved
5. **Question Changes** - assess comparability
6. **Option Changes** - verify answer-set stability
