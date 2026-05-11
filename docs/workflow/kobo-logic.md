# KoBo Validation Logic

**Use this page alongside a real KoBo report.** Open the matching Excel sheet for each section below.

## Pipeline Context

Before any report row is produced, the validator completes four preparation blocks:

1. **Config and reference resolution**  -  load active config, resolve `latest_template` or `previous_round` baseline.
2. **Survey/choices parsing**  -  normalize XLSForm field structures and map language-specific labels.
3. **Placeholder and logic integrity checks**  -  evaluate `relevant` expressions, placeholder syntax, and replacement readiness.
4. **Issue synthesis and export**  -  write standardized issue rows and workbook sheets.

---

## 1  -  Summary Sheet

Aggregates all issue rows by severity and by check group. Read this first.

- Any `HIGH` issue means the questionnaire should not be launched until resolved.
- Use Summary to prioritize investigation, not for root-cause detail.
- Move to detail sheets for exact question/field evidence.
- Header context lines identify the exact run:
  `Comparison basis`, `Current questionnaire`, `Checked against`, `Language scope`, and `Template used for placeholder mapping`.

---

## 2  -  Critical Sets Sheet

Checks whether all required questions defined in `critical_sets.yaml` are present and have the correct mandatory behavior. If this layer fails, downstream analysis can be inconsistent across rounds.

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>missing_critical_question</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A required critical question is absent from the current form. Min-count deficits are also reported under this type (field = <code>count</code>). For WEALTH checks, <code>o_hh_wealth_*</code> is accepted as an alternative to <code>hh_wealth_*</code>.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>critical_mandatory_mismatch</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A critical question is present, but its mandatory category no longer matches the configured expectation.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>advisory_question</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A non-required advisory question (<code>required: false</code>) is missing. Not a blocker, but worth reviewing.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>crop_harvest_violation</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The crop/harvest structural completeness rule failed  -  neither the minimal nor the full allowed set is present.</span>
  </div>
</div>

---

## 3  -  Questionnaire Structure Sheet

Validates `relevant` expression references, routing drift, duplicate names, and `${variable}` syntax. A single broken reference can hide entire question groups in the field  -  silent errors.

### How this sheet is split (not duplicate checks)

1. **Skip logic references (relevant)**  
   Checks only the `relevant` column to catch broken routing references and drift vs baseline.
2. **Q type integrity, duplicates and KoBo references**  
   Checks question type integrity, duplicate names, and `${var}` / `$var` syntax across survey text/formula fields (`label`, `hint`, `constraint`, `calculation`), outside the `relevant` drift check.

`#placeholder#` mapping problems are reported in **Replacement Issues**, not in the two structure summary rows above.

### Check A: Skip logic references (relevant)

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>broken_relevant_reference</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A <code>relevant</code> expression references a question or variable not present in the form. The condition will fail silently at runtime.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>relevant_inexact_reference</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The referenced variable name is not present exactly, but a close optional counterpart (for example <code>o_var</code>) exists. This is usually a mis-targeted routing reference.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>relevant_modified</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A <code>relevant</code> expression changed from baseline. Routing paths may differ from the previous round.</span>
  </div>
</div>

### Check B: Q type integrity, duplicates and KoBo references

<div class="issue-block">
  <div class="issue-block-label"><code>type_changed</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Incompatible or structurally invalid type transition (for example single-select to multi-select, or option-bearing to non-option with invalid option shape).</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Type changed within compatible variants after normalization. Review for expected behavior consistency.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>duplicate_qname</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Duplicate question names break deterministic referencing in <code>relevant</code> expressions and in data joins.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>duplicate_choice_name</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Duplicate choice names within one list can cause option collisions when the list is referenced by multiple questions.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-block-label"><code>kobo_ref_loose_syntax</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Reference uses loose syntax like <code>$var</code> where <code>var</code> is an existing question name. Use <code>${var}</code>.</span>
  </div>
  <div class="issue-card issue-card-medium">
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Loose syntax is present but does not match an existing question name. Still normalize to <code>${var}</code>.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>kobo_ref_missing_variable</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A <code>${var}</code> reference points to a variable not defined anywhere in the survey sheet.</span>
  </div>
</div>

---

## 4  -  Replacement Issues Sheet

Checks placeholder consistency between the template, the current questionnaire, and the Additional Information sheet. Unresolved tokens appear as raw `#placeholder#` text to enumerators.

