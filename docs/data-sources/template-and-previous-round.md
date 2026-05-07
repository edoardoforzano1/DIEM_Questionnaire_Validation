# Template and Previous Round

## Template Baseline

In `latest_template` mode, the validator auto-selects the newest matching template from `templates_dir`.

## Previous Round Baseline

In `previous_round` mode, the validator uses `previous_round_file` resolved under `working_dir`.

## Why Both Matter

- Template protects standard structure consistency.
- Previous round protects longitudinal consistency.

Using both strategically across the workflow reduces false positives and preserves comparability over time.
