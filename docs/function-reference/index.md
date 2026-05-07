# Function Reference Overview

This section provides technical documentation for script-level functions, including signatures, parameters, returns, pipeline stage, and full function source.

## Scope

- Entrypoint and dispatch: `validate.py`
- Full KoBo function catalogue: `scripts/kobo_validator.py`
- Full GeoPoll function catalogue: `scripts/geopoll_validator.py`

## How to Use

1. Open the validator page from the left menu.
2. Use the **Pipeline Function Map** to navigate functions by validation stage.
3. Open a function section to inspect signature, parameters, and stage mapping.
4. Expand **Function source** to view the exact implementation body.
5. Map report behavior back to implementation.

## Regeneration

To regenerate validator function pages after code changes:

```powershell
conda run -n base python scripts/regenerate_function_docs.py
```