!!! info "Previous-round remap note"
    In `previous_round` mode, replacement-driven deltas are remapped to `additional_information_replacement_change (...)` with INFO severity and reported in this sheet.

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>placeholder_not_found</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A placeholder token exists in survey text but has no usable replacement mapping in the Additional Information sheet.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>placeholder_should_use_kobo_ref</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Text appears to be a variable reference but is written as plain text instead of proper <code>${variable}</code> KoBo syntax.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>additional_information_replacement_change (...)</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Difference is replacement-driven (Additional Information / crop / AGOL context) and tracked here to avoid confusion in Question and Choice Changes.</span>
  </div>
</div>

---

## 5  -  Question Changes Sheet

Compares the current form against the reference question by question  -  presence, mandatory status, labels, and field-level metadata.  
Q type integrity is intentionally tracked in **Questionnaire Structure**.

### Issue types

<div class="issue-block">
  <div class="issue-block-label"><code>removed_question</code> <span class="issue-dynamic-note"> -  severity is dynamic</span></div>
  <div class="issue-card issue-card-high">
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">Removed question is <code>mandatory</code> or <code>mandatory-panel</code> in the reference. Loss of a mandatory question breaks indicator calculation.</span>
  </div>
  <div class="issue-card issue-card-info">
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">Removed question is optional in the reference, <em>or</em> was downgraded because the remaining group still satisfies the min-count threshold (prefix-count downgrade logic).</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-info">
    <span class="issue-card-name"><code>added_question</code></span>
    <span class="sev sev-info">INFO</span>
    <span class="issue-card-body">A question exists in the current form but was not in the reference. Track for traceability.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_to_optional</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">A mandatory baseline question moved to optional counterpart. Coverage risk: the question may not be collected for all eligible households.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-high">
    <span class="issue-card-name"><code>mandatory_column_mismatch</code></span>
    <span class="sev sev-high">HIGH</span>
    <span class="issue-card-body">The mandatory column/category value differs from the baseline expectation  -  the question's enforcement behavior changed.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>label_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Question label text changed after normalization. Verify interpretive equivalence across rounds.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>required_modified</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">The <code>required</code> field changed, which may affect form completeness enforcement.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>choice_filter_modified</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">The <code>choice_filter</code> logic changed, which may alter which answer options are shown to the enumerator.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>appearance_modified</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Appearance metadata changed. Review for enumerator UX differences.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>calculation_modified</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A calculation expression changed, which may alter derived values in the collected data.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>constraint_modified</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A constraint rule changed, which may alter input validation behavior for enumerators.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>hint_changed</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Hint text changed. Review to ensure guidance quality and consistency with previous instructions.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>choices_list_changed</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">The linked choices list name changed for this question. The answer set may differ from the baseline.</span>
  </div>
</div>

---

## 6  -  Choice Changes Sheet

Compares option additions, removals, and label drift for shared questions. Choice drift alters respondent interpretation even if the question stem looks unchanged.

!!! warning "Read Question Changes and Choice Changes together"
    If a question is removed, its choices will typically not appear as standalone choice removals. Always interpret both sheets in combination.

### Issue types

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>removed_choice</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A baseline option was removed from the current choice list. Respondents can no longer select a previously available answer.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>added_choice</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">A new option exists only in the current choice list. Review for compatibility with historical data coding.</span>
  </div>
</div>

<div class="issue-block">
  <div class="issue-card issue-card-medium">
    <span class="issue-card-name"><code>choice_label_mismatch</code></span>
    <span class="sev sev-medium">MEDIUM</span>
    <span class="issue-card-body">Option label text changed while the option identity still matches. Verify interpretive equivalence.</span>
  </div>
</div>

---

## 7  -  Validated Questionnaire Output (Previous-Round Workflow Only)

Produced only when `reference_mode: previous_round` is configured. This is the final ready-to-use questionnaire file produced by the validator.

**What is built:**

- Crop choice lists rebuilt from the current `Crop list` sheet.
- Admin lists refreshed from AGOL where available.
- All placeholder tokens replaced in text fields.
- Final scan for remaining unresolved tokens before saving.

---

## Recommended Review Sequence

1. **Summary**  -  triage severity and identify blocked check groups
2. **Critical Sets**  -  confirm structural completeness
3. **Questionnaire Structure**  -  validate relevant logic and naming
4. **Replacement Issues**  -  confirm all placeholders are resolved
5. **Question Changes**  -  assess comparability risk
6. **Choice Changes**  -  verify answer-set stability
7. **Validated Questionnaire Output**  -  confirm deployment file quality (previous-round workflow only)
