# Entrypoint (`validate.py`)

## Main Responsibility

- Load centralized config.
- Resolve optional config profile overlay.
- Validate `tool` value.
- Dispatch execution to the selected validator script.

## Main Function

- `main()` controls all dispatch behavior.

## Dispatch Map

- `geopoll` -> `scripts/geopoll_validator.py`
- `kobo` -> `scripts/kobo_validator.py`
