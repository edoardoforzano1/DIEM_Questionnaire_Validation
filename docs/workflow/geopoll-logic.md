# GeoPoll Validation Logic

**Use this page alongside a real GeoPoll report.** Open the matching Excel sheet for each section.

## Pipeline Context

Before any report row is produced, the validator completes three preparation blocks:

1. **Config and reference resolution**  -  load active config, resolve `latest_template` or `previous_round` baseline.
2. **Extraction and normalization**  -  parse survey rows, options, code tokens; normalize text, skip-logic, and placeholders to reduce false positives.
3. **Issue synthesis**  -  convert raw diffs and rule failures into standardized `issue_type` rows with severity and metadata.

---

## 1  -  Summary Sheet

Aggregates all issue rows by severity and by check group. Read this first  -  it tells you which detail sheets need attention without opening each one.

- If any `HIGH` row is present  -  the questionnaire should not be launched until resolved.
- Use Summary as a triage map, not for root-cause investigation.
- Open the specific detail sheet for every check group that is not PASS.

![GeoPoll Summary](../assets/images/reports/geopoll-summary.png){: .sheet-placeholder }

---

## 2  -  Critical Sets Sheet

Checks whether all required questions defined in `critical_sets.yaml` are present and have the correct mandatory behavior. A structurally incomplete questionnaire can pass all other checks and still produce broken indicators.

![GeoPoll Critical Sets](../assets/images/reports/geopoll-critical-sets.png){: .sheet-placeholder }

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>missing_critical_question</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A required critical question is absent from the current questionnaire. Min-count deficits are also reported under this type (field = <code>count</code>). For WEALTH checks, <code>o_hh_wealth_*</code> is accepted as an alternative to <code>hh_wealth_*</code>.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>critical_mandatory_mismatch</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The question exists but its Mandatory column value doesn't match the configured expectation.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>advisory_question</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A non-required advisory question (<code>required: false</code>) is absent. Not a blocker.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>crop_harvest_violation</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The crop/harvest question set is incomplete  -  neither the minimal nor the full allowed composition is present.</span>
  </div>
</div>

---

## 3  -  Questionnaire Structure Sheet

Validates skip routing logic, option-code references, and duplicate Q Names.

### Skip pattern column priority

The validator resolves an **effective skip rule** per question using this column priority:

<div class="logic-box">
<strong>Priority (highest first):</strong><br>
1. <code>Specify skip pattern variable (from blue text)</code>  -  user-authored override, always authoritative when filled<br>
2. <code>Skip Pattern</code>  -  the standard routing field<br>
3. <code>Default skip patterns &amp; conditional</code>  -  fallback rule used when the above two are empty<br><br>
Both the current questionnaire and the reference use the same priority to determine their respective effective rules before comparing them.
</div>

![GeoPoll Questionnaire Structure](../assets/images/reports/geopoll-structure.png){: .sheet-placeholder }

### Skip Pattern Issues

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skip_pattern_empty</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Default column has a routing rule but both Specify and Skip Pattern are empty  -  the skip routing is not filled in.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>default_skip_modified</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Specify is blank and both Skip Pattern and Default are filled, but they disagree  -  internal inconsistency within the current questionnaire, not a reference comparison.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skipPattern_invalid_qname</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The effective skip rule routes to a Q Name that doesn't exist in the current questionnaire.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skipPattern_invalid_qnameCategory</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The reference uses a flexible rule ("route to an optional question or non-mandatory alternative") but the Skip Pattern routes to a <strong>mandatory</strong> question.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>skipPattern_changes</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The effective skip rule differs from the reference  -  the routing target or condition changed.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>skipPattern_range_mismatch</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The option code numbers in the Skip Pattern for a given target differ from what the reference specifies.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>skipPattern_range_invalid</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The effective skip rule references option codes that don't exist in the current answer options for that question.</span>
  </div>
</div>

### Q Type Integrity Issues

<div class="issue-block">
  <div class="issue-block-label"><code>qtype_changed</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Incompatible or structurally invalid type transition (e.g. single-select to multi-select, numeric to open-text). Applies regardless of mandatory status.</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Type changed within compatible variants (e.g. label-only type reclassification).</span>
  </div>
</div>

### Duplicate Q Name Issues

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>duplicate_qname</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Duplicate Q Name values cause reference collisions in skip logic and data joins.</span>
  </div>
