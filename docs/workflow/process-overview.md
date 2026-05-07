# Process Overview

Use this page as the main map of the validation pipeline.

## Read Order

1. Read this page.
2. Read [Reference Modes](reference-modes.md).
3. Read [GeoPoll Logic](geopoll-logic.md) or [KoBo Logic](kobo-logic.md).

## Shared Pipeline

Both tools follow the same macro flow:

1. Load config (`validation_config.yaml`) and optional profile overlay.
2. Resolve baseline file from the selected reference mode.
3. Read questionnaire structures and answer options.
4. Normalize fields to make comparisons fair.
5. Run rule checks and build issue records.
6. Aggregate results by severity and issue type.
7. Export an Excel report with sectioned sheets.

## Normalization Layer

Normalization is critical to avoid false positives.

- Text normalization: trims/standardizes comparison text.
- Logic normalization: canonicalizes skip/relevant expressions where possible.
- Placeholder normalization: resolves template markers and additional info replacements.
- Option normalization: aligns option structures before diffing labels/presence.

??? warning "Why normalization matters"

    Without normalization, harmless formatting differences can appear as fake validation failures.

## Tool-Specific Flow

=== "GeoPoll"

    - Survey reading with language-aware column resolution.
    - Option and code extraction.
    - Skip-pattern consistency and structural checks.
    - Critical sets and crop-harvest rule checks.
    - Report sections: Summary, Critical Sets, Questionnaire Structure, Replacement Issues, Question Changes, Option Changes.

=== "KoBo"

    - `survey` and `choices` parsing.
    - Relevant-logic validation and duplicate checks.
    - Placeholder and additional-information diagnostics.
    - Critical set and structural checks.
    - Report sections: Summary, Critical Sets, Questionnaire Structure, Replacement Issues, Question Changes, Choice Changes.
    - In `previous_round` workflows, produces validated questionnaire output.
