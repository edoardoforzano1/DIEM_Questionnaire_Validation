# Reference Modes

Reference mode decides the baseline questionnaire used for comparison.

| Mode | Baseline file | Typical use |
|---|---|---|
| `latest_template` | Newest matching template in `templates_dir` | Template compliance before first deployment |
| `previous_round` | `previous_round_file` resolved under `working_dir` | Round-to-round continuity/regression control |

## Decision Guide

1. Use `latest_template` when validating against official standard structure.
2. Use `previous_round` when checking whether a new round drifts from the last validated round.

## Practical Effect on Results

- `latest_template` can flag intentional local adaptations as differences if they are not in template.
- `previous_round` is sensitive to round drift, especially in skip logic, labels, and mandatory status.

??? example "Example: `latest_template`"

    Before country rollout, check draft form against the newest official template for that language.

??? example "Example: `previous_round`"

    Before round N launch, compare against validated round N-1 to catch unplanned removals or logic regressions.

## Related Pages

- [GeoPoll Logic](geopoll-logic.md)
- [KoBo Logic](kobo-logic.md)
