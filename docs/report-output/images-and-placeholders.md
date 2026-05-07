# Images and Placeholders

All report screenshots are loaded from repository paths under `docs/assets/images/reports/`.

## Folder Structure

- `docs/assets/images/reports/placeholders/`:
  - Current placeholder images used by workflow pages.
- `docs/assets/images/reports/`:
  - Your real screenshots (recommended destination).

## How to Replace Placeholders

1. Open the relevant workflow page and note the target screenshot name shown in the blue note.
2. Export or capture the screenshot from your report.
3. Save it into `docs/assets/images/reports/` with the suggested filename.
4. Replace the placeholder link in the page with the real image path.

Example replacement:

```md
![GeoPoll Summary](../assets/images/reports/geopoll-summary.png)
```

## Current Placeholder Files

- `geopoll-summary-placeholder.svg`
- `geopoll-critical-sets-placeholder.svg`
- `geopoll-structure-placeholder.svg`
- `geopoll-replacement-placeholder.svg`
- `geopoll-question-changes-placeholder.svg`
- `geopoll-option-changes-placeholder.svg`
- `kobo-summary-placeholder.svg`
- `kobo-critical-sets-placeholder.svg`
- `kobo-structure-placeholder.svg`
- `kobo-replacement-placeholder.svg`
- `kobo-question-changes-placeholder.svg`
- `kobo-choice-changes-placeholder.svg`
- `kobo-validated-output-placeholder.svg`

## Upload Methods

1. Local git flow:
   - copy images into folder
   - commit and push
2. GitHub web UI:
   - open target folder
   - `Add file` -> `Upload files`

MkDocs will include everything under `docs/` automatically in local serve and site build.
