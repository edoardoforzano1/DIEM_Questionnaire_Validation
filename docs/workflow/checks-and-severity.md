# Checks and Severity

## Severity Levels

| Severity | Meaning | Action |
|---|---|---|
| `high` | Blocking risk for deployment quality | Must be fixed before release |
| `medium` | Important inconsistency | Review and resolve when justified |
| `info` | Informational difference | Track for traceability |
| `pass` | Rule passed | No action needed |

## Common Cross-Tool Checks

- Non-optional question removed.
- Mandatory category changed.
- Option label mismatch.
- Option added or removed.

## KoBo-Focused Checks

- Broken `${variable}` references in `relevant`.
- Relevant expression changes.
- Placeholder replacement integrity.
- Choice list refresh checks for crop/admin lists in validated outputs.

## GeoPoll-Focused Checks

- Prefix-count thresholds for critical sections.
- Crop/harvest set completeness rules.
- Skip-pattern consistency and reference integrity.
- Codes and options consistency against reference.
