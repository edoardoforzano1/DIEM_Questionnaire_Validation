# Process Overview

Validation follows the same high-level flow for both tools.

1. Load configuration and optional profile override.
2. Resolve reference file (`latest_template` or `previous_round`).
3. Read questionnaire structure and options.
4. Normalize values needed for fair comparison.
5. Run comparison and rule checks.
6. Build issue tables with severity and metadata.
7. Export Excel report.

## Tool Pipelines

??? note "KoBo pipeline summary"

    - Configuration and reference resolution.
    - Survey and choices parsing.
    - Placeholder normalization and replacement checks.
    - Relevant logic validation.
    - Question, option, and critical checks.
    - Excel report export.
    - Validated questionnaire export in `previous_round` mode.

??? note "GeoPoll pipeline summary"

    - Configuration and reference resolution.
    - Survey sheet parsing and option extraction.
    - Placeholder restoration and replacement mapping.
    - Presence, mandatory, and option comparison.
    - Skip consistency and structural checks.
    - Critical set and crop-harvest checks.
    - Excel report export.