</div>

---

## 4  -  Replacement Issues Sheet

Validates placeholder token coverage. Unresolved placeholders appear as literal `$...$` tokens to the enumerator and invalidate downstream label interpretation.

![GeoPoll Replacement Issues](../assets/images/reports/geopoll-replacement-issues.png){: .sheet-placeholder }

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>replacement_additional_info_missing</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Additional Information sheet failed to load replacement keys  -  no placeholder substitution is possible.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>replacement_crop_selection_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Crop list selection doesn't match the expected shape (e.g. top-10 rule not met).</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>replacement_crop_round_delta</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The selected crop set differs from the reference round. Track for longitudinal comparability.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>replacement_missing_key</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A placeholder token exists in the questionnaire text but no replacement key was found in Additional Information.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-block-label"><code>replacement_unresolved_placeholder</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A <strong>crop placeholder</strong> remains unresolved in the validated text. Crop tokens are structural.</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A <strong>non-crop placeholder</strong> had a mapping but still appears unresolved in the output text.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>replacement_malformed_placeholder</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Placeholder token format is malformed  -  unbalanced markers that cannot be processed.</span>
  </div>
</div>

---

## 5  -  Question Changes Sheet

Compares the current questionnaire against the reference question by question. This is the primary comparability risk layer  -  even small wording changes can alter indicator interpretation.

![GeoPoll Question Changes](../assets/images/reports/geopoll-question-changes.png){: .sheet-placeholder }

### Question Changes (Core)

*Report block: "QUESTION CHANGES (CORE)  -  Presence, mandatory, Q type, labels"*

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_source_missing</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Mandatory column is largely blank in one of the files  -  mandatory-based comparisons cannot be trusted. Verify the source column is populated before reviewing other issues.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-block-label"><code>removed_question</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Removed question is <code>mandatory</code> or <code>mandatory-panel</code> in the reference.</span>
  </div>
  <div class="issue-card issue-card-info">
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Removed question is optional, or the group's min-count threshold is still met after removal (prefix-count downgrade).</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>added_question</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">New question not in the reference. Track for traceability.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_to_optional</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A mandatory baseline question now appears only as optional  -  the question may not be collected for all households.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_column_mismatch</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The Mandatory column value differs from the reference.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>question_label_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Question wording changed after normalization. Verify interpretive equivalence.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-block-label"><code>qtype_changed</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Incompatible or invalid type transition (e.g. single-select to multi-select, numeric to open-text). Applies regardless of mandatory status.</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Type changed within compatible variants (e.g. label-only type reclassification).</span>
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
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>conditional_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Conditional column changed. Track for traceability.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>programming_instructions_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Programming Instructions column changed.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>core_questions_only_changed</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">The Core questions only flag changed, which may alter inclusion logic for core indicator calculations.</span>
  </div>
</div>

---

## 6  -  Option Changes Sheet

Compares answer sets at the option level. Answer-set drift changes respondent meaning even when the question stem is unchanged.

!!! warning "Read Question Changes and Option Changes together"
    If a question is removed, its options typically won't appear as standalone option removals.

![GeoPoll Option Changes](../assets/images/reports/geopoll-option-changes.png){: .sheet-placeholder }

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>removed_option</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A baseline option no longer exists in the current questionnaire.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>added_option</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A new option exists only in the current questionnaire.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>option_label_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Option text changed while the option identity (position or code) still matched.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>option_position_renumbered_same_label</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Option ordering changed with no label-text change. Labels are stable.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>codes_col_removed</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Code values removed from the Codes column  -  breaks downstream data mappings.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>codes_col_added</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">New code values added. Verify skip-logic and data-coding compatibility.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>codes_col_token_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Code tokens differ for the same matched option  -  the option now maps to a different code.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>codes_col_renumbered_same_token</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Numeric code positions changed while token semantics stayed stable.</span>
  </div>
</div>

---

## Recommended Review Sequence

1. **Summary**  -  triage and identify blocked check groups
2. **Critical Sets**  -  confirm structural completeness
3. **Questionnaire Structure**  -  validate skip routing and naming
4. **Replacement Issues**  -  confirm all placeholders resolved
5. **Question Changes**  -  assess comparability
6. **Option Changes**  -  verify answer-set stability

