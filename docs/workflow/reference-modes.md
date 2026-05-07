# Reference Modes

Reference mode determines which file is treated as baseline.

| Mode | Baseline | Typical use |
|---|---|---|
| `latest_template` | Newest matching template in `templates_dir` | First validation for a new country/round draft |
| `previous_round` | `previous_round_file` from `working_dir` | Round-to-round consistency and regression checks |

## Decision Guide

1. Use `latest_template` when validating alignment with official template.
2. Use `previous_round` when preserving continuity from a validated past round.

??? example "Example: latest_template"

    Country team prepares a new form and wants to ensure template compliance before deployment.

??? example "Example: previous_round"

    Team validates round N against round N-1 to catch removed mandatory questions, changed logic, or option drift.
