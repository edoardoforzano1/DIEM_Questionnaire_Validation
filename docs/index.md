# DIEM Questionnaire Validation Documentation

This documentation explains how DIEM questionnaire validation works for KoBo and GeoPoll, including reference modes, logic, report interpretation, and function-level behavior.

## Start Here

- [Getting Started](getting-started.md)
- [Process Overview](workflow/process-overview.md)
- [Reference Modes](workflow/reference-modes.md)
- [Checks and Severity](workflow/checks-and-severity.md)
- [Report Output](report-output/index.md)

=== "KoBo"

    KoBo validation includes skip-logic checks, placeholder normalization, and generation of a validated questionnaire file in `previous_round` mode.

=== "GeoPoll"

    GeoPoll validation includes critical set completeness checks, crop and harvest logic checks, and structured sheet-level report output.

??? info "What this documentation is designed for"

    - Internal team onboarding.
    - Repeatable validation operations across rounds.
    - Troubleshooting report findings quickly.
