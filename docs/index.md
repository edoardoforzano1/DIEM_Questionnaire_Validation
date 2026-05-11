# DIEM Questionnaire Validation

Internal documentation for the GeoPoll and KoBo questionnaire validation workflows.

## What this system does

Validates a questionnaire file against a reference (official template or previous round) and produces a structured Excel report. Every detected difference is classified by issue type and severity — HIGH blocks round launch, MEDIUM needs review, INFO is tracked for traceability.

## How to get started

1. Read `README.md` for environment setup and the launcher commands.
2. Edit `configuration/validation_config.yaml` to point to your questionnaire file.
3. Run `validate` from the repository root.
4. Open the report in `batch_output/<run_name>/`.

For documentation: run `.\documentation` from the repo root to open this site at `http://127.0.0.1:8000/`.

## Documentation map

| Section | What it covers |
|---|---|
| [Getting Started](getting-started.md) | Environment setup, dependency install, first run |
| [Process Overview](workflow/process-overview.md) | Full pipeline diagram — inputs, steps, outputs |
| [Reference Modes](workflow/reference-modes.md) | When to use `latest_template` vs `previous_round` |
| [Severity Reference](workflow/checks-and-severity.md) | Severity levels, dynamic severity logic, issue index by sheet |
| [GeoPoll Logic](workflow/geopoll-logic.md) | All GeoPoll sheets with issue cards and report screenshots |
| [KoBo Logic](workflow/kobo-logic.md) | All KoBo sheets with issue cards and report screenshots |
