# Checks and Severity

## Severity Levels

| Severity | Meaning | Action |
|---|---|---|
| `high` | Deployment-blocking quality risk | Fix before release |
| `medium` | Significant difference needing review | Resolve or document rationale |
| `info` | Informational delta | Track for traceability |
| `pass` | Rule passed | No action |

## Cross-Tool Core Checks

- Question added/removed.
- Mandatory category mismatch.
- Label/metadata drift.
- Option/choice drift.

## GeoPoll-Focused Families

- Critical sets and minimum-count thresholds.
- Crop-harvest structure completeness.
- Skip-pattern consistency and option-code integrity.
- Q-type integrity and duplicate question names.
- Placeholder replacement diagnostics.

## KoBo-Focused Families

- Relevant logic reference integrity.
- KoBo variable syntax and missing reference checks.
- Duplicate question or choice-name checks.
- Placeholder/template/additional-info consistency.
- Validated-questionnaire replacement status checks.

??? warning "Interpretation reminder"

    Option/choice-level differences should be interpreted together with question-level differences.
    If a question is removed, you may not see every downstream option removal as separate rows.

## Deep Dive Pages

- [GeoPoll Logic](geopoll-logic.md)
- [KoBo Logic](kobo-logic.md)
