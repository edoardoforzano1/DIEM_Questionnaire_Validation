# GeoPoll Validator (`scripts/geopoll_validator.py`)

This page is organized by the validator pipeline stages used in the script.
Use the stage map to navigate quickly, then open each function spec for parameters and full source.

Total functions documented: **147**

## Pipeline Function Map

### 1. Runtime and logger helpers

- [`_NullOutput.write`](#fn-write-17)
- [`_NullOutput.flush`](#fn-flush-18)
- [`_NullOutput.fileno`](#fn-fileno-19)
- [`_banner`](#fn--banner-25)
- [`_info`](#fn--info-37)
- [`_step`](#fn--step-41)
- [`_summary`](#fn--summary-50)

### 2. Step 1 Configuration

- [`_load_effective_config`](#fn--load-effective-config-130)
- [`_reference_scope_label`](#fn--reference-scope-label-195)
- [`_not_in_reference_text`](#fn--not-in-reference-text-202)

### 3. Step 2 Reference file resolution

- [`_normalize_header_name`](#fn--normalize-header-name-233)
- [`_header_tokens`](#fn--header-tokens-238)
- [`_is_language_candidate_header`](#fn--is-language-candidate-header-243)
- [`resolve_language_column`](#fn-resolve-language-column-255)
- [`detect_language_from_filename`](#fn-detect-language-from-filename-308)
- [`choose_target_language`](#fn-choose-target-language-315)
- [`extract_date_from_name`](#fn-extract-date-from-name-355)
- [`find_latest_template`](#fn-find-latest-template-366)
- [`resolve_reference_file`](#fn-resolve-reference-file-386)
- [`load_critical_sets`](#fn-load-critical-sets-397)
- [`prepare_run`](#fn-prepare-run-433)
- [`_write_config_snapshot_geopoll`](#fn--write-config-snapshot-geopoll-471)

### 4. Step 3 Reading and normalising the survey sheet

- [`_resolve_column_by_aliases`](#fn--resolve-column-by-aliases-593)
- [`read_survey_sheet`](#fn-read-survey-sheet-601)
- [`build_questions_df`](#fn-build-questions-df-660)

### 5. Step 4 Exploding answer options

- [`_normalize_q_type`](#fn--normalize-q-type-715)
- [`is_option_bearing_qtype`](#fn-is-option-bearing-qtype-722)
- [`parse_options`](#fn-parse-options-747)
- [`extract_question_stem`](#fn-extract-question-stem-770)
- [`explode_options`](#fn-explode-options-782)
- [`parse_codes_cell`](#fn-parse-codes-cell-832)
- [`explode_codes`](#fn-explode-codes-850)
- [`_normalize_placeholder_token`](#fn--normalize-placeholder-token-929)
- [`_is_crop_placeholder_token`](#fn--is-crop-placeholder-token-938)
- [`_contains_crop_marker_text`](#fn--contains-crop-marker-text-945)
- [`_clean_header`](#fn--clean-header-952)
- [`_find_column`](#fn--find-column-956)
- [`read_generic_sheet`](#fn-read-generic-sheet-965)
- [`read_additional_information`](#fn-read-additional-information-998)
- [`read_crop_list`](#fn-read-crop-list-1002)
- [`has_placeholder`](#fn-has-placeholder-1006)
- [`build_placeholder_restore_map`](#fn-build-placeholder-restore-map-1010)
- [`restore_placeholder_cells`](#fn-restore-placeholder-cells-1034)
- [`_normalize_placeholder_key`](#fn--normalize-placeholder-key-1089)
- [`_placeholder_lookup_aliases`](#fn--placeholder-lookup-aliases-1105)
- [`_build_placeholder_index`](#fn--build-placeholder-index-1132)
- [`_lookup_placeholder_replacement`](#fn--lookup-placeholder-replacement-1142)
- [`_language_code_for_text_column`](#fn--language-code-for-text-column-1151)
- [`_placeholder_token_explicit_lang`](#fn--placeholder-token-explicit-lang-1173)
- [`analyze_additional_info_substitutions`](#fn-analyze-additional-info-substitutions-1182)
- [`build_additional_info_replacements`](#fn-build-additional-info-replacements-1237)
- [`build_additional_info_replacements_by_language`](#fn-build-additional-info-replacements-by-language-1251)
- [`apply_text_replacements`](#fn-apply-text-replacements-1300)
- [`apply_text_replacements._lang_map`](#fn--lang-map-1314)
- [`apply_placeholder_conversions`](#fn-apply-placeholder-conversions-1350)
- [`extract_crop_metadata`](#fn-extract-crop-metadata-1391)
- [`find_crop_placeholder_questions`](#fn-find-crop-placeholder-questions-1416)
- [`_is_selected_crop_value`](#fn--is-selected-crop-value-1431)
- [`_build_sorted_crop_entries`](#fn--build-sorted-crop-entries-1435)
- [`build_crop_option_block`](#fn-build-crop-option-block-1462)
- [`build_crop_code_block`](#fn-build-crop-code-block-1477)
- [`rebuild_crop_questions_for_deployed_form`](#fn-rebuild-crop-questions-for-deployed-form-1492)

### 6. Step 6 Normalisation helpers

- [`normalize_text_expr`](#fn-normalize-text-expr-1710)
- [`normalize_code_token_expr`](#fn-normalize-code-token-expr-1729)
- [`normalize_mandatory_expr`](#fn-normalize-mandatory-expr-1741)

### 7. Step 7 Comparison and validation functions

- [`_normalize_skip_text`](#fn--normalize-skip-text-1776)
- [`_parse_skip_option_codes`](#fn--parse-skip-option-codes-1781)
- [`_extract_referenced_qnames`](#fn--extract-referenced-qnames-1830)
- [`_extract_qname_tokens`](#fn--extract-qname-tokens-1881)
- [`_extract_qname_like`](#fn--extract-qname-like-1886)
- [`_extract_condition_codes`](#fn--extract-condition-codes-1896)
- [`_extract_skip_codes_for_target`](#fn--extract-skip-codes-for-target-1919)
- [`_extract_skip_codes_for_target._codes_from_spec`](#fn--codes-from-spec-1928)
- [`_parse_default_skip_rules`](#fn--parse-default-skip-rules-1969)
- [`_semantic_skip_signature`](#fn--semantic-skip-signature-2042)
- [`_check_skip_consistency`](#fn--check-skip-consistency-2074)
- [`validate_skip_patterns`](#fn-validate-skip-patterns-2191)

### 8. Step 8 Issue unifiers

- [`make_presence_issues`](#fn-make-presence-issues-2368)
- [`make_mandatory_issues`](#fn-make-mandatory-issues-2483)
- [`make_option_issues`](#fn-make-option-issues-2497)
- [`make_option_presence_issues`](#fn-make-option-presence-issues-2515)
- [`build_option_changes_view`](#fn-build-option-changes-view-2536)
- [`build_option_changes_view._scope_view`](#fn--scope-view-2556)

### 9. Step 9 Run the full pipeline

- [`compare_question_presence`](#fn-compare-question-presence-2647)
- [`compare_mandatory`](#fn-compare-mandatory-2671)
- [`_mandatory_cat_expr`](#fn--mandatory-cat-expr-2711)
- [`_normalize_qtype_value`](#fn--normalize-qtype-value-2722)
- [`_qtype_mode`](#fn--qtype-mode-2736)
- [`_qtype_change_severity`](#fn--qtype-change-severity-2749)
- [`compare_qtype_changes`](#fn-compare-qtype-changes-2761)
- [`compare_legacy_text_field_changes`](#fn-compare-legacy-text-field-changes-2827)
- [`compare_question_labels_single`](#fn-compare-question-labels-single-2889)
- [`build_question_changes_view`](#fn-build-question-changes-view-2955)
- [`build_question_changes_view._scope_view`](#fn--scope-view-2997)
- [`compare_option_labels_single`](#fn-compare-option-labels-single-3064)
- [`compare_option_presence_single`](#fn-compare-option-presence-single-3090)
- [`compare_option_code_renumber_single`](#fn-compare-option-code-renumber-single-3127)
- [`compare_codes_presence_single`](#fn-compare-codes-presence-single-3191)
- [`compare_codes_token_mismatch_single`](#fn-compare-codes-token-mismatch-single-3223)
- [`compare_codes_renumber_single`](#fn-compare-codes-renumber-single-3275)
- [`build_codes_changes_view`](#fn-build-codes-changes-view-3334)
- [`validate_critical_sets`](#fn-validate-critical-sets-3409)
- [`validate_prefix_counts`](#fn-validate-prefix-counts-3494)
- [`validate_crop_harvest`](#fn-validate-crop-harvest-3531)
- [`_tick`](#fn--tick-3576)
- [`_add_issue_reason`](#fn--add-issue-reason-3760)

### 10. Step 10 Export to Excel

- [`_header_row`](#fn--header-row-4127)
- [`_section_header`](#fn--section-header-4134)
- [`_data_row`](#fn--data-row-4141)
- [`_autofit`](#fn--autofit-4150)
- [`_action_for_issue_type`](#fn--action-for-issue-type-4195)
- [`_issues_col_map`](#fn--issues-col-map-4200)
- [`_issues_table`](#fn--issues-table-4221)
- [`_tokenize_for_word_diff`](#fn--tokenize-for-word-diff-4257)
- [`_coalesce_segments`](#fn--coalesce-segments-4268)
- [`_build_diff_segments`](#fn--build-diff-segments-4280)
- [`_set_rich_text`](#fn--set-rich-text-4299)
- [`_apply_inline_diff_for_issue`](#fn--apply-inline-diff-for-issue-4315)
- [`_apply_inline_diff_for_issue._match_issue`](#fn--match-issue-4324)
- [`_set_status`](#fn--set-status-4356)
- [`_cat_counts`](#fn--cat-counts-4390)
- [`write_summary_sheet`](#fn-write-summary-sheet-4399)
- [`write_structure_skip_sheet`](#fn-write-structure-skip-sheet-4561)
- [`write_structure_skip_sheet._sorted`](#fn--sorted-4565)
- [`write_replacement_issues_sheet`](#fn-write-replacement-issues-sheet-4596)
- [`write_critical_sets_sheet`](#fn-write-critical-sets-sheet-4622)
- [`write_question_changes_sheet`](#fn-write-question-changes-sheet-4650)
- [`write_option_changes_sheet`](#fn-write-option-changes-sheet-4681)
- [`export_validation_report`](#fn-export-validation-report-4725)
- [`_resolve_survey_sheet`](#fn--resolve-survey-sheet-4739)
- [`_sheet_header_map`](#fn--sheet-header-map-4746)
- [`_count_selected_crops`](#fn--count-selected-crops-4756)
- [`_placeholder_scan_columns`](#fn--placeholder-scan-columns-4770)
- [`_extract_placeholder_tokens`](#fn--extract-placeholder-tokens-4777)
- [`_has_broken_placeholder_token`](#fn--has-broken-placeholder-token-4781)
- [`_count_unresolved_placeholders`](#fn--count-unresolved-placeholders-4789)
- [`_selected_crop_labels`](#fn--selected-crop-labels-4802)
- [`_selected_crop_entries`](#fn--selected-crop-entries-4820)
- [`_join_short`](#fn--join-short-4848)
- [`_build_crop_round_delta_issue_rows`](#fn--build-crop-round-delta-issue-rows-4856)
- [`_build_replacement_issue_rows`](#fn--build-replacement-issue-rows-4908)
- [`_build_replacement_issue_rows._effective_replacements_for_col`](#fn--effective-replacements-for-col-4973)
- [`_fetch_admin_reference`](#fn--fetch-admin-reference-5080)
- [`_write_table_sheet`](#fn--write-table-sheet-5130)
- [`_apply_admin_sheets`](#fn--apply-admin-sheets-5145)
- [`_build_replacement_status_rows`](#fn--build-replacement-status-rows-5188)
- [`write_validated_questionnaire`](#fn-write-validated-questionnaire-5297)

## Full Specifications

### `_NullOutput.write` {#fn-write-17}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:17`

**Signature**

```python
def write(self, *a, **kw):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `self` | positional_or_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `*a` | var_positional | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `**kw` | var_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |

??? note "Function source"

    ```python
    def write(self, *a, **kw): pass
    ```

### `_NullOutput.flush` {#fn-flush-18}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:18`

**Signature**

```python
def flush(self, *a, **kw):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `self` | positional_or_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `*a` | var_positional | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |
| `**kw` | var_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |

??? note "Function source"

    ```python
    def flush(self, *a, **kw): pass
    ```

### `_NullOutput.fileno` {#fn-fileno-19}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:19`

**Signature**

```python
def fileno(self):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `self` | positional_or_keyword | Yes | `-` | `-` | Internal helper parameter used by runtime/logging wrapper code. |

??? note "Function source"

    ```python
    def fileno(self): raise OSError("not a real file")
    ```

### `_banner` {#fn--banner-25}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:25`

**Signature**

```python
def _banner(tool: str, language: str, iso3: str, mode: str) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `tool` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |

??? note "Function source"

    ```python
    def _banner(tool: str, language: str, iso3: str, mode: str) -> None:
        global _T_START
        _T_START = _time.perf_counter()
        _sys.stdout = _NullOutput()
        print("", file=_REAL_STDOUT)
        print("=" * _BANNER_W, file=_REAL_STDOUT)
        print("  DIEM Questionnaire Validation v2", file=_REAL_STDOUT)
        print(f"  Tool: {tool.upper()}  |  Language: {language.upper()}  |  Country: {iso3.upper()}", file=_REAL_STDOUT)
        print(f"  Reference mode: {mode}", file=_REAL_STDOUT)
        print("=" * _BANNER_W, file=_REAL_STDOUT)
    ```

### `_info` {#fn--info-37}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:37`

**Signature**

```python
def _info(label: str, value: str) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |

??? note "Function source"

    ```python
    def _info(label: str, value: str) -> None:
        print(f"  {label:<12} {value}", file=_REAL_STDOUT)
    ```

### `_step` {#fn--step-41}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:41`

**Signature**

```python
def _step(label: str, detail: str='') -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Runtime and logger helpers` stage. |
| `detail` | positional_or_keyword | No | `''` | `str` | Input used by the `Runtime and logger helpers` stage. |

??? note "Function source"

    ```python
    def _step(label: str, detail: str = "") -> None:
        global _STEP_N
        _STEP_N += 1
        tag  = f"[{_STEP_N}/{_STEP_TOTAL}]"
        pad  = "." * max(1, 44 - len(label))
        tail = f"  {detail}" if detail else ""
        print(f"  {tag} {label} {pad}{tail}", file=_REAL_STDOUT, flush=True)
    ```

### `_summary` {#fn--summary-50}

**Pipeline stage:** `Runtime and logger helpers`

**Location:** `scripts/geopoll_validator.py:50`

**Signature**

```python
def _summary(all_issues=None, report_path=None, extra_paths=None) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Runtime and logger helpers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | No | `None` | `-` | Polars DataFrame carrying records for this processing stage. |
| `report_path` | positional_or_keyword | No | `None` | `-` | Filesystem path used for reading inputs or writing outputs. |
| `extra_paths` | positional_or_keyword | No | `None` | `-` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def _summary(all_issues=None, report_path=None, extra_paths=None) -> None:
        _sys.stdout = _REAL_STDOUT
        print()
        print("-" * _BANNER_W)
        print("  VALIDATION SUMMARY")
        print("-" * _BANNER_W)
        try:
            import polars as _pl
            if all_issues is not None and all_issues.height > 0:
                sev = {r["severity"]: r["n"] for r in
                       all_issues.group_by("severity").agg(_pl.len().alias("n")).to_dicts()}
                high   = sev.get("high",   0)
                medium = sev.get("medium", 0)
                info   = sev.get("info",   0)
                print(f"  {'HIGH':<10} {high:>4}   {'Must fix before deployment' if high else 'None'}")
                print(f"  {'MEDIUM':<10} {medium:>4}   {'Review suggested' if medium else 'None'}")
                print(f"  {'INFO':<10} {info:>4}   Informational")
                print(f"  {'PASS':<10} {'yes' if high == 0 and medium == 0 else 'no':>4}")
            else:
                print("  No issues found — questionnaire passed all checks.")
        except Exception as _e:
            print(f"  (summary unavailable: {_e})")
        print()
        if report_path:
            print(f"  Report  : {report_path}")
        if extra_paths:
            for _lbl, _p in extra_paths:
                print(f"  {_lbl:<8}: {_p}")
        print(f"  Time    : {_time.perf_counter() - _T_START:.1f}s")
        print("=" * _BANNER_W)
        print()
    ```

### `_load_effective_config` {#fn--load-effective-config-130}

**Pipeline stage:** `Step 1 Configuration`

**Location:** `scripts/geopoll_validator.py:130`

**Signature**

```python
def _load_effective_config(cfg_path: Path) -> tuple[dict, Path | None, Path]:
```

**Returns:** `tuple[dict, Path | None, Path]`

**What it does:** Implements logic in the `Step 1 Configuration` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def _load_effective_config(cfg_path: Path) -> tuple[dict, Path | None, Path]:
        base_cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
        if not isinstance(base_cfg, dict):
            raise TypeError(f"Config must be a mapping in {cfg_path}")

        profile_name = str(base_cfg.get("config_profile") or "").strip()
        profile_path: Path | None = None
        effective_cfg = dict(base_cfg)

        if profile_name:
            profiles_dir = Path(base_cfg.get("config_profiles_dir") or (Path(base_cfg.get("output_dir") or base_cfg.get("working_dir") or "C:/Temp/questionnaire_validation") / "config_profiles"))
            candidate = Path(profile_name)
            if not candidate.is_absolute():
                candidate = profiles_dir / candidate

            if candidate.suffix.lower() not in {".yaml", ".yml"}:
                if candidate.with_suffix(".yaml").exists():
                    candidate = candidate.with_suffix(".yaml")
                elif candidate.with_suffix(".yml").exists():
                    candidate = candidate.with_suffix(".yml")

            if not candidate.exists():
                raise FileNotFoundError(
                    f"Config profile not found: {candidate}\n"
                    f"Set 'config_profile' to an existing file or leave it empty."
                )

            profile_cfg = yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}
            if not isinstance(profile_cfg, dict):
                raise TypeError(f"Config profile must be a mapping in {candidate}")

            effective_cfg.update(profile_cfg)
            profile_path = candidate.resolve()

        active_cfg_path = profile_path or cfg_path.resolve()
        return effective_cfg, profile_path, active_cfg_path
    ```

### `_reference_scope_label` {#fn--reference-scope-label-195}

**Pipeline stage:** `Step 1 Configuration`

**Location:** `scripts/geopoll_validator.py:195`

**Signature**

```python
def _reference_scope_label() -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 1 Configuration` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _reference_scope_label() -> str:
        mode = str(getattr(globals().get("cfg", None), "reference_mode", "") or "").strip().lower()
        if mode == "previous_round":
            return "previous round"
        return "latest template"
    ```

### `_not_in_reference_text` {#fn--not-in-reference-text-202}

**Pipeline stage:** `Step 1 Configuration`

**Location:** `scripts/geopoll_validator.py:202`

**Signature**

```python
def _not_in_reference_text(suffix: str='') -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 1 Configuration` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `suffix` | positional_or_keyword | No | `''` | `str` | Input used by the `Step 1 Configuration` stage. |

??? note "Function source"

    ```python
    def _not_in_reference_text(suffix: str = "") -> str:
        base = _reference_scope_label()
        if suffix:
            return f"(not in {base} {suffix})"
        return f"(not in {base})"
    ```

### `_normalize_header_name` {#fn--normalize-header-name-233}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:233`

**Signature**

```python
def _normalize_header_name(name: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 2 Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _normalize_header_name(name: str) -> str:
        s = str(name or "").strip().lower()
        return re.sub(r"[^a-z0-9]+", "", s)
    ```

### `_header_tokens` {#fn--header-tokens-238}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:238`

**Signature**

```python
def _header_tokens(name: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 2 Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _header_tokens(name: str) -> list[str]:
        s = str(name or "").strip().lower()
        return [t for t in re.split(r"[^a-z0-9]+", s) if t]
    ```

### `_is_language_candidate_header` {#fn--is-language-candidate-header-243}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:243`

**Signature**

```python
def _is_language_candidate_header(name: str) -> bool:
```

**Returns:** `bool`

**What it does:** Reject obvious non-language columns to avoid false alias matches.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _is_language_candidate_header(name: str) -> bool:
        """Reject obvious non-language columns to avoid false alias matches."""
        n = _normalize_header_name(name)
        blocked = {
            "qname", "suggestedqname", "qtype", "mandatory", "excelrow", "sourcefile",
            "length", "len", "codes", "additionalnotes",
            "defaultskippatternsconditional", "specifyskippatternvariablefrombluetext",
            "specifyskippatternvariable",
        }
        return n not in blocked
    ```

### `resolve_language_column` {#fn-resolve-language-column-255}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:255`

**Signature**

```python
def resolve_language_column(columns: list[str], language: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Resolves the best matching text column for a language, supporting variants

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `columns` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 2 Reference file resolution` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def resolve_language_column(columns: list[str], language: str) -> str | None:
        """
        Resolves the best matching text column for a language, supporting variants
        such as 'fr_French' while remaining deterministic.
        """
        lang = str(language or "EN").upper()
        preferred = LANGUAGE_COLUMN.get(lang, "English")
        if preferred in columns:
            return preferred

        preferred_norm = _normalize_header_name(preferred)
        for c in columns:
            if _normalize_header_name(c) == preferred_norm:
                return c

        aliases = [_normalize_header_name(a) for a in LANGUAGE_ALIASES.get(lang, [])]
        ranked: list[tuple[int, int, str]] = []
        for c in columns:
            if not _is_language_candidate_header(c):
                continue
            c_norm = _normalize_header_name(c)
            c_toks = set(_header_tokens(c))
            score = 0

            if preferred_norm and preferred_norm in c_norm:
                score += 6

            for a in aliases:
                if not a:
                    continue
                if len(a) <= 2:
                    # short language codes (fr/es/ar/pt/en): require token/prefix match,
                    # never generic substring match (prevents 'Codes' -> 'Spanish').
                    c_low = str(c or "").strip().lower()
                    if a in c_toks:
                        score += 5
                    if c_low.startswith(a + "_") or c_low.startswith(a + "-"):
                        score += 4
                else:
                    if a in c_norm:
                        score += 3
                    if a in c_toks:
                        score += 2

            if score > 0:
                ranked.append((score, -len(c), c))

        if not ranked:
            return None
        ranked.sort(reverse=True)
        return ranked[0][2]
    ```

### `detect_language_from_filename` {#fn-detect-language-from-filename-308}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:308`

**Signature**

```python
def detect_language_from_filename(path: Path | str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Returns EN/FR/ES/AR/PT when filename contains a language token like _ar_.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path | str` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def detect_language_from_filename(path: Path | str) -> str | None:
        """Returns EN/FR/ES/AR/PT when filename contains a language token like _ar_."""
        name = Path(path).name.lower()
        m = re.search(r"_(en|fr|es|ar|pt)(?=_|\.|$)", name)
        return m.group(1).upper() if m else None
    ```

### `choose_target_language` {#fn-choose-target-language-315}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:315`

**Signature**

```python
def choose_target_language(questionnaire_path: Path, questions_df: pl.DataFrame, preferred: str='EN') -> tuple[str, str]:
```

**Returns:** `tuple[str, str]`

**What it does:** Chooses the analysis language for text/option comparisons.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `preferred` | positional_or_keyword | No | `'EN'` | `str` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def choose_target_language(questionnaire_path: Path, questions_df: pl.DataFrame, preferred: str = "EN") -> tuple[str, str]:
        """
        Chooses the analysis language for text/option comparisons.
        Priority:
          1) language token in questionnaire filename (if non-EN and present in columns)
          2) config language (if non-EN and present in columns)
          3) best available non-EN column with most non-empty cells
          4) EN fallback
        """
        cols = questions_df.columns

        file_lang = detect_language_from_filename(questionnaire_path)
        if file_lang and file_lang != "EN" and resolve_language_column(cols, file_lang):
            return file_lang, "filename"

        pref = str(preferred or "EN").upper()
        if pref != "EN" and resolve_language_column(cols, pref):
            return pref, "config"

        scored: list[tuple[int, str]] = []
        for lang in ["AR", "FR", "ES", "PT"]:
            col = resolve_language_column(cols, lang)
            if not col:
                continue
            n_non_empty = (
                questions_df
                .select(pl.col(col).cast(pl.Utf8).fill_null("").str.strip_chars().alias("_v"))
                .filter(pl.col("_v") != "")
                .height
            )
            if n_non_empty > 0:
                scored.append((n_non_empty, lang))

        if scored:
            scored.sort(reverse=True)
            return scored[0][1], "auto_non_en"

        return "EN", "fallback_en"
    ```

### `extract_date_from_name` {#fn-extract-date-from-name-355}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:355`

**Signature**

```python
def extract_date_from_name(path: Path) -> int:
```

**Returns:** `int`

**What it does:** Pulls the 8-digit date out of a filename like:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |

??? note "Function source"

    ```python
    def extract_date_from_name(path: Path) -> int:
        """
        Pulls the 8-digit date out of a filename like:
          household_questionnaire_geopoll_EN_template_20250708_ISO3.xlsx
                                                        ^^^^^^^^
        Returns 0 if no date is found, so the file sorts last.
        """
        m = re.search(r"template_(\d{8})", path.name)
        return int(m.group(1)) if m else 0
    ```

### `find_latest_template` {#fn-find-latest-template-366}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:366`

**Signature**

```python
def find_latest_template(template_repo: Path, enumerator: str, language: str) -> Path:
```

**Returns:** `Path`

**What it does:** Scans the template repo folder and returns the most recent template

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `template_repo` | positional_or_keyword | Yes | `-` | `Path` | Input used by the `Step 2 Reference file resolution` stage. |
| `enumerator` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 2 Reference file resolution` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def find_latest_template(template_repo: Path, enumerator: str, language: str) -> Path:
        """
        Scans the template repo folder and returns the most recent template
        matching the given enumerator (geopoll/kobo) and language (EN/FR/etc.).
        Sorts by date in filename first, then by file modification time as fallback.
        """
        matches = [
            p for p in template_repo.glob("*.xlsx")
            if enumerator.lower() in p.name.lower()
            and f"_{language.lower()}_" in p.name.lower()
            and "template" in p.name.lower()
        ]
        if not matches:
            raise FileNotFoundError(
                f"No template found for enumerator='{enumerator}', language='{language}' in:\n  {template_repo}"
            )
        matches.sort(key=lambda p: (extract_date_from_name(p), p.stat().st_mtime), reverse=True)
        return matches[0]
    ```

### `resolve_reference_file` {#fn-resolve-reference-file-386}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:386`

**Signature**

```python
def resolve_reference_file(cfg: ValidationConfig) -> Path:
```

**Returns:** `Path`

**What it does:** Returns the path to the reference file based on reference_mode in the config.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |

??? note "Function source"

    ```python
    def resolve_reference_file(cfg: ValidationConfig) -> Path:
        """Returns the path to the reference file based on reference_mode in the config."""
        if cfg.reference_mode == "latest_template":
            return find_latest_template(cfg.template_repo, cfg.enumerator, cfg.language)
        if cfg.reference_mode == "previous_round":
            if not cfg.previous_round_file:
                raise ValueError("previous_round_file must be set when reference_mode='previous_round'")
            return cfg.working_dir / cfg.previous_round_file
        raise ValueError(f"Unknown reference_mode: '{cfg.reference_mode}'")
    ```

### `load_critical_sets` {#fn-load-critical-sets-397}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:397`

**Signature**

```python
def load_critical_sets(cfg: ValidationConfig) -> dict:
```

**Returns:** `dict`

**What it does:** Loads validation rules from critical_sets.yaml.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |

??? note "Function source"

    ```python
    def load_critical_sets(cfg: ValidationConfig) -> dict:
        """
        Loads validation rules from critical_sets.yaml.
        Search order:
          1. cfg.critical_sets_file (if set)
          2. critical_sets.yaml next to validation_config.yaml
          3. critical_sets.yaml in the parent folder of validation_config.yaml
          4. critical_sets.yaml in the current working directory
          5. critical_sets.yaml in a scripts/ subfolder of the current directory

        Returns a dict with keys: exact_sets, min_count_sets, crop_harvest.
        If the file is not found, structural validation is disabled (empty rules returned).
        """
        _cfg_dir = Path(__file__).parent.parent / "configuration"
        candidates = [
            Path(cfg.critical_sets_file) if cfg.critical_sets_file else None,
            _cfg_dir / "critical_sets.yaml",
            _cfg_dir.parent / "critical_sets.yaml",
            Path.cwd() / "critical_sets.yaml",
            Path.cwd() / "scripts" / "critical_sets.yaml",
        ]
        for path in candidates:
            if path is not None and path.exists():
                with open(path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                print(f"Rules loaded  : {path}")
                return {
                    "exact_sets"    : data.get("exact_sets", {}),
                    "min_count_sets": data.get("min_count_sets", {}),
                    "crop_harvest"  : data.get("crop_harvest", {}),
                }
        print("  critical_sets.yaml not found  structural validation disabled.")
        print(f"   Searched: {[str(p) for p in candidates if p is not None]}")
        return {"exact_sets": {}, "min_count_sets": {}, "crop_harvest": {}}
    ```

### `prepare_run` {#fn-prepare-run-433}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:433`

**Signature**

```python
def prepare_run(cfg: ValidationConfig) -> dict:
```

**Returns:** `dict`

**What it does:** Creates output directories and resolves all file paths.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |

??? note "Function source"

    ```python
    def prepare_run(cfg: ValidationConfig) -> dict:
        """
        Creates output directories and resolves all file paths.
        Returns a dict with the three paths the rest of the notebook needs.
        Prints a summary so you can confirm the right files were picked up.
        """
        cfg.working_dir.mkdir(parents=True, exist_ok=True)
        output_dir = (cfg.output_dir if cfg.output_dir else cfg.working_dir) / cfg.output_subfolder
        output_dir.mkdir(parents=True, exist_ok=True)

        questionnaire_path = cfg.working_dir / cfg.questionnaire_file
        reference_path     = resolve_reference_file(cfg)

        if not questionnaire_path.exists():
            raise FileNotFoundError(f"Questionnaire file not found:\n  {questionnaire_path}")
        if not reference_path.exists():
            raise FileNotFoundError(f"Reference file not found:\n  {reference_path}")

        _vn = _y.get("validation_number")
        _rtag = f"_R{_vn}" if _vn else ""
        _dtag = _time.strftime("%Y%m%d")
        report_file = output_dir / f"report_geopoll_{cfg.language.lower()}_{cfg.iso3.upper()}{_rtag}_{_dtag}.xlsx"
        validated_questionnaire_file = output_dir / f"validated_questionnaire_geopoll_{cfg.language.lower()}_{cfg.iso3.upper()}{_rtag}_{_dtag}.xlsx"

        run = {
            "questionnaire_path" : questionnaire_path,
            "reference_path"     : reference_path,
            "report_file"        : report_file,
            "validated_questionnaire_file": validated_questionnaire_file,
        }

        print("Questionnaire :", questionnaire_path)
        print("Reference     :", reference_path)
        print("Report output :", report_file)
        print("Validated out :", validated_questionnaire_file)
        return run
    ```

### `_write_config_snapshot_geopoll` {#fn--write-config-snapshot-geopoll-471}

**Pipeline stage:** `Step 2 Reference file resolution`

**Location:** `scripts/geopoll_validator.py:471`

**Signature**

```python
def _write_config_snapshot_geopoll(cfg: ValidationConfig, run: dict, cfg_base_path: Path, cfg_active_path: Path, effective_cfg: dict) -> Path:
```

**Returns:** `Path`

**What it does:** Implements logic in the `Step 2 Reference file resolution` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cfg` | positional_or_keyword | Yes | `-` | `ValidationConfig` | Runtime configuration object for this validation run. |
| `run` | positional_or_keyword | Yes | `-` | `dict` | Runtime configuration object for this validation run. |
| `cfg_base_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `cfg_active_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `effective_cfg` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 2 Reference file resolution` stage. |

??? note "Function source"

    ```python
    def _write_config_snapshot_geopoll(
        cfg: ValidationConfig,
        run: dict,
        cfg_base_path: Path,
        cfg_active_path: Path,
        effective_cfg: dict,
    ) -> Path:
        logs_root = cfg.output_dir if cfg.output_dir else run["report_file"].parent.parent
        logs_dir = logs_root / "configuration"
        logs_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_file = logs_dir / f"config_geopoll_{cfg.language}_{cfg.iso3}_{ts}.yaml"

        payload = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "tool": cfg.enumerator,
            "active_config_file": str(cfg_active_path),
            "base_config_file": str(cfg_base_path.resolve()),
            "config_profile": str(effective_cfg.get("config_profile") or ""),
            "resolved_config": {
                "templates_dir": str(cfg.template_repo),
                "working_dir": str(cfg.working_dir),
                "questionnaire_file": cfg.questionnaire_file,
                "reference_mode": cfg.reference_mode,
                "language": cfg.language,
                "iso3": cfg.iso3,
                "output_dir": str(cfg.output_dir) if cfg.output_dir else "",
                "output_subfolder": cfg.output_subfolder,
                "previous_round_file": cfg.previous_round_file or "",
                "critical_sets_file": str(cfg.critical_sets_file) if cfg.critical_sets_file else "",
            },
            "resolved_run_paths": {k: str(v) for k, v in run.items()},
        }

        with out_file.open("w", encoding="utf-8") as f:
            yaml.safe_dump(payload, f, sort_keys=False, allow_unicode=True)
        return out_file
    ```

### `_resolve_column_by_aliases` {#fn--resolve-column-by-aliases-593}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `scripts/geopoll_validator.py:593`

**Signature**

```python
def _resolve_column_by_aliases(columns: list[str], aliases: list[str]) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 3 Reading and normalising the survey sheet` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `columns` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `aliases` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def _resolve_column_by_aliases(columns: list[str], aliases: list[str]) -> str | None:
        alias_norm = {_normalize_header_name(a) for a in aliases}
        for c in columns:
            if _normalize_header_name(c) in alias_norm:
                return c
        return None
    ```

### `read_survey_sheet` {#fn-read-survey-sheet-601}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `scripts/geopoll_validator.py:601`

**Signature**

```python
def read_survey_sheet(path: Path, sheet_name: str='survey', header_row: int=3, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Reads the survey sheet from an xlsx file into a Polars DataFrame.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `sheet_name` | positional_or_keyword | No | `'survey'` | `str` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `header_row` | positional_or_keyword | No | `3` | `int` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 3 Reading and normalising the survey sheet` stage. |

??? note "Function source"

    ```python
    def read_survey_sheet(path: Path, sheet_name: str = "survey", header_row: int = 3, _wb=None) -> pl.DataFrame:
        """
        Reads the survey sheet from an xlsx file into a Polars DataFrame.

        header_row=3 because the GeoPoll template has two title rows above the
        real column headers.

        Two columns are added automatically:
          excel_row    the actual row number in the Excel file (for tracing mismatches)
          source_file  the filename (tells you which file a row came from)

        Pass _wb to reuse an already-opened openpyxl workbook (avoids re-opening
        the same file multiple times).
        """
        owns_wb = _wb is None
        wb = _wb or openpyxl.load_workbook(path, data_only=True, read_only=True)
        try:
            ws = next(
                (wb[n] for n in wb.sheetnames if n.strip().lower() == sheet_name.lower()),
                None
            )
            if ws is None:
                raise KeyError(f"Sheet '{sheet_name}' not found. Available sheets: {wb.sheetnames}")

            row_iter = ws.iter_rows(values_only=True)
            for _ in range(header_row - 1):
                next(row_iter)   # skip the two title rows

            raw_headers = next(row_iter)
            headers = [
                str(h).replace("\n", " ").strip() if h is not None else f"unnamed_{i}"
                for i, h in enumerate(raw_headers, 1)
            ]

            rows      = []
            excel_row = header_row + 1

            for values in row_iter:
                if all(v is None for v in values):
                    excel_row += 1
                    continue
                row_dict = {headers[i]: values[i] for i in range(len(headers))}
                row_dict["excel_row"]   = excel_row
                row_dict["source_file"] = Path(path).name
                rows.append(row_dict)
                excel_row += 1

            df = pl.DataFrame(rows)
        
            if "Q Name" not in df.columns:
                raise KeyError(f"'Q Name' column not found after reading the sheet. Available columns: {df.columns}")

            df = df.filter(pl.col("Q Name").is_not_null())
   
            return df.with_columns(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
        finally:
            if owns_wb:
                wb.close()
    ```

### `build_questions_df` {#fn-build-questions-df-660}

**Pipeline stage:** `Step 3 Reading and normalising the survey sheet`

**Location:** `scripts/geopoll_validator.py:660`

**Signature**

```python
def build_questions_df(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Selects and cleans the core validation columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def build_questions_df(df: pl.DataFrame) -> pl.DataFrame:
        """
        Selects and cleans the core validation columns.
        Warns (does not crash) if an expected column is missing  silent drops
        would make mismatches invisible.
        """
        # Canonicalise language columns first (e.g. fr_French -> French)
        # so downstream logic can rely on stable names.
        mapped: list[tuple[str, str]] = []
        for lang_code, canonical in LANGUAGE_COLUMN.items():
            if canonical in df.columns:
                continue
            matched = resolve_language_column(df.columns, lang_code)
            if matched and matched != canonical:
                df = df.with_columns(pl.col(matched).alias(canonical))
                mapped.append((matched, canonical))
        if mapped:
            print(f"  Language columns mapped: {mapped}")

        # Canonicalise known non-language column variants (especially skip columns).
        mapped_cols: list[tuple[str, str]] = []
        for canonical, aliases in COLUMN_ALIASES.items():
            if canonical in df.columns:
                continue
            matched = _resolve_column_by_aliases(df.columns, aliases)
            if matched and matched != canonical:
                df = df.with_columns(pl.col(matched).alias(canonical))
                mapped_cols.append((matched, canonical))
        if mapped_cols:
            print(f"  Columns mapped: {mapped_cols}")

        missing = [
            c for c in CORE_COLUMNS
            if c not in df.columns and c not in ("excel_row", "source_file")
        ]
        if missing:
            print(f"  Expected columns not found (will be skipped): {missing}")

        available = [c for c in CORE_COLUMNS if c in df.columns]
        out = df.select(available)

        out = out.with_columns(
            cs.exclude("excel_row").cast(pl.Utf8).fill_null("").str.strip_chars()
        )
        return out
    ```

### `_normalize_q_type` {#fn--normalize-q-type-715}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:715`

**Signature**

```python
def _normalize_q_type(value: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _normalize_q_type(value: str) -> str:
        txt = str(value or "").strip().lower()
        txt = re.sub(r"[-_/]+", " ", txt)
        txt = re.sub(r"\s+", " ", txt)
        return txt
    ```

### `is_option_bearing_qtype` {#fn-is-option-bearing-qtype-722}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:722`

**Signature**

```python
def is_option_bearing_qtype(value: str) -> bool:
```

**Returns:** `bool`

**What it does:** Robust Q Type classifier for option-bearing questions.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def is_option_bearing_qtype(value: str) -> bool:
        """
        Robust Q Type classifier for option-bearing questions.
        Handles spacing/punctuation variants (e.g. Open Ended vs Open-Ended).
        """
        t = _normalize_q_type(value)
        if not t:
            return False
        if t == "single choice":
            return True
        if "select all that apply" in t:
            return True
        if "single choice" in t and "open ended" in t:
            return True
        return False
    ```

### `parse_options` {#fn-parse-options-747}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:747`

**Signature**

```python
def parse_options(text: str) -> list[tuple[int, str]]:
```

**Returns:** `list[tuple[int, str]]`

**What it does:** Parses numbered options from a question text cell.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def parse_options(text: str) -> list[tuple[int, str]]:
        """
        Parses numbered options from a question text cell.
        Returns a list of (option_code, option_label) tuples.

        Labels are whitespace-collapsed but otherwise kept raw 
    

        Example:
            input:  "What is your gender?\\n\\n1)Male\\n2)Female\\n3)DON'T want to answer"
            output: [(1, "Male"), (2, "Female"), (3, "DON'T want to answer")]
        """
        if not text or not isinstance(text, str):
            return []
        results = []
        for m in OPTION_PATTERN.finditer(text):
            code  = int(m.group(1))
            label = " ".join(m.group(2).split())   # collapse newlines/extra spaces
            if label:
                results.append((code, label))
        return results
    ```

### `extract_question_stem` {#fn-extract-question-stem-770}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:770`

**Signature**

```python
def extract_question_stem(text: str) -> str:
```

**Returns:** `str`

**What it does:** Returns only the question/instruction part, removing numbered option blocks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def extract_question_stem(text: str) -> str:
        """
        Returns only the question/instruction part, removing numbered option blocks.
        Used for Question Changes so option text is handled only in Option Changes.
        """
        if not text or not isinstance(text, str):
            return ""
        m = OPTION_PATTERN.search(text)
        stem = text[:m.start()] if m else text
        return stem.strip()
    ```

### `explode_options` {#fn-explode-options-782}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:782`

**Signature**

```python
def explode_options(questions_df: pl.DataFrame, text_col: str='English') -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Turns the questions DataFrame (one row per question) into an options

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `text_col` | positional_or_keyword | No | `'English'` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def explode_options(questions_df: pl.DataFrame, text_col: str = "English") -> pl.DataFrame:
        """
        Turns the questions DataFrame (one row per question) into an options
        DataFrame (one row per answer option).

        Output columns:
            Q Name, Q Type, option_code (Int64), option_label (Utf8),
            excel_row, source_file
        """
        EMPTY_SCHEMA = {
            "Q Name"      : pl.Utf8,
            "Q Type"      : pl.Utf8,
            "option_code" : pl.Int64,
            "option_label": pl.Utf8,
            "excel_row"   : pl.Int64,
            "source_file" : pl.Utf8,
        }

        if text_col not in questions_df.columns:
            print(f"  Column '{text_col}' not found  returning empty options frame.")
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        df = (
            questions_df.filter(
                pl.col("Q Type").map_elements(is_option_bearing_qtype, return_dtype=pl.Boolean)
            )
            if "Q Type" in questions_df.columns
            else questions_df
        )

        carry_cols = [c for c in ["Q Name", "Q Type", "excel_row", "source_file"] if c in df.columns]
        rows = []

        for row in df.select(carry_cols + [text_col]).iter_rows(named=True):
            text = row.get(text_col) or ""
            for code, label in parse_options(text):
                out_row = {c: row.get(c) for c in carry_cols}
                out_row["option_code"]  = code
                out_row["option_label"] = label
                rows.append(out_row)

        if not rows:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        return pl.DataFrame(rows).with_columns(
            pl.col("option_code").cast(pl.Int64),
            pl.col("option_label").cast(pl.Utf8),
        )
    ```

### `parse_codes_cell` {#fn-parse-codes-cell-832}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:832`

**Signature**

```python
def parse_codes_cell(text: str) -> list[tuple[int, str]]:
```

**Returns:** `list[tuple[int, str]]`

**What it does:** Parses numbered entries from the survey 'Codes' column, e.g.:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def parse_codes_cell(text: str) -> list[tuple[int, str]]:
        """
        Parses numbered entries from the survey 'Codes' column, e.g.:
          1)shock_none
          2)shock_flood
        Returns (code_num, code_token) rows.
        """
        if not text or not isinstance(text, str):
            return []
        out = []
        for m in OPTION_PATTERN.finditer(text):
            num = int(m.group(1))
            token = " ".join(m.group(2).split())
            if token:
                out.append((num, token))
        return out
    ```

### `explode_codes` {#fn-explode-codes-850}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:850`

**Signature**

```python
def explode_codes(questions_df: pl.DataFrame, codes_col: str='Codes') -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Turns the survey 'Codes' column into one row per numbered code token.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `codes_col` | positional_or_keyword | No | `'Codes'` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def explode_codes(questions_df: pl.DataFrame, codes_col: str = "Codes") -> pl.DataFrame:
        """
        Turns the survey 'Codes' column into one row per numbered code token.
        Output columns: Q Name, code_num, code_token, excel_row, source_file
        """
        EMPTY_SCHEMA = {
            "Q Name": pl.Utf8,
            "code_num": pl.Int64,
            "code_token": pl.Utf8,
            "excel_row": pl.Int64,
            "source_file": pl.Utf8,
        }
        if codes_col not in questions_df.columns:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        carry_cols = [c for c in ["Q Name", "excel_row", "source_file"] if c in questions_df.columns]
        rows = []
        for row in questions_df.select(carry_cols + [codes_col]).iter_rows(named=True):
            for num, tok in parse_codes_cell(str(row.get(codes_col) or "")):
                rd = {c: row.get(c) for c in carry_cols}
                rd["code_num"] = num
                rd["code_token"] = tok
                rows.append(rd)
        if not rows:
            return pl.DataFrame(schema=EMPTY_SCHEMA)
        return pl.DataFrame(rows).with_columns([
            pl.col("code_num").cast(pl.Int64),
            pl.col("code_token").cast(pl.Utf8),
        ])
    ```

### `_normalize_placeholder_token` {#fn--normalize-placeholder-token-929}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:929`

**Signature**

```python
def _normalize_placeholder_token(token: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _normalize_placeholder_token(token: str) -> str:
        s = str(token or "").strip()
        if s.startswith("$") and s.endswith("$") and len(s) >= 2:
            s = s[1:-1]
        s = re.sub(r"\s+", " ", s).strip().upper()
        s = re.sub(r" (EN|FR|ES|AR|PT)$", "", s)
        return s
    ```

### `_is_crop_placeholder_token` {#fn--is-crop-placeholder-token-938}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:938`

**Signature**

```python
def _is_crop_placeholder_token(token: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _is_crop_placeholder_token(token: str) -> bool:
        norm = _normalize_placeholder_token(token)
        if norm.startswith("TEN MOST COMMON CROP"):
            return True
        return norm in {"CROPS SOLD", "CROP CODES", "CROP SOLD CODES"}
    ```

### `_contains_crop_marker_text` {#fn--contains-crop-marker-text-945}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:945`

**Signature**

```python
def _contains_crop_marker_text(text: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _contains_crop_marker_text(text: str) -> bool:
        for tok in re.findall(r"\$[^$\r\n]+\$", str(text or "")):
            if _is_crop_placeholder_token(tok):
                return True
        return False
    ```

### `_clean_header` {#fn--clean-header-952}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:952`

**Signature**

```python
def _clean_header(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _clean_header(value) -> str:
        return str(value or "").replace("\n", " ").strip()
    ```

### `_find_column` {#fn--find-column-956}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:956`

**Signature**

```python
def _find_column(columns: list[str], *candidates: str) -> Optional[str]:
```

**Returns:** `Optional[str]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `columns` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `*candidates` | var_positional | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _find_column(columns: list[str], *candidates: str) -> Optional[str]:
        lookup = {_clean_header(c).lower(): c for c in columns}
        for candidate in candidates:
            match = lookup.get(_clean_header(candidate).lower())
            if match:
                return match
        return None
    ```

### `read_generic_sheet` {#fn-read-generic-sheet-965}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:965`

**Signature**

```python
def read_generic_sheet(path: Path, sheet_name: str, header_row: int, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Reads any workbook sheet into Polars using the provided 1-based header row.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `sheet_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |
| `header_row` | positional_or_keyword | Yes | `-` | `int` | Input used by the `Step 4 Exploding answer options` stage. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def read_generic_sheet(path: Path, sheet_name: str, header_row: int, _wb=None) -> pl.DataFrame:
        """
        Reads any workbook sheet into Polars using the provided 1-based header row.
        Used for auxiliary sheets such as Crop list and Additional information.
        """
        owns_wb = _wb is None
        wb = _wb or openpyxl.load_workbook(path, data_only=True, read_only=True)
        try:
            ws = next((wb[n] for n in wb.sheetnames if n.strip().lower() == sheet_name.lower()), None)
            if ws is None:
                raise KeyError(f"Sheet '{sheet_name}' not found in {path.name}. Available sheets: {wb.sheetnames}")

            row_iter = ws.iter_rows(values_only=True)
            for _ in range(header_row - 1):
                next(row_iter)

            raw_headers = next(row_iter)
            headers = [
                _clean_header(h) if h is not None else f"unnamed_{i}"
                for i, h in enumerate(raw_headers, 1)
            ]

            rows = []
            for values in row_iter:
                if all(v is None for v in values):
                    continue
                rows.append({headers[i]: values[i] for i in range(len(headers))})

            return pl.DataFrame(rows) if rows else pl.DataFrame(schema={h: pl.Utf8 for h in headers})
        finally:
            if owns_wb:
                wb.close()
    ```

### `read_additional_information` {#fn-read-additional-information-998}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:998`

**Signature**

```python
def read_additional_information(path: Path, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def read_additional_information(path: Path, _wb=None) -> pl.DataFrame:
        return read_generic_sheet(path, sheet_name="Additional information", header_row=2, _wb=_wb)
    ```

### `read_crop_list` {#fn-read-crop-list-1002}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1002`

**Signature**

```python
def read_crop_list(path: Path, _wb=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def read_crop_list(path: Path, _wb=None) -> pl.DataFrame:
        return read_generic_sheet(path, sheet_name="Crop list", header_row=3, _wb=_wb)
    ```

### `has_placeholder` {#fn-has-placeholder-1006}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1006`

**Signature**

```python
def has_placeholder(value) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def has_placeholder(value) -> bool:
        return bool(PLACEHOLDER_PATTERN.search(str(value or "")))
    ```

### `build_placeholder_restore_map` {#fn-build-placeholder-restore-map-1010}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1010`

**Signature**

```python
def build_placeholder_restore_map(reference_questions: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> dict[str, dict[str, str]]:
```

**Returns:** `dict[str, dict[str, str]]`

**What it does:** Returns a per-question map of columns whose template/reference cell still

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_placeholder_restore_map(
        reference_questions: pl.DataFrame,
        candidate_columns: Optional[list[str]] = None,
    ) -> dict[str, dict[str, str]]:
        """
        Returns a per-question map of columns whose template/reference cell still
        contains a $...$ placeholder. Those exact reference cells are what we use
        to restore the current questionnaire before comparison.
        """
        columns = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in reference_questions.columns]
        restore_map: dict[str, dict[str, str]] = {}

        for row in reference_questions.select(["Q Name"] + columns).iter_rows(named=True):
            qname = row["Q Name"]
            hits = {
                col: str(row[col] or "")
                for col in columns
                if has_placeholder(row.get(col))
            }
            if hits:
                restore_map[qname] = hits
        return restore_map
    ```

### `restore_placeholder_cells` {#fn-restore-placeholder-cells-1034}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1034`

**Signature**

```python
def restore_placeholder_cells(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Restores current questionnaire cells to the template/reference version,

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def restore_placeholder_cells(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        candidate_columns: Optional[list[str]] = None,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Restores current questionnaire cells to the template/reference version,
        but only for cells where the reference still contains a $...$ placeholder.
        Returns (restored_questions, restore_log).
        """
        restore_map = build_placeholder_restore_map(reference_questions, candidate_columns)
        if not restore_map:
            empty_log = pl.DataFrame(schema={"Q Name": pl.Utf8, "field": pl.Utf8, "restored_value": pl.Utf8})
            return current_questions.clone(), empty_log

        restore_log_rows = []
        for qname, hits in restore_map.items():
            for field, restored_value in hits.items():
                restore_log_rows.append({
                    "Q Name": qname,
                    "field": field,
                    "restored_value": restored_value,
                })

        if not restore_log_rows:
            empty_log = pl.DataFrame(schema={"Q Name": pl.Utf8, "field": pl.Utf8, "restored_value": pl.Utf8})
            return current_questions.clone(), empty_log

        restore_log = pl.DataFrame(restore_log_rows).select(["Q Name", "field", "restored_value"])
        restore_wide = restore_log.pivot(
            values="restored_value",
            index="Q Name",
            columns="field",
            aggregate_function="first",
        )

        joined = current_questions.join(restore_wide, on="Q Name", how="left", suffix="_restore")

        fields = sorted(set(restore_log["field"].to_list()))
        for field in fields:
            restore_col = f"{field}_restore"
            if field in current_questions.columns and restore_col in joined.columns:
                joined = (
                    joined
                    .with_columns(pl.coalesce([pl.col(restore_col), pl.col(field)]).alias(field))
                    .drop(restore_col)
                )

        leftover_restore_cols = [c for c in joined.columns if c.endswith("_restore")]
        if leftover_restore_cols:
            joined = joined.drop(leftover_restore_cols)

        restored = joined.select(current_questions.columns)
        return restored, restore_log
    ```

### `_normalize_placeholder_key` {#fn--normalize-placeholder-key-1089}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1089`

**Signature**

```python
def _normalize_placeholder_key(original_value: str) -> str:
```

**Returns:** `str`

**What it does:** Normalize an Additional information 'Original' key to a placeholder token.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `original_value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _normalize_placeholder_key(original_value: str) -> str:
        """
        Normalize an Additional information 'Original' key to a placeholder token.

        Accepts both strict "$...$" keys and plain labels like "currency".
        Plain labels are canonicalized to "$label$".
        """
        original = str(original_value or "").strip()
        if not original:
            return ""
        if has_placeholder(original):
            m = PLACEHOLDER_PATTERN.search(original)
            return m.group(0).strip() if m else ""
        return f"${original}$"
    ```

### `_placeholder_lookup_aliases` {#fn--placeholder-lookup-aliases-1105}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1105`

**Signature**

```python
def _placeholder_lookup_aliases(token: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Build normalized lookup aliases for placeholder tokens (e.g. $season FR$ -> $season$).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _placeholder_lookup_aliases(token: str) -> list[str]:
        """Build normalized lookup aliases for placeholder tokens (e.g. $season FR$ -> $season$)."""
        raw = str(token or "").strip()
        if not raw:
            return []

        aliases = []
        if raw.startswith("$") and raw.endswith("$") and len(raw) >= 2:
            inner = re.sub(r"\s+", " ", raw[1:-1]).strip()
            if inner:
                aliases.append(f"${inner}$")
                base = re.sub(r"\s+(EN|FR|ES|AR|PT)$", "", inner, flags=re.IGNORECASE).strip()
                if base and base != inner:
                    aliases.append(f"${base}$")
        else:
            aliases.append(raw)

        out = []
        seen = set()
        for a in aliases:
            k = a.lower()
            if k and k not in seen:
                seen.add(k)
                out.append(k)
        return out
    ```

### `_build_placeholder_index` {#fn--build-placeholder-index-1132}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1132`

**Signature**

```python
def _build_placeholder_index(replacements: dict[str, str]) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _build_placeholder_index(replacements: dict[str, str]) -> dict[str, str]:
        idx = {}
        for k, v in (replacements or {}).items():
            if not v:
                continue
            for alias in _placeholder_lookup_aliases(k):
                idx.setdefault(alias, v)
        return idx
    ```

### `_lookup_placeholder_replacement` {#fn--lookup-placeholder-replacement-1142}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1142`

**Signature**

```python
def _lookup_placeholder_replacement(token: str, replacements: dict[str, str], idx: dict[str, str] | None=None) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `idx` | positional_or_keyword | No | `None` | `dict[str, str] | None` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _lookup_placeholder_replacement(token: str, replacements: dict[str, str], idx: dict[str, str] | None = None) -> str | None:
        mapping = idx if idx is not None else _build_placeholder_index(replacements)
        for alias in _placeholder_lookup_aliases(token):
            val = mapping.get(alias)
            if val is not None and str(val) != "":
                return val
        return None
    ```

### `_language_code_for_text_column` {#fn--language-code-for-text-column-1151}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1151`

**Signature**

```python
def _language_code_for_text_column(column_name: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `column_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _language_code_for_text_column(column_name: str) -> str | None:
        c = str(column_name or "")
        c_norm = _normalize_header_name(c)
        for lang in ["EN", "FR", "ES", "AR", "PT"]:
            canonical = LANGUAGE_COLUMN.get(lang, "")
            if canonical and c_norm == _normalize_header_name(canonical):
                return lang
            aliases = LANGUAGE_ALIASES.get(lang, [])
            toks = set(_header_tokens(c))
            for a in aliases:
                a_norm = _normalize_header_name(a)
                if not a_norm:
                    continue
                if len(a_norm) <= 2:
                    c_low = c.lower().strip()
                    if a.lower() in toks or c_low.startswith(a.lower() + "_") or c_low.startswith(a.lower() + "-"):
                        return lang
                elif a_norm in c_norm:
                    return lang
        return None
    ```

### `_placeholder_token_explicit_lang` {#fn--placeholder-token-explicit-lang-1173}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1173`

**Signature**

```python
def _placeholder_token_explicit_lang(token: str) -> str | None:
```

**Returns:** `str | None`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _placeholder_token_explicit_lang(token: str) -> str | None:
        raw = str(token or "").strip()
        if not (raw.startswith("$") and raw.endswith("$") and len(raw) >= 2):
            return None
        inner = re.sub(r"\s+", " ", raw[1:-1]).strip()
        m = re.search(r"\s+(EN|FR|ES|AR|PT)$", inner, flags=re.IGNORECASE)
        return m.group(1).upper() if m else None
    ```

### `analyze_additional_info_substitutions` {#fn-analyze-additional-info-substitutions-1182}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1182`

**Signature**

```python
def analyze_additional_info_substitutions(path: Path, language: str, _wb=None) -> dict:
```

**Returns:** `dict`

**What it does:** Return diagnostics about Additional information substitution readiness.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def analyze_additional_info_substitutions(path: Path, language: str, _wb=None) -> dict:
        """Return diagnostics about Additional information substitution readiness."""
        df = read_additional_information(path, _wb=_wb)
        out = {
            "has_sheet": True,
            "has_required_columns": True,
            "replacement_col": "",
            "original_col": "",
            "rows_with_any_data": 0,
            "rows_with_placeholder_style_original": 0,
            "rows_with_non_placeholder_original": 0,
            "loaded_keys": set(),
            "blank_value_keys": set(),
        }

        if df.height == 0:
            out["has_sheet"] = False
            return out

        replacement_col = _find_column(
            df.columns,
            f"Replacement ({language})",
            "Replacement",
            "Replacement (EN)",
        )
        original_col = _find_column(df.columns, "Original")
        out["replacement_col"] = replacement_col or ""
        out["original_col"] = original_col or ""
        if not replacement_col or not original_col:
            out["has_required_columns"] = False
            return out

        for row in df.iter_rows(named=True):
            original = str(row.get(original_col) or "").strip()
            replacement = str(row.get(replacement_col) or "").strip()
            if not original and not replacement:
                continue

            out["rows_with_any_data"] += 1
            if has_placeholder(original):
                out["rows_with_placeholder_style_original"] += 1
            elif original:
                out["rows_with_non_placeholder_original"] += 1

            key = _normalize_placeholder_key(original)
            if not key:
                continue
            if replacement:
                out["loaded_keys"].add(key)
            else:
                out["blank_value_keys"].add(key)

        return out
    ```

### `build_additional_info_replacements` {#fn-build-additional-info-replacements-1237}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1237`

**Signature**

```python
def build_additional_info_replacements(path: Path, language: str, _wb=None) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Backward-compatible single-language map from Additional information.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_additional_info_replacements(path: Path, language: str, _wb=None) -> dict[str, str]:
        """Backward-compatible single-language map from Additional information."""
        per_lang = build_additional_info_replacements_by_language(path, _wb=_wb)
        lang = str(language or "EN").upper()
        if per_lang.get(lang):
            return per_lang[lang]
        if per_lang.get("EN"):
            return per_lang["EN"]
        for m in per_lang.values():
            if m:
                return m
        return {}
    ```

### `build_additional_info_replacements_by_language` {#fn-build-additional-info-replacements-by-language-1251}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1251`

**Signature**

```python
def build_additional_info_replacements_by_language(path: Path, _wb=None) -> dict[str, dict[str, str]]:
```

**Returns:** `dict[str, dict[str, str]]`

**What it does:** Build per-language substitution maps from Additional information.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `_wb` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_additional_info_replacements_by_language(path: Path, _wb=None) -> dict[str, dict[str, str]]:
        """Build per-language substitution maps from Additional information."""
        df = read_additional_information(path, _wb=_wb)
        original_col = _find_column(df.columns, "Original")
        if not original_col or df.height == 0:
            return {lang: {} for lang in ["EN", "FR", "ES", "AR", "PT"]}

        generic_replacement_col = _find_column(df.columns, "Replacement")
        en_replacement_col = _find_column(df.columns, "Replacement (EN)", "Replacement EN")

        replacement_col_by_lang = {}
        for lang in ["EN", "FR", "ES", "AR", "PT"]:
            replacement_col_by_lang[lang] = _find_column(
                df.columns,
                f"Replacement ({lang})",
                f"Replacement {lang}",
            )

        out = {lang: {} for lang in ["EN", "FR", "ES", "AR", "PT"]}
        season_phase_by_lang = {lang: "" for lang in out.keys()}

        for row in df.iter_rows(named=True):
            key = _normalize_placeholder_key(str(row.get(original_col) or "").strip())
            if not key:
                continue

            for lang in out.keys():
                replacement = ""
                col = replacement_col_by_lang.get(lang)
                if col:
                    replacement = str(row.get(col) or "").strip()
                if not replacement and generic_replacement_col:
                    replacement = str(row.get(generic_replacement_col) or "").strip()
                if not replacement and lang != "EN" and en_replacement_col:
                    replacement = str(row.get(en_replacement_col) or "").strip()

                if replacement:
                    out[lang][key] = replacement
                    if key.lower() in {"$season phase$", "$season phase $"}:
                        season_phase_by_lang[lang] = replacement.lower()

        for lang, mapping in out.items():
            if "$expected or nothing$" in mapping:
                phase = season_phase_by_lang.get(lang, "")
                mapping["$expected or nothing$"] = "expected" if phase in SEASON_PHASE_EXPECTED_VALUES else ""

        return out
    ```

### `apply_text_replacements` {#fn-apply-text-replacements-1300}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1300`

**Signature**

```python
def apply_text_replacements(value, replacements: dict[str, str], replacements_by_language: Optional[dict[str, dict[str, str]]]=None) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements_by_language` | positional_or_keyword | No | `None` | `Optional[dict[str, dict[str, str]]]` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def apply_text_replacements(
        value,
        replacements: dict[str, str],
        replacements_by_language: Optional[dict[str, dict[str, str]]] = None,
    ) -> str:
        text = str(value or "")
        has_lang_maps = any((replacements_by_language or {}).values())
        if not replacements and not has_lang_maps:
            return text

        default_map = replacements or {}
        default_idx = _build_placeholder_index(default_map)
        lang_idx_cache: dict[str, dict[str, str]] = {}

        def _lang_map(lang: str) -> dict[str, str]:
            if not replacements_by_language:
                return {}
            return replacements_by_language.get(lang, {}) or {}

        for token in sorted(set(re.findall(r"\$[^$\r\n]+\$", text)), key=len, reverse=True):
            replacement = None
            token_lang = _placeholder_token_explicit_lang(token)

            # If token explicitly carries a language suffix (e.g. $season FR$),
            # prioritize that language replacement column.
            if token_lang:
                token_lang_map = _lang_map(token_lang)
                if token_lang_map:
                    if token_lang not in lang_idx_cache:
                        lang_idx_cache[token_lang] = _build_placeholder_index(token_lang_map)
                    replacement = _lookup_placeholder_replacement(token, token_lang_map, lang_idx_cache[token_lang])

            # Fallback to the active column/default language map.
            if replacement is None and default_map:
                replacement = _lookup_placeholder_replacement(token, default_map, default_idx)

            # Final fallback: EN map if available (useful when EN is selected and
            # only English replacements are filled).
            if replacement is None:
                en_map = _lang_map("EN")
                if en_map:
                    if "EN" not in lang_idx_cache:
                        lang_idx_cache["EN"] = _build_placeholder_index(en_map)
                    replacement = _lookup_placeholder_replacement(token, en_map, lang_idx_cache["EN"])

            if replacement is not None:
                text = text.replace(token, replacement)
        return text
    ```

### `apply_text_replacements._lang_map` {#fn--lang-map-1314}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1314`

**Signature**

```python
def _lang_map(lang: str) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `lang` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _lang_map(lang: str) -> dict[str, str]:
            if not replacements_by_language:
                return {}
            return replacements_by_language.get(lang, {}) or {}
    ```

### `apply_placeholder_conversions` {#fn-apply-placeholder-conversions-1350}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1350`

**Signature**

```python
def apply_placeholder_conversions(questions_df: pl.DataFrame, replacements: dict[str, str], candidate_columns: Optional[list[str]]=None, replacements_by_language: Optional[dict[str, dict[str, str]]]=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Forward-applies placeholder replacements to text-bearing columns.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 4 Exploding answer options` stage. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |
| `replacements_by_language` | positional_or_keyword | No | `None` | `Optional[dict[str, dict[str, str]]]` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def apply_placeholder_conversions(
        questions_df: pl.DataFrame,
        replacements: dict[str, str],
        candidate_columns: Optional[list[str]] = None,
        replacements_by_language: Optional[dict[str, dict[str, str]]] = None,
    ) -> pl.DataFrame:
        """
        Forward-applies placeholder replacements to text-bearing columns.
        Language columns use language-specific replacement maps when available.
        """
        columns = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in questions_df.columns]
        if not columns:
            return questions_df.clone()

        default_replacements = replacements or {}
        has_lang_maps = any((replacements_by_language or {}).values())
        out = questions_df.clone()

        for col in columns:
            lang = _language_code_for_text_column(col)
            col_replacements = default_replacements
            if replacements_by_language and lang and replacements_by_language.get(lang):
                col_replacements = replacements_by_language[lang]

            if not col_replacements and not has_lang_maps:
                continue

            out = out.with_columns(
                pl.col(col)
                .cast(pl.Utf8)
                .fill_null("")
                .map_elements(
                    lambda v: apply_text_replacements(v, col_replacements, replacements_by_language=replacements_by_language),
                    return_dtype=pl.Utf8,
                )
                .alias(col)
            )

        return out
    ```

### `extract_crop_metadata` {#fn-extract-crop-metadata-1391}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1391`

**Signature**

```python
def extract_crop_metadata(crop_df: pl.DataFrame, language: str) -> dict:
```

**Returns:** `dict`

**What it does:** Pulls the key columns from the Crop list sheet in a language-aware way.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def extract_crop_metadata(crop_df: pl.DataFrame, language: str) -> dict:
        """
        Pulls the key columns from the Crop list sheet in a language-aware way.
        Returned labels include the full crop pool, not only the selected rows.
        """
        label_col = _find_column(crop_df.columns, f"Label ({language})", "Label (EN)")
        dataset_col = _find_column(crop_df.columns, "Dataset code")
        select_col = _find_column(crop_df.columns, "Select top 10 crops", "Select top 10 crops ")

        if not label_col:
            return {"label_col": None, "dataset_col": dataset_col, "select_col": select_col, "labels": []}

        labels = [
            str(v).strip()
            for v in crop_df.get_column(label_col).to_list()
            if str(v or "").strip()
        ]
        return {
            "label_col": label_col,
            "dataset_col": dataset_col,
            "select_col": select_col,
            "labels": labels,
        }
    ```

### `find_crop_placeholder_questions` {#fn-find-crop-placeholder-questions-1416}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1416`

**Signature**

```python
def find_crop_placeholder_questions(reference_questions: pl.DataFrame) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Identifies questions whose reference/template text carries a crop marker.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def find_crop_placeholder_questions(reference_questions: pl.DataFrame) -> list[str]:
        """
        Identifies questions whose reference/template text carries a crop marker.
        Those are the questions that need template-style restoration for comparison
        and deployed-style rebuilding for validated output.
        """
        text_columns = [c for c in RESTORE_TEXT_COLUMNS if c in reference_questions.columns]
        hits = []
        for row in reference_questions.select(["Q Name"] + text_columns).iter_rows(named=True):
            values = "\n".join(str(row.get(col) or "") for col in text_columns)
            if _contains_crop_marker_text(values):
                hits.append(row["Q Name"])
        return sorted(set(hits))
    ```

### `_is_selected_crop_value` {#fn--is-selected-crop-value-1431}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1431`

**Signature**

```python
def _is_selected_crop_value(value) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def _is_selected_crop_value(value) -> bool:
        return str(value or "").strip().lower() not in {"", "0", "0.0", "none", "nan"}
    ```

### `_build_sorted_crop_entries` {#fn--build-sorted-crop-entries-1435}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1435`

**Signature**

```python
def _build_sorted_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Implements logic in the `Step 4 Exploding answer options` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _build_sorted_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
        meta = extract_crop_metadata(crop_df, language)
        label_col = meta.get("label_col")
        dataset_col = meta.get("dataset_col")
        select_col = meta.get("select_col")
        if not label_col or label_col not in crop_df.columns:
            return []

        needed = [label_col]
        if dataset_col and dataset_col in crop_df.columns:
            needed.append(dataset_col)
        if select_col and select_col in crop_df.columns:
            needed.append(select_col)

        entries = []
        for idx, row in enumerate(crop_df.select(needed).iter_rows(named=True), start=1):
            label = str(row.get(label_col) or "").strip()
            code = str(row.get(dataset_col) or "").strip() if dataset_col and dataset_col in crop_df.columns else ""
            selected = _is_selected_crop_value(row.get(select_col)) if select_col and select_col in crop_df.columns else False
            if not label and not code:
                continue
            entries.append({"row_idx": idx, "label": label, "code": code, "selected": selected})

        entries.sort(key=lambda e: (0 if e["selected"] else 1, e["row_idx"]))
        return entries
    ```

### `build_crop_option_block` {#fn-build-crop-option-block-1462}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1462`

**Signature**

```python
def build_crop_option_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool=True) -> str:
```

**Returns:** `str`

**What it does:** Builds a numbered crop label block: selected crops first, then others.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `include_no_crop` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_crop_option_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool = True) -> str:
        """Builds a numbered crop label block: selected crops first, then others."""
        entries = _build_sorted_crop_entries(crop_df, language)
        labels = [e["label"] for e in entries if e["label"]]
        if not labels:
            return ""

        lines = [f"{idx}){label}" for idx, label in enumerate(labels, start=1)]
        if include_no_crop:
            lines.extend(["91)No crop production", "92)DON'T KNOW", "93)REFUSED"])
        else:
            lines.extend(["92)DON'T KNOW", "93)REFUSED"])
        return "\n".join(lines)
    ```

### `build_crop_code_block` {#fn-build-crop-code-block-1477}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1477`

**Signature**

```python
def build_crop_code_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool=True) -> str:
```

**Returns:** `str`

**What it does:** Builds a numbered crop dataset-code block: selected crops first, then others.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `include_no_crop` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def build_crop_code_block(crop_df: pl.DataFrame, language: str, include_no_crop: bool = True) -> str:
        """Builds a numbered crop dataset-code block: selected crops first, then others."""
        entries = _build_sorted_crop_entries(crop_df, language)
        codes = [e["code"] for e in entries if e["code"]]
        if not codes:
            return ""

        lines = [f"{idx}){code}" for idx, code in enumerate(codes, start=1)]
        if include_no_crop:
            lines.extend(["91)No crop production", "92)DON'T KNOW", "93)REFUSED"])
        else:
            lines.extend(["92)DON'T KNOW", "93)REFUSED"])
        return "\n".join(lines)
    ```

### `rebuild_crop_questions_for_deployed_form` {#fn-rebuild-crop-questions-for-deployed-form-1492}

**Pipeline stage:** `Step 4 Exploding answer options`

**Location:** `scripts/geopoll_validator.py:1492`

**Signature**

```python
def rebuild_crop_questions_for_deployed_form(questions_df: pl.DataFrame, template_questions: pl.DataFrame, crop_df: pl.DataFrame, language: str, candidate_columns: Optional[list[str]]=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Replaces crop placeholders using the current questionnaire Crop list.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `template_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 4 Exploding answer options` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 4 Exploding answer options` stage. |

??? note "Function source"

    ```python
    def rebuild_crop_questions_for_deployed_form(
        questions_df: pl.DataFrame,
        template_questions: pl.DataFrame,
        crop_df: pl.DataFrame,
        language: str,
        candidate_columns: Optional[list[str]] = None,
    ) -> pl.DataFrame:
        """
        Replaces crop placeholders using the current questionnaire Crop list.
        Handles label and code markers, singular/plural and language-suffixed forms.
        """
        crop_qnames = set(find_crop_placeholder_questions(template_questions))
        columns = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in questions_df.columns]
        if not crop_qnames or not columns:
            return questions_df.clone()

        main_block = build_crop_option_block(crop_df, language, include_no_crop=True)
        sold_block = build_crop_option_block(crop_df, language, include_no_crop=False)
        main_code_block = build_crop_code_block(crop_df, language, include_no_crop=True)
        sold_code_block = build_crop_code_block(crop_df, language, include_no_crop=False)
        if not main_block:
            return questions_df.clone()

        crop_qnames_list = sorted(crop_qnames)
        qname_lc = pl.col("Q Name").cast(pl.Utf8).str.to_lowercase()
        is_crop_q = pl.col("Q Name").is_in(crop_qnames_list)
        is_sales_q = qname_lc.str.contains("sales")

        exprs = []
        for col in columns:
            base = pl.col(col).cast(pl.Utf8).fill_null("")

            has_marker = (
                base.str.contains(CROP_LABEL_MARKER_PATTERN)
                | base.str.contains(CROP_SOLD_LABEL_MARKER_PATTERN)
                | base.str.contains(CROP_CODE_MARKER_PATTERN)
                | base.str.contains(CROP_SOLD_CODE_MARKER_PATTERN)
            )

            replaced_main = (
                base
                .str.replace_all(CROP_LABEL_MARKER_PATTERN, main_block)
                .str.replace_all(CROP_SOLD_LABEL_MARKER_PATTERN, sold_block)
                .str.replace_all(CROP_CODE_MARKER_PATTERN, main_code_block)
                .str.replace_all(CROP_SOLD_CODE_MARKER_PATTERN, sold_code_block)
            )

            replaced_sold = (
                base
                .str.replace_all(CROP_LABEL_MARKER_PATTERN, sold_block)
                .str.replace_all(CROP_SOLD_LABEL_MARKER_PATTERN, sold_block)
                .str.replace_all(CROP_CODE_MARKER_PATTERN, sold_code_block)
                .str.replace_all(CROP_SOLD_CODE_MARKER_PATTERN, sold_code_block)
            )

            exprs.append(
                pl.when(is_crop_q & has_marker)
                .then(
                    pl.when(is_sales_q).then(replaced_sold).otherwise(replaced_main)
                )
                .otherwise(base)
                .alias(col)
            )

        return questions_df.with_columns(exprs)
    ```

### `normalize_text_expr` {#fn-normalize-text-expr-1710}

**Pipeline stage:** `Step 6 Normalisation helpers`

**Location:** `scripts/geopoll_validator.py:1710`

**Signature**

```python
def normalize_text_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Polars expression that lowercases a string column, removes punctuation,

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_text_expr(col_name: str) -> pl.Expr:
        """
        Polars expression that lowercases a string column, removes punctuation,
        and collapses whitespace. Apply as an alias so the original column is preserved.

        Usage:
            df.with_columns(normalize_text_expr("option_label").alias("option_label_norm"))
        """
        return (
            pl.col(col_name)
            .cast(pl.Utf8)
            .fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"[^\w\s]", "")   # remove punctuation
            .str.replace_all(r"\s+", " ")       # collapse multiple spaces
            .str.strip_chars()
        )
    ```

### `normalize_code_token_expr` {#fn-normalize-code-token-expr-1729}

**Pipeline stage:** `Step 6 Normalisation helpers`

**Location:** `scripts/geopoll_validator.py:1729`

**Signature**

```python
def normalize_code_token_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Normalizes code tokens from the 'Codes' column for stable comparisons.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_code_token_expr(col_name: str) -> pl.Expr:
        """Normalizes code tokens from the 'Codes' column for stable comparisons."""
        return (
            pl.col(col_name)
            .cast(pl.Utf8)
            .fill_null("")
            .str.to_lowercase()
            .str.replace_all(r"[^a-z0-9_]+", "")
            .str.strip_chars()
        )
    ```

### `normalize_mandatory_expr` {#fn-normalize-mandatory-expr-1741}

**Pipeline stage:** `Step 6 Normalisation helpers`

**Location:** `scripts/geopoll_validator.py:1741`

**Signature**

```python
def normalize_mandatory_expr(col_name: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Polars expression that maps any common yes/no variant to canonical "yes"/"no"/""

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 6 Normalisation helpers` stage. |

??? note "Function source"

    ```python
    def normalize_mandatory_expr(col_name: str) -> pl.Expr:
        """
        Polars expression that maps any common yes/no variant to canonical "yes"/"no"/""
        so that "Yes", "YES", "y", "true", "1" are all treated as equivalent.

        Using when/then/otherwise keeps this inside the Polars execution engine
        (faster and parallelisable) vs a Python lambda with map_elements.
        """
        cleaned = (
            pl.col(col_name)
            .cast(pl.Utf8)
            .fill_null("")
            .str.to_lowercase()
            .str.strip_chars()
        )
        return (
            pl.when(cleaned.is_in(["yes", "y", "true", "1"])).then(pl.lit("yes"))
            .when(cleaned.is_in(["no",  "n", "false", "0"])).then(pl.lit("no"))
            .otherwise(pl.lit(""))
        )
    ```

### `_normalize_skip_text` {#fn--normalize-skip-text-1776}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1776`

**Signature**

```python
def _normalize_skip_text(value) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 7 Comparison and validation functions` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _normalize_skip_text(value) -> str:
        text = "" if value is None else str(value)
        return re.sub(r"\s+", " ", text).strip()
    ```

### `_parse_skip_option_codes` {#fn--parse-skip-option-codes-1781}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1781`

**Signature**

```python
def _parse_skip_option_codes(skip_text: str, max_range_span: int=200, max_total_codes: int=500) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Extracts numeric option codes from the left side of skip rules.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `max_range_span` | positional_or_keyword | No | `200` | `int` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `max_total_codes` | positional_or_keyword | No | `500` | `int` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _parse_skip_option_codes(
        skip_text: str,
        max_range_span: int = 200,
        max_total_codes: int = 500,
    ) -> set[int]:
        """
        Extracts numeric option codes from the left side of skip rules.
        Examples handled: "1=...", "1-4 = ...", "1,3,5=...", "2 to 4 = ...".

        Safety guards:
          - do not fully expand very wide ranges,
          - cap total extracted codes to avoid pathological blowups.
        """
        if not skip_text:
            return set()

        codes = set()
        parts = [p.strip() for p in re.split(r"[\r\n;]+", str(skip_text)) if p.strip()]
        for part in parts:
            if len(codes) >= max_total_codes:
                break

            left = part.split("=", 1)[0] if "=" in part else part

            for a, b in re.findall(r"\b(\d+)\s*(?:-|to)\s*(\d+)\b", left, flags=re.IGNORECASE):
                start, end = int(a), int(b)
                lo, hi = sorted((start, end))
                span = hi - lo + 1

                if span <= max_range_span and (len(codes) + span) <= max_total_codes:
                    codes.update(range(lo, hi + 1))
                else:
                    # Keep endpoints so we still validate something without exploding runtime.
                    codes.add(lo)
                    codes.add(hi)
                    if len(codes) >= max_total_codes:
                        break

            if len(codes) >= max_total_codes:
                break

            left_no_ranges = re.sub(r"\b\d+\s*(?:-|to)\s*\d+\b", " ", left, flags=re.IGNORECASE)
            for n in re.findall(r"\b\d+\b", left_no_ranges):
                codes.add(int(n))
                if len(codes) >= max_total_codes:
                    break

        return codes
    ```

### `_extract_referenced_qnames` {#fn--extract-referenced-qnames-1830}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1830`

**Signature**

```python
def _extract_referenced_qnames(skip_text: str, source_q: str, ref_qnames: set[str], curr_qnames: set[str]) -> set[str]:
```

**Returns:** `set[str]`

**What it does:** Extract target question names from skip rules using a strict heuristic:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `source_q` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `ref_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `curr_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_referenced_qnames(skip_text: str, source_q: str, ref_qnames: set[str], curr_qnames: set[str]) -> set[str]:
        """
        Extract target question names from skip rules using a strict heuristic:
          - parse only RHS of '=' (or line/segment after '='),
          - take the first token as candidate target,
          - ignore common routing labels (ineligible, end, quota, etc.),
          - keep candidates that are known qnames OR look like qnames (underscore).
        """
        text = str(skip_text or "")
        if len(text) > 4000:
            text = text[:4000]

        stopwords = {
            "ineligible", "eligible", "end", "poll", "quota", "reached",
            "terminate", "terminated", "screenout", "screen_out",
            "refusal", "refused", "closeout", "close", "callback",
            "yes", "no", "na", "n_a", "none",
        }

        out = set()
        segments = [s.strip() for s in re.split(r"[\r\n;]+", text) if s.strip()]
        for seg in segments:
            if "=" not in seg:
                continue
            rhs = seg.split("=", 1)[1].strip()
            if not rhs:
                continue

            m = re.match(r"^\s*([A-Za-z_]\w*)", rhs)
            if not m:
                continue

            cand = m.group(1)
            cand_l = cand.lower()
            if cand == source_q or cand_l in stopwords:
                continue

            if cand in ref_qnames or cand in curr_qnames or ("_" in cand):
                out.add(cand)

        return out
    ```

### `_extract_qname_tokens` {#fn--extract-qname-tokens-1881}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1881`

**Signature**

```python
def _extract_qname_tokens(text: str, known_qnames: set[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Return word tokens from text that are known Q Names.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_qname_tokens(text: str, known_qnames: set[str]) -> list[str]:
        """Return word tokens from text that are known Q Names."""
        return [t for t in _QNAME_TOKEN_RE.findall(str(text or "")) if t in known_qnames]
    ```

### `_extract_qname_like` {#fn--extract-qname-like-1886}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1886`

**Signature**

```python
def _extract_qname_like(text: str, known_qnames: set[str]) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Return word tokens that are either known Q Names OR look like Q Names

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_qname_like(text: str, known_qnames: set[str]) -> list[str]:
        """
        Return word tokens that are either known Q Names OR look like Q Names
        (contain an underscore).  This lets us detect references to Q Names
        that were renamed / removed from the current questionnaire.
        """
        return [t for t in _QNAME_TOKEN_RE.findall(str(text or ""))
                if t in known_qnames or "_" in t]
    ```

### `_extract_condition_codes` {#fn--extract-condition-codes-1896}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1896`

**Signature**

```python
def _extract_condition_codes(stmt: str) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Extract option codes from a full Default-column rule statement by finding

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `stmt` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_condition_codes(stmt: str) -> set[int]:
        """
        Extract option codes from a full Default-column rule statement by finding
        the range between '=' and 'go to', e.g.:
          "if hh_gender = 1-4, go to hh_education"  -> {1, 2, 3, 4}
          "For any response, go to X"               -> {} (any response = no range)
        Receives the FULL statement (not sliced) so that 'go to' can anchor the match.
        """
        match = re.search(
            r'=\s*([\d][^;=\n]*?)\s*,?\s*go\s+to',
            stmt, re.IGNORECASE,
        )
        if not match:
            return set()
        rng = match.group(1).strip()
        codes: set[int] = set()
        for a, b in re.findall(r'\b(\d+)\s*(?:-|to)\s*(\d+)\b', rng, re.IGNORECASE):
            lo, hi = sorted((int(a), int(b)))
            codes.update(range(lo, hi + 1))
        clean = re.sub(r'\b\d+\s*(?:-|to)\s*\d+\b', ' ', rng, flags=re.IGNORECASE)
        codes.update(int(n) for n in re.findall(r'\b\d+\b', clean))
        return codes
    ```

### `_extract_skip_codes_for_target` {#fn--extract-skip-codes-for-target-1919}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1919`

**Signature**

```python
def _extract_skip_codes_for_target(skip_text: str, target: str) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Extract option codes from Skip-Pattern lines that send flow to *target*.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `target` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _extract_skip_codes_for_target(skip_text: str, target: str) -> set[int]:
        """
        Extract option codes from Skip-Pattern lines that send flow to *target*.
        Handles both compact and verbose styles:
          "1-3 = hh_education"
          "if hh_gender = 1-3, go to hh_education"
          "1 = q_a 2-4 = q_b"
          "if q = 1, go to a if q = 2-4, go to b"
        """
        def _codes_from_spec(spec: str) -> set[int]:
            out: set[int] = set()
            for a, b in re.findall(r'\b(\d+)\s*(?:-|to)\s*(\d+)\b', spec, re.IGNORECASE):
                lo, hi = sorted((int(a), int(b)))
                out.update(range(lo, hi + 1))
            clean = re.sub(r'\b\d+\s*(?:-|to)\s*\d+\b', ' ', spec, flags=re.IGNORECASE)
            out.update(int(n) for n in re.findall(r'\b\d+\b', clean))
            return out

        compact_re = re.compile(
            r'(\d+(?:\s*(?:-|to)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:-|to)\s*\d+)?)*)\s*=\s*(\[[^\]]+\]|[A-Za-z_]\w*)',
            re.IGNORECASE,
        )
        verbose_re = re.compile(
            r'if\s+[A-Za-z_]\w*\s*=\s*([^;]+?)\s*,?\s*go\s+to\s*(.+?)(?=(?:\s+if\s+[A-Za-z_]\w*\s*=)|$)',
            re.IGNORECASE,
        )

        codes: set[int] = set()
        for part in re.split(r'[\r\n;]+', str(skip_text or "")):
            if target not in part:
                continue

            # Compact style supports multiple mappings in one segment.
            for m in compact_re.finditer(part):
                code_spec = m.group(1)
                target_text = m.group(2)
                target_tokens = _extract_qname_like(target_text, {target})
                if target in target_tokens or target_text.strip('[] ') == target:
                    codes.update(_codes_from_spec(code_spec))

            # Verbose style supports multiple "if ... go to ..." clauses in one segment.
            for vm in verbose_re.finditer(part):
                code_spec = vm.group(1)
                target_text = vm.group(2).strip().strip('.')
                target_tokens = _extract_qname_like(target_text, {target})
                if target in target_tokens or target_text.strip('[] ') == target:
                    codes.update(_codes_from_spec(code_spec))

        return codes
    ```

### `_extract_skip_codes_for_target._codes_from_spec` {#fn--codes-from-spec-1928}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1928`

**Signature**

```python
def _codes_from_spec(spec: str) -> set[int]:
```

**Returns:** `set[int]`

**What it does:** Implements logic in the `Step 7 Comparison and validation functions` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `spec` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _codes_from_spec(spec: str) -> set[int]:
            out: set[int] = set()
            for a, b in re.findall(r'\b(\d+)\s*(?:-|to)\s*(\d+)\b', spec, re.IGNORECASE):
                lo, hi = sorted((int(a), int(b)))
                out.update(range(lo, hi + 1))
            clean = re.sub(r'\b\d+\s*(?:-|to)\s*\d+\b', ' ', spec, flags=re.IGNORECASE)
            out.update(int(n) for n in re.findall(r'\b\d+\b', clean))
            return out
    ```

### `_parse_default_skip_rules` {#fn--parse-default-skip-rules-1969}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:1969`

**Signature**

```python
def _parse_default_skip_rules(default_text: str, known_qnames: set[str]) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Parse "Default skip patterns & conditional" into structured rules.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `default_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _parse_default_skip_rules(default_text: str, known_qnames: set[str]) -> list[dict]:
        """
        Parse "Default skip patterns & conditional" into structured rules.
        Each rule: {targets, is_flexible, is_next_question, raw}

        Handles both compact and verbose styles, including multiple clauses in one line.
        """
        text = _normalize_skip_text(str(default_text or ""))
        if not text:
            return []

        rules = []

        # Verbose style, including chained clauses in one segment.
        verbose_re = re.compile(
            r'if\s+[A-Za-z_]\w*\s*=\s*([^;]+?)\s*,?\s*go\s+to\s*(.+?)(?=(?:\s+if\s+[A-Za-z_]\w*\s*=)|$)',
            re.IGNORECASE,
        )
        for vm in verbose_re.finditer(text):
            code_spec = vm.group(1)
            target_text = vm.group(2).strip().strip('.')
            is_next_question = bool(_NEXT_Q_RE.search(target_text))
            is_flexible = bool(_OPTIONAL_RE.search(target_text))
            targets = _extract_qname_like(target_text, known_qnames)
            option_codes = _extract_condition_codes(f"x = {code_spec}, go to y")
            if targets or is_next_question:
                rules.append({
                    "targets": targets,
                    "is_flexible": is_flexible,
                    "is_next_question": is_next_question,
                    "option_codes": option_codes,
                    "raw": vm.group(0),
                })

        # Compact form fallback (no "go to"): "1 = q1 2-4 = q2"
        # Keep full RHS clause so patterns like "OR optional question" are preserved.
        if not rules:
            compact_re = re.compile(
                r'(\d+(?:\s*(?:-|to)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:-|to)\s*\d+)?)*)\s*=\s*(.+?)(?=(?:\s+\d+(?:\s*(?:-|to)\s*\d+)?(?:\s*,\s*\d+(?:\s*(?:-|to)\s*\d+)?)*)\s*=|$)',
                re.IGNORECASE,
            )
            for m in compact_re.finditer(text):
                code_spec = m.group(1)
                target_text = m.group(2).strip().strip('.')
                targets = _extract_qname_like(target_text, known_qnames)
                if not targets:
                    continue
                rules.append({
                    "targets": targets,
                    "is_flexible": bool(_OPTIONAL_RE.search(target_text)),
                    "is_next_question": bool(_NEXT_Q_RE.search(target_text)),
                    "option_codes": _extract_condition_codes(f"x = {code_spec}, go to y"),
                    "raw": m.group(0),
                })

        # Minimal fallback for "For any response, go to target" when no numeric condition exists.
        if not rules:
            any_re = re.compile(r'for\s+any\s+response\s*,?\s*go\s+to\s*(.+)$', re.IGNORECASE)
            m = any_re.search(text)
            if m:
                target_text = m.group(1).strip().strip('.')
                targets = _extract_qname_like(target_text, known_qnames)
                if targets:
                    rules.append({
                        "targets": targets,
                        "is_flexible": bool(_OPTIONAL_RE.search(target_text)),
                        "is_next_question": bool(_NEXT_Q_RE.search(target_text)),
                        "option_codes": set(),
                        "raw": m.group(0),
                    })

        return rules
    ```

### `_semantic_skip_signature` {#fn--semantic-skip-signature-2042}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:2042`

**Signature**

```python
def _semantic_skip_signature(skip_text: str, known_qnames: set[str]) -> tuple[set[tuple], bool]:
```

**Returns:** `tuple[set[tuple], bool]`

**What it does:** Build a semantic signature for skip logic text so phrasing differences

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _semantic_skip_signature(skip_text: str, known_qnames: set[str]) -> tuple[set[tuple], bool]:
        """
        Build a semantic signature for skip logic text so phrasing differences
        can still compare as equal.

        Signature item:
          (target, sorted_codes_tuple, is_flexible, is_next_question)
        """
        text = _normalize_skip_text(skip_text)
        if not text:
            return set(), False

        rules = _parse_default_skip_rules(text, known_qnames)
        if not rules:
            return set(), False

        sig: set[tuple] = set()
        for rule in rules:
            codes = tuple(sorted(int(c) for c in (rule.get("option_codes") or set())))
            is_flexible = bool(rule.get("is_flexible"))
            is_next_question = bool(rule.get("is_next_question"))
            targets = sorted(set(rule.get("targets") or []))

            if not targets and is_next_question:
                sig.add(("__NEXT__", codes, is_flexible, is_next_question))
                continue

            for t in targets:
                sig.add((t, codes, is_flexible, is_next_question))

        return sig, True
    ```

### `_check_skip_consistency` {#fn--check-skip-consistency-2074}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:2074`

**Signature**

```python
def _check_skip_consistency(skip_text: str, rules: list[dict], q_mandatory_map: dict[str, str], curr_qnames: set[str], known_qnames: set[str], source_q: str, next_qname: str | None) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Returns a list of issue descriptions (empty = consistent).

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `skip_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `rules` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `q_mandatory_map` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `curr_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `known_qnames` | positional_or_keyword | Yes | `-` | `set[str]` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `source_q` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `next_qname` | positional_or_keyword | Yes | `-` | `str | None` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def _check_skip_consistency(
        skip_text      : str,
        rules          : list[dict],
        q_mandatory_map: dict[str, str],
        curr_qnames    : set[str],
        known_qnames   : set[str],
        source_q       : str,
        next_qname     : str | None,
    ) -> list[str]:
        """
        Returns a list of issue descriptions (empty = consistent).

        Rules:
        - Each required target Q Name must appear in skip_text.
        - If the rule is flexible ("OR optional question"), a non-mandatory Q Name
          in skip_text is also acceptable.
        - [next question] is treated as equivalent to the concrete next Q Name.
        - Any explicit RHS target that does not exist in current questionnaire
          is treated as a broken reference.

        Range-check policy:
        - Compare ranges only when a target has one unambiguous numeric mapping.
        - Skip range comparison for ambiguous authoring forms (e.g. "otherwise").
        """
        skip_text_s = str(skip_text or "")
        skip_present = set(_extract_qname_like(skip_text_s, curr_qnames))
        skip_mentions_next = bool(_NEXT_Q_RE.search(skip_text_s))
        issues = []

        # Broken target references must stay high severity:
        # RHS targets that do not exist in the current questionnaire.
        skip_targets = _extract_referenced_qnames(
            skip_text_s,
            source_q=source_q,
            ref_qnames=known_qnames,
            curr_qnames=curr_qnames,
        )
        invalid_targets = sorted(t for t in skip_targets if t not in curr_qnames)
        if invalid_targets:
            issues.append(
                f"target question(s) not found in current questionnaire: {invalid_targets}"
            )

        expected_codes_by_target: dict[str, set[int]] = {}
        range_skip_targets: set[str] = set()

        for rule in rules:
            targets = list(rule.get("targets") or [])
            is_flexible = bool(rule.get("is_flexible"))
            is_next_question = bool(rule.get("is_next_question"))
            expected_codes = set(rule.get("option_codes") or set())
            raw_l = str(rule.get("raw") or "").lower()

            # Resolve [next question] to concrete target when possible.
            if is_next_question and not targets and next_qname:
                targets = [next_qname]

            if not targets:
                continue

            found_targets = [t for t in targets if t in skip_present]

            # Equivalence: skip says [next question], rule says concrete next qname.
            if not found_targets and skip_mentions_next and next_qname and next_qname in targets:
                found_targets = [next_qname]

            # Equivalence: rule says [next question], skip says concrete next qname.
            if not found_targets and is_next_question and next_qname and next_qname in skip_present:
                found_targets = [next_qname]

            if not found_targets:
                if is_flexible:
                    non_mand = [
                        q for q in skip_present
                        if q_mandatory_map.get(q) not in ("mandatory", "mandatory-panel")
                    ]
                    if not non_mand:
                        issues.append(
                            f"expected {targets} (or non-mandatory alternative) not found in skip pattern"
                        )
                else:
                    if not skip_text_s.strip():
                        issues.append(
                            f"skip pattern is empty but default/spec says go to {targets}"
                        )
                    else:
                        issues.append(
                            f"expected {targets} in skip pattern; got: {skip_text_s[:80]}"
                        )

            ambiguous = (len(targets) != 1) or ("otherwise" in raw_l)
            if ambiguous or not expected_codes:
                for t in targets:
                    range_skip_targets.add(t)
            else:
                t = targets[0]
                expected_codes_by_target.setdefault(t, set()).update(expected_codes)

        # Range verification per target (single comparison per target).
        for t, expected in expected_codes_by_target.items():
            if t in range_skip_targets:
                continue

            # next-question equivalence may hide explicit target token in skip text.
            if t not in skip_present and not (skip_mentions_next and next_qname == t):
                continue

            actual_codes = _extract_skip_codes_for_target(skip_text_s, t)
            if actual_codes and actual_codes != expected:
                issues.append(
                    f"option range mismatch for target '{t}': "
                    f"default/spec says {sorted(expected)}, "
                    f"skip pattern has {sorted(actual_codes)}"
                )

        return issues
    ```

### `validate_skip_patterns` {#fn-validate-skip-patterns-2191}

**Pipeline stage:** `Step 7 Comparison and validation functions`

**Location:** `scripts/geopoll_validator.py:2191`

**Signature**

```python
def validate_skip_patterns(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, current_options_en: pl.DataFrame | None=None, reference_options_en: pl.DataFrame | None=None, option_issue_qnames: set[str] | None=None, option_issue_reasons: dict[str, set[str]] | None=None, q_mandatory_map: dict[str, str] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Four-layer skip-pattern validation:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_options_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `reference_options_en` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `option_issue_qnames` | positional_or_keyword | No | `None` | `set[str] | None` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `option_issue_reasons` | positional_or_keyword | No | `None` | `dict[str, set[str]] | None` | Input used by the `Step 7 Comparison and validation functions` stage. |
| `q_mandatory_map` | positional_or_keyword | No | `None` | `dict[str, str] | None` | Input used by the `Step 7 Comparison and validation functions` stage. |

??? note "Function source"

    ```python
    def validate_skip_patterns(
        current_questions    : pl.DataFrame,
        reference_questions  : pl.DataFrame,
        current_options_en   : pl.DataFrame | None = None,
        reference_options_en : pl.DataFrame | None = None,
        option_issue_qnames  : set[str] | None = None,
        option_issue_reasons : dict[str, set[str]] | None = None,
        q_mandatory_map      : dict[str, str] | None = None,
    ) -> pl.DataFrame:
        """
        Four-layer skip-pattern validation:

        1. Template consistency check (mostly medium): current effective skip rule
           should align with template effective rule. Broken references remain high.

        Effective rule selection per side:
           - Current (analyzed): use "Specify skip pattern variable (from blue text)"
             when filled; otherwise fall back to "Skip Pattern", then "Default".
           - Reference/template: use template "Specify" when filled; otherwise
             template "Skip Pattern", then template "Default".

        2. Option code validity (high): numeric codes referenced in Skip Pattern
           must actually exist in the question's answer options.

        3. Option drift risk (medium): a question that has skip logic also had its
           option set changed, so skip ranges may need review.
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field"     : pl.Utf8, "current" : pl.Utf8, "reference": pl.Utf8,
            "severity"  : pl.Utf8, "excel_row": pl.Int64,
        }

        DEF_COL  = "Default skip patterns & conditional "
        SPEC_COL = "Specify skip pattern variable (from blue text)"
        SKIP_COL = "Skip Pattern"

        has_def_cur  = DEF_COL  in current_questions.columns
        has_spec_cur = SPEC_COL in current_questions.columns
        has_skip_cur = SKIP_COL in current_questions.columns

        has_def_ref  = DEF_COL  in reference_questions.columns
        has_spec_ref = SPEC_COL in reference_questions.columns
        has_skip_ref = SKIP_COL in reference_questions.columns

        if not has_def_cur and not has_skip_cur and not has_spec_cur:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        curr_qnames = set(current_questions["Q Name"].to_list())
        ref_qnames  = set(reference_questions["Q Name"].to_list())
        known_qnames = curr_qnames | ref_qnames
        q_mandatory_map     = q_mandatory_map or {}
        option_issue_qnames = option_issue_qnames or set()
        option_issue_reasons = option_issue_reasons or {}

        # Option code lookup for validity check (layer 3)
        curr_opt_map: dict[str, set[int]] = {}
        if current_options_en is not None and current_options_en.height > 0:
            for row in current_options_en.select(["Q Name", "option_code"]).iter_rows(named=True):
                q, c = row.get("Q Name"), row.get("option_code")
                if q and c is not None:
                    curr_opt_map.setdefault(q, set()).add(int(c))

        # Minimal row maps from current + reference questionnaires
        cur_cols = ["Q Name"] + [c for c in [SKIP_COL, DEF_COL, SPEC_COL, "excel_row"]
                                 if c in current_questions.columns]
        ref_cols = ["Q Name"] + [c for c in [SKIP_COL, DEF_COL, SPEC_COL]
                                 if c in reference_questions.columns]
        cur_rows = {r["Q Name"]: r
                    for r in current_questions.select(cur_cols).iter_rows(named=True)}
        ref_rows = {r["Q Name"]: r
                    for r in reference_questions.select(ref_cols).iter_rows(named=True)}

        # Q Name ordering for "next question" resolution
        qname_list = current_questions["Q Name"].to_list()
        qname_next = {q: qname_list[i + 1]
                      for i, q in enumerate(qname_list) if i + 1 < len(qname_list)}

        issues = []
        seen_drift = set()

        for qname, cr in cur_rows.items():
            excel_row = cr.get("excel_row")
            skip_text = _normalize_skip_text(cr.get(SKIP_COL) or "")
            def_text  = _normalize_skip_text(cr.get(DEF_COL)  or "")
            spec_text = _normalize_skip_text(cr.get(SPEC_COL) or "")

            rr = ref_rows.get(qname, {})
            ref_skip_text = _normalize_skip_text(rr.get(SKIP_COL) or "") if has_skip_ref else ""
            ref_def_text  = _normalize_skip_text(rr.get(DEF_COL)  or "") if has_def_ref else ""
            ref_spec_text = _normalize_skip_text(rr.get(SPEC_COL) or "") if has_spec_ref else ""

            # Current effective rule: Specify > Skip Pattern > Default
            current_effective = spec_text if spec_text else (skip_text if skip_text else def_text)

            # Reference/template effective rule: Specify > Skip Pattern > Default
            reference_effective = ref_spec_text if ref_spec_text else (ref_skip_text if ref_skip_text else ref_def_text)

            # Layer 1: Current effective rule must align with template effective rule.
            if reference_effective and current_effective:
                rules = _parse_default_skip_rules(reference_effective, known_qnames)
                for desc in _check_skip_consistency(
                    current_effective,
                    rules,
                    q_mandatory_map,
                    curr_qnames,
                    known_qnames,
                    qname,
                    qname_next.get(qname),
                ):
                    is_range = desc.startswith("option range mismatch")
                    is_broken_target = desc.startswith("target question(s) not found in current questionnaire")
                    is_empty = desc.startswith("skip pattern is empty")
                    severity = "high" if (is_broken_target or is_empty) else "medium"
                    issues.append({
                        "issue_type": "skip_range_mismatch" if is_range else "skip_consistency_error",
                        "set_name": "",
                        "Q Name": qname, "field": SKIP_COL,
                        "current": current_effective[:220], "reference": reference_effective[:220],
                        "severity": "medium" if is_range else severity,
                        "excel_row": excel_row,
                    })

            # Layer 2: no additional override-only notes are emitted to avoid noise.

            # Layer 3: Option codes in effective current skip rule must exist in options
            if current_effective:
                mentioned = _parse_skip_option_codes(current_effective)
                available = curr_opt_map.get(qname, set())
                if mentioned and available:
                    invalid = sorted(c for c in mentioned if c not in available)
                    if invalid:
                        issues.append({
                            "issue_type": "skip_pattern_invalid_option_code", "set_name": "",
                            "Q Name": qname, "field": SKIP_COL,
                            "current": f"invalid option code(s): {invalid}",
                            "reference": f"valid codes: {sorted(available)}",
                            "severity": "high", "excel_row": excel_row,
                        })

            # Layer 4: Option drift risk
            if current_effective and qname in option_issue_qnames:
                key = (qname, SKIP_COL)
                if key not in seen_drift:
                    seen_drift.add(key)
                    _reasons = sorted(option_issue_reasons.get(qname, set()))
                    _trigger_txt = (
                        f"Option drift triggers: {'; '.join(_reasons)}"
                        if _reasons else
                        "Option drift trigger detected; see Option Changes for this Q Name"
                    )
                    issues.append({
                        "issue_type": "potential_skip_pattern_option_drift", "set_name": "",
                        "Q Name": qname, "field": SKIP_COL,
                        "current": _trigger_txt,
                        "reference": "",
                        "severity": "medium", "excel_row": excel_row,
                    })

        if not issues:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        return (
            pl.DataFrame(issues)
            .unique(subset=["issue_type", "Q Name", "field", "current", "reference"], keep="first")
        )
    ```

### `make_presence_issues` {#fn-make-presence-issues-2368}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `scripts/geopoll_validator.py:2368`

**Signature**

```python
def make_presence_issues(added: pl.DataFrame, removed: pl.DataFrame, reference_questions: pl.DataFrame | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts added/removed question lists into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `added` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `removed` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `reference_questions` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def make_presence_issues(
        added: pl.DataFrame,
        removed: pl.DataFrame,
        reference_questions: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """
        Converts added/removed question lists into the common issues schema.

        Severity rules:
          - Optional questions (o_ prefix): 'info'   tracked but not a blocker
          - Non-optional added            : 'medium'  unexpected addition, review needed
          - Non-optional removed          : 'high'    mandatory question missing
        """
        added_opt_lookup = (
            added
            .with_columns([
                pl.col("Q Name").cast(pl.Utf8).str.strip_chars().alias("_q"),
                pl.when(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.starts_with("o_"))
                .then(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.slice(2))
                .otherwise(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
                .str.to_lowercase()
                .alias("_core"),
            ])
            .filter(pl.col("_q").str.starts_with("o_"))
            .select(["_core", pl.col("Q Name").alias("_optional_qname")])
            .unique(subset=["_core"], keep="first")
        )

        if reference_questions is not None and "Mandatory" in reference_questions.columns:
            removed_aug = (
                removed.join(
                    reference_questions.select(["Q Name", "Mandatory"]),
                    on="Q Name", how="left"
                )
                .with_columns(
                    pl.when(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.starts_with("o_"))
                    .then(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.slice(2))
                    .otherwise(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
                    .str.to_lowercase()
                    .alias("_core")
                )
            )
            severity_expr = (
                pl.when(normalize_mandatory_expr("Mandatory") == "yes")
                .then(pl.lit("high"))
                .otherwise(pl.lit("info"))
                .alias("severity")
            )
            moved_to_optional = (
                removed_aug
                .join(added_opt_lookup, on="_core", how="inner")
                .filter(normalize_mandatory_expr("Mandatory") == "yes")
            )
        else:
            removed_aug = removed.with_columns([
                pl.lit("").alias("Mandatory"),
                pl.when(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.starts_with("o_"))
                .then(pl.col("Q Name").cast(pl.Utf8).str.strip_chars().str.slice(2))
                .otherwise(pl.col("Q Name").cast(pl.Utf8).str.strip_chars())
                .str.to_lowercase()
                .alias("_core"),
            ])
            severity_expr = (
                pl.when(pl.col("is_optional")).then(pl.lit("info")).otherwise(pl.lit("high"))
                .alias("severity")
            )
            moved_to_optional = pl.DataFrame(schema={
                "Q Name": pl.Utf8, "is_optional": pl.Boolean, "Mandatory": pl.Utf8,
                "_core": pl.Utf8, "_optional_qname": pl.Utf8,
            })

        moved_issues = (
            moved_to_optional.with_columns([
                pl.lit("mandatory_to_optional").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("Q Name").alias("field"),
                pl.col("_optional_qname").alias("current"),
                pl.lit("present (mandatory in reference)").alias("reference"),
                pl.lit("high").alias("severity"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )

        added_base = (
            added.join(moved_to_optional.select(pl.col("_optional_qname").alias("Q Name")), on="Q Name", how="anti")
            if moved_to_optional.height > 0 else added
        )
        added_issues = added_base.with_columns([
            pl.lit("added_question").alias("issue_type"),
            pl.lit("").alias("set_name"),
            pl.lit("Q Name").alias("field"),
            pl.lit("present").alias("current"),
            pl.lit("missing_in_reference").alias("reference"),
            pl.lit("info").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        removed_base = (
            removed_aug.join(moved_to_optional.select(["Q Name"]), on="Q Name", how="anti")
            if moved_to_optional.height > 0 else removed_aug
        )
        removed_issues = removed_base.with_columns([
            pl.lit("removed_question").alias("issue_type"),
            pl.lit("").alias("set_name"),
            pl.lit("Q Name").alias("field"),
            pl.lit("missing_in_current").alias("current"),
            pl.lit("present").alias("reference"),
            severity_expr,
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        return pl.concat([added_issues, removed_issues, moved_issues], how="vertical")
    ```

### `make_mandatory_issues` {#fn-make-mandatory-issues-2483}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `scripts/geopoll_validator.py:2483`

**Signature**

```python
def make_mandatory_issues(mandatory_diff: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts mandatory mismatches into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `mandatory_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_mandatory_issues(mandatory_diff: pl.DataFrame) -> pl.DataFrame:
        """Converts mandatory mismatches into the common issues schema."""
        return (
            mandatory_diff
            .with_columns([
                pl.lit("").alias("set_name"),
                pl.col("Mandatory").alias("current"),
                pl.col("Mandatory_ref").alias("reference"),
                pl.lit("high").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `make_option_issues` {#fn-make-option-issues-2497}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `scripts/geopoll_validator.py:2497`

**Signature**

```python
def make_option_issues(option_diff: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts option label mismatches into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def make_option_issues(option_diff: pl.DataFrame) -> pl.DataFrame:
        """Converts option label mismatches into the common issues schema."""
        return (
            option_diff
            .with_columns([
                pl.lit("").alias("set_name"),
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `make_option_presence_issues` {#fn-make-option-presence-issues-2515}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `scripts/geopoll_validator.py:2515`

**Signature**

```python
def make_option_presence_issues(added_options: pl.DataFrame, removed_options: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts added/removed options into the common issues schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `added_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `removed_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def make_option_presence_issues(added_options: pl.DataFrame, removed_options: pl.DataFrame) -> pl.DataFrame:
        """Converts added/removed options into the common issues schema."""
        added_issues = added_options.with_columns([
            pl.lit("").alias("set_name"),
            pl.col("option_label").alias("current"),
            pl.lit(_not_in_reference_text()).alias("reference"),
            pl.lit("medium").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        removed_issues = removed_options.with_columns([
            pl.lit("").alias("set_name"),
            pl.lit("(removed)").alias("current"),
            pl.col("option_label").alias("reference"),
            pl.lit("high").alias("severity"),
            pl.lit(None).cast(pl.Int64).alias("excel_row"),
        ]).select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])

        return pl.concat([added_issues, removed_issues], how="vertical")
    ```

### `build_option_changes_view` {#fn-build-option-changes-view-2536}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `scripts/geopoll_validator.py:2536`

**Signature**

```python
def build_option_changes_view(en_option_diff: pl.DataFrame, en_added_options: pl.DataFrame, en_removed_options: pl.DataFrame, en_code_renumber: pl.DataFrame, tgt_option_diff: pl.DataFrame, tgt_added_options: pl.DataFrame, tgt_removed_options: pl.DataFrame, tgt_code_renumber: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Builds Option Changes rows with independent EN and target-language checks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `en_option_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `en_added_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `en_removed_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `en_code_renumber` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `tgt_option_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `tgt_added_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `tgt_removed_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `tgt_code_renumber` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 8 Issue unifiers` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def build_option_changes_view(
        en_option_diff: pl.DataFrame,
        en_added_options: pl.DataFrame,
        en_removed_options: pl.DataFrame,
        en_code_renumber: pl.DataFrame,
        tgt_option_diff: pl.DataFrame,
        tgt_added_options: pl.DataFrame,
        tgt_removed_options: pl.DataFrame,
        tgt_code_renumber: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """
        Builds Option Changes rows with independent EN and target-language checks.

        Layout policy:
        - Current value / Reference / rule are always EN baseline.
        - For non-EN runs, target language values are added in separate columns.
        """
        is_en = str(target_lang).upper() == "EN"

        def _scope_view(option_diff, added_opts, removed_opts, renumber_opts, scope):
            mismatch = option_diff.with_columns([
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            added = added_opts.with_columns([
                pl.col("option_label").alias("current"),
                pl.lit(_not_in_reference_text()).alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            removed = removed_opts.with_columns([
                pl.lit("(removed)").alias("current"),
                pl.col("option_label").alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            renumber = renumber_opts.with_columns([
                pl.concat_str([
                    pl.col("new_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label").cast(pl.Utf8),
                ]).alias("current"),
                pl.concat_str([
                    pl.col("old_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label_ref").cast(pl.Utf8),
                ]).alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            base = pl.concat([mismatch, added, removed, renumber], how="vertical")
            return base.rename({
                "current": f"current_{scope.lower()}",
                "reference": f"reference_{scope.lower()}",
                "severity": f"severity_{scope.lower()}",
                "excel_row": f"excel_row_{scope.lower()}",
            })

        en_view = _scope_view(en_option_diff, en_added_options, en_removed_options, en_code_renumber, "EN")
        if is_en:
            return (
                en_view
                .with_columns([
                    pl.lit("").alias("set_name"),
                    pl.col("current_en").alias("current"),
                    pl.col("reference_en").alias("reference"),
                    pl.col("severity_en").alias("severity"),
                    pl.col("excel_row_en").alias("excel_row"),
                ])
                .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        tgt_view = _scope_view(tgt_option_diff, tgt_added_options, tgt_removed_options, tgt_code_renumber, "TGT")
        keys = ["issue_type", "Q Name", "field"]
        out = en_view.join(tgt_view, on=keys, how="full", suffix="_t")

        return (
            out
            .with_columns([
                pl.coalesce([pl.col("issue_type"), pl.col("issue_type_t")]).alias("issue_type"),
                pl.coalesce([pl.col("Q Name"), pl.col("Q Name_t")]).alias("Q Name"),
                pl.coalesce([pl.col("field"), pl.col("field_t")]).alias("field"),
                pl.lit("").alias("set_name"),
                pl.coalesce([pl.col("current_en"), pl.lit("")]).alias("current"),
                pl.coalesce([pl.col("reference_en"), pl.lit("")]).alias("reference"),
                pl.coalesce([pl.col("current_tgt"), pl.lit("")]).alias("current_lang"),
                pl.coalesce([pl.col("reference_tgt"), pl.lit("")]).alias("reference_lang"),
                pl.when(pl.col("severity_tgt") == "high").then(pl.lit("high"))
                .when(pl.col("severity_en") == "high").then(pl.lit("high"))
                .when(pl.col("severity_tgt") == "medium").then(pl.lit("medium"))
                .when(pl.col("severity_en") == "medium").then(pl.lit("medium"))
                .otherwise(pl.lit("info")).alias("severity"),
                pl.coalesce([pl.col("excel_row_tgt"), pl.col("excel_row_en")]).alias("excel_row"),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "field", "current", "reference",
                "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )
    ```

### `build_option_changes_view._scope_view` {#fn--scope-view-2556}

**Pipeline stage:** `Step 8 Issue unifiers`

**Location:** `scripts/geopoll_validator.py:2556`

**Signature**

```python
def _scope_view(option_diff, added_opts, removed_opts, renumber_opts, scope):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 8 Issue unifiers` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `option_diff` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `added_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `removed_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `renumber_opts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |
| `scope` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 8 Issue unifiers` stage. |

??? note "Function source"

    ```python
    def _scope_view(option_diff, added_opts, removed_opts, renumber_opts, scope):
            mismatch = option_diff.with_columns([
                pl.col("option_label").alias("current"),
                pl.col("option_label_ref").alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            added = added_opts.with_columns([
                pl.col("option_label").alias("current"),
                pl.lit(_not_in_reference_text()).alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            removed = removed_opts.with_columns([
                pl.lit("(removed)").alias("current"),
                pl.col("option_label").alias("reference"),
                pl.lit(None).cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            renumber = renumber_opts.with_columns([
                pl.concat_str([
                    pl.col("new_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label").cast(pl.Utf8),
                ]).alias("current"),
                pl.concat_str([
                    pl.col("old_code").cast(pl.Utf8),
                    pl.lit(") "),
                    pl.col("option_label_ref").cast(pl.Utf8),
                ]).alias("reference"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])

            base = pl.concat([mismatch, added, removed, renumber], how="vertical")
            return base.rename({
                "current": f"current_{scope.lower()}",
                "reference": f"reference_{scope.lower()}",
                "severity": f"severity_{scope.lower()}",
                "excel_row": f"excel_row_{scope.lower()}",
            })
    ```

### `compare_question_presence` {#fn-compare-question-presence-2647}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2647`

**Signature**

```python
def compare_question_presence(current_questions: pl.DataFrame, reference_questions: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Returns (added, removed). Each DataFrame includes `is_optional`.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def compare_question_presence(
        current_questions : pl.DataFrame,
        reference_questions: pl.DataFrame,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Returns (added, removed). Each DataFrame includes `is_optional`.
        """
        key_col = "Q Name"

        added = (
            current_questions.select([key_col])
            .join(reference_questions.select([key_col]), on=key_col, how="anti")
            .with_columns(pl.col(key_col).str.starts_with("o_").alias("is_optional"))
        )

        removed = (
            reference_questions.select([key_col])
            .join(current_questions.select([key_col]), on=key_col, how="anti")
            .with_columns(pl.col(key_col).str.starts_with("o_").alias("is_optional"))
        )

        return added, removed
    ```

### `compare_mandatory` {#fn-compare-mandatory-2671}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2671`

**Signature**

```python
def compare_mandatory(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, treat_blank_as_no: bool=True) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Compares Mandatory column values by Q Name.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `treat_blank_as_no` | positional_or_keyword | No | `True` | `bool` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_mandatory(
        current_questions : pl.DataFrame,
        reference_questions: pl.DataFrame,
        treat_blank_as_no: bool = True,
    ) -> pl.DataFrame:
        """
        Compares Mandatory column values by Q Name.
        """
        if "Mandatory" not in current_questions.columns or "Mandatory" not in reference_questions.columns:
            return pl.DataFrame(schema={
                "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
                "Mandatory": pl.Utf8, "Mandatory_ref": pl.Utf8, "excel_row": pl.Int64,
            })

        joined = (
            current_questions.select(["Q Name", "Mandatory", "excel_row"])
            .join(reference_questions.select(["Q Name", "Mandatory"]), on="Q Name", how="inner", suffix="_ref")
            .with_columns([
                pl.col("Mandatory").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Mandatory"),
                pl.col("Mandatory_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Mandatory_ref"),
            ])
        )

        if treat_blank_as_no:
            joined = joined.with_columns([
                pl.when(pl.col("Mandatory") == "").then(pl.lit("No")).otherwise(pl.col("Mandatory")).alias("Mandatory"),
                pl.when(pl.col("Mandatory_ref") == "").then(pl.lit("No")).otherwise(pl.col("Mandatory_ref")).alias("Mandatory_ref"),
            ])

        return (
            joined
            .filter(normalize_text_expr("Mandatory") != normalize_text_expr("Mandatory_ref"))
            .with_columns([
                pl.lit("mandatory_column_mismatch").alias("issue_type"),
                pl.lit("Mandatory").alias("field"),
            ])
            .select(["issue_type", "Q Name", "field", "Mandatory", "Mandatory_ref", "excel_row"])
        )
    ```

### `_mandatory_cat_expr` {#fn--mandatory-cat-expr-2711}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2711`

**Signature**

```python
def _mandatory_cat_expr(qname_col: str, mandatory_col: str) -> pl.Expr:
```

**Returns:** `pl.Expr`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `qname_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `mandatory_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _mandatory_cat_expr(qname_col: str, mandatory_col: str) -> pl.Expr:
        qn = pl.col(qname_col).cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        md = pl.col(mandatory_col).cast(pl.Utf8).fill_null("").str.strip_chars().str.to_lowercase()
        return (
            pl.when(qn.str.starts_with("o_")).then(pl.lit("optional"))
            .when(md.str.contains("panel")).then(pl.lit("mandatory-panel"))
            .when(md.is_in(["yes", "y", "true", "1"])).then(pl.lit("mandatory"))
            .otherwise(pl.lit("non-mandatory"))
        )
    ```

### `_normalize_qtype_value` {#fn--normalize-qtype-value-2722}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2722`

**Signature**

```python
def _normalize_qtype_value(value: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _normalize_qtype_value(value: str) -> str:
        s = str(value or "").strip().lower()
        if not s:
            return ""
        s = re.sub(r"[\\/_-]+", " ", s)
        s = re.sub(r"\s+", " ", s).strip()
        # Canonical families for stable comparisons.
        if "select all that apply" in s:
            return "select all that apply"
        if "single choice" in s:
            return "single choice"
        return s
    ```

### `_qtype_mode` {#fn--qtype-mode-2736}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2736`

**Signature**

```python
def _qtype_mode(value: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `value` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _qtype_mode(value: str) -> str:
        t = _normalize_qtype_value(value)
        if not t:
            return ""
        if "select all that apply" in t:
            return "multi_select"
        if "single choice" in t:
            return "single_select"
        if is_option_bearing_qtype(t):
            return "option_bearing"
        return "non_option"
    ```

### `_qtype_change_severity` {#fn--qtype-change-severity-2749}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2749`

**Signature**

```python
def _qtype_change_severity(curr_mode: str, ref_mode: str, mandatory_cat: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `curr_mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `ref_mode` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `mandatory_cat` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _qtype_change_severity(curr_mode: str, ref_mode: str, mandatory_cat: str) -> str:
        high_mand = str(mandatory_cat or "") in {"mandatory", "mandatory-panel"}
        modes = {str(curr_mode or ""), str(ref_mode or "")}
        if "single_select" in modes and "multi_select" in modes:
            return "high" if high_mand else "medium"
        if "non_option" in modes and (("single_select" in modes) or ("multi_select" in modes) or ("option_bearing" in modes)):
            return "high"
        if curr_mode != ref_mode:
            return "high" if high_mand else "medium"
        return "high" if high_mand else "medium"
    ```

### `compare_qtype_changes` {#fn-compare-qtype-changes-2761}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2761`

**Signature**

```python
def compare_qtype_changes(current_questions: pl.DataFrame, reference_questions: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Risk-based Q Type comparison:

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def compare_qtype_changes(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Risk-based Q Type comparison:
        - normalises wording to avoid cosmetic false positives
        - escalates severity for mandatory questions and option-bearing mode shifts
        """
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if "Q Type" not in current_questions.columns or "Q Type" not in reference_questions.columns:
            return pl.DataFrame(schema=EMPTY)

        joined = (
            current_questions
            .select(["Q Name", "Q Type", "Mandatory", "excel_row"])
            .join(
                reference_questions.select(["Q Name", "Q Type", "Mandatory"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                pl.col("Q Type").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Type"),
                pl.col("Q Type_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("Q Type_ref"),
                pl.coalesce([pl.col("Mandatory"), pl.col("Mandatory_ref")]).alias("_mand_base"),
            ])
            .with_columns([
                pl.col("Q Type").map_elements(_normalize_qtype_value, return_dtype=pl.Utf8).alias("_type_norm"),
                pl.col("Q Type_ref").map_elements(_normalize_qtype_value, return_dtype=pl.Utf8).alias("_type_norm_ref"),
                pl.col("Q Type").map_elements(_qtype_mode, return_dtype=pl.Utf8).alias("_type_mode"),
                pl.col("Q Type_ref").map_elements(_qtype_mode, return_dtype=pl.Utf8).alias("_type_mode_ref"),
                _mandatory_cat_expr("Q Name", "_mand_base").alias("_mandatory_cat"),
            ])
            .filter(pl.col("_type_norm") != pl.col("_type_norm_ref"))
            .with_columns(
                pl.struct(["_type_mode", "_type_mode_ref", "_mandatory_cat"])
                .map_elements(
                    lambda r: _qtype_change_severity(
                        r.get("_type_mode"),
                        r.get("_type_mode_ref"),
                        r.get("_mandatory_cat"),
                    ),
                    return_dtype=pl.Utf8,
                )
                .alias("severity")
            )
        )
        if joined.height == 0:
            return pl.DataFrame(schema=EMPTY)

        return (
            joined
            .with_columns([
                pl.lit("qtype_changed").alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit("Q Type").alias("field"),
                pl.col("Q Type").alias("current"),
                pl.col("Q Type_ref").alias("reference"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_legacy_text_field_changes` {#fn-compare-legacy-text-field-changes-2827}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2827`

**Signature**

```python
def compare_legacy_text_field_changes(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, column_name: str, issue_type: str, default_severity: str='medium', high_when_mandatory: bool=False) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Legacy column parity checks with normalization to avoid cosmetic false positives.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `column_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `default_severity` | positional_or_keyword | No | `'medium'` | `str` | Severity label used for final issue classification. |
| `high_when_mandatory` | positional_or_keyword | No | `False` | `bool` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_legacy_text_field_changes(
        current_questions: pl.DataFrame,
        reference_questions: pl.DataFrame,
        column_name: str,
        issue_type: str,
        default_severity: str = "medium",
        high_when_mandatory: bool = False,
    ) -> pl.DataFrame:
        """Legacy column parity checks with normalization to avoid cosmetic false positives."""
        EMPTY = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if column_name not in current_questions.columns or column_name not in reference_questions.columns:
            return pl.DataFrame(schema=EMPTY)

        joined = (
            current_questions
            .select(["Q Name", column_name, "Mandatory", "excel_row"])
            .join(
                reference_questions.select(["Q Name", column_name, "Mandatory"]),
                on="Q Name", how="inner", suffix="_ref",
            )
            .with_columns([
                pl.col(column_name).cast(pl.Utf8).fill_null("").str.strip_chars().alias("_curr"),
                pl.col(f"{column_name}_ref").cast(pl.Utf8).fill_null("").str.strip_chars().alias("_ref"),
                pl.coalesce([pl.col("Mandatory"), pl.col("Mandatory_ref")]).alias("_mand_base"),
            ])
            .with_columns([
                normalize_text_expr("_curr").alias("_curr_norm"),
                normalize_text_expr("_ref").alias("_ref_norm"),
                _mandatory_cat_expr("Q Name", "_mand_base").alias("_mandatory_cat"),
            ])
            .filter((pl.col("_curr_norm") != pl.col("_ref_norm")) & ((pl.col("_curr_norm") != "") | (pl.col("_ref_norm") != "")))
        )
        if joined.height == 0:
            return pl.DataFrame(schema=EMPTY)

        if high_when_mandatory:
            joined = joined.with_columns(
                pl.when(pl.col("_mandatory_cat").is_in(["mandatory", "mandatory-panel"]))
                .then(pl.lit("high"))
                .otherwise(pl.lit(default_severity))
                .alias("severity")
            )
        else:
            joined = joined.with_columns(pl.lit(default_severity).alias("severity"))

        return (
            joined
            .with_columns([
                pl.lit(issue_type).alias("issue_type"),
                pl.lit("").alias("set_name"),
                pl.lit(column_name).alias("field"),
                pl.col("_curr").alias("current"),
                pl.col("_ref").alias("reference"),
            ])
            .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
        )
    ```

### `compare_question_labels_single` {#fn-compare-question-labels-single-2889}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2889`

**Signature**

```python
def compare_question_labels_single(current_questions: pl.DataFrame, reference_questions: pl.DataFrame, current_text_col: str, reference_text_col: str, lang_scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Question stem (text label) changes for matching Q Name in one language scope.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `current_text_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_text_col` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_question_labels_single(
        current_questions : pl.DataFrame,
        reference_questions: pl.DataFrame,
        current_text_col: str,
        reference_text_col: str,
        lang_scope: str,
    ) -> pl.DataFrame:
        """
        Question stem (text label) changes for matching Q Name in one language scope.
        Numbered option blocks are removed so option labels are handled only in Option Changes.
        """
        if current_text_col not in current_questions.columns or reference_text_col not in reference_questions.columns:
            return pl.DataFrame(schema={
                "issue_type": pl.Utf8,
                "Q Name": pl.Utf8,
                "field": pl.Utf8,
                "current": pl.Utf8,
                "reference": pl.Utf8,
                "severity": pl.Utf8,
                "excel_row": pl.Int64,
                "lang_scope": pl.Utf8,
            })

        return (
            current_questions
            .select([
                "Q Name",
                "excel_row",
                pl.col(current_text_col).alias("_curr_text"),
            ])
            .join(
                reference_questions.select([
                    "Q Name",
                    pl.col(reference_text_col).alias("_ref_text"),
                ]),
                on="Q Name",
                how="inner",
            )
            .with_columns([
                pl.col("_curr_text")
                .map_elements(extract_question_stem, return_dtype=pl.Utf8)
                .fill_null("")
                .str.strip_chars()
                .alias("current"),
                pl.col("_ref_text")
                .map_elements(extract_question_stem, return_dtype=pl.Utf8)
                .fill_null("")
                .str.strip_chars()
                .alias("reference"),
            ])
            .with_columns([
                normalize_text_expr("current").alias("_current_norm"),
                normalize_text_expr("reference").alias("_reference_norm"),
            ])
            .filter(pl.col("_current_norm") != pl.col("_reference_norm"))
            .with_columns([
                pl.lit("question_label_mismatch").alias("issue_type"),
                pl.lit("label").alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
                pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
            ])
            .select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row", "lang_scope"])
        )
    ```

### `build_question_changes_view` {#fn-build-question-changes-view-2955}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2955`

**Signature**

```python
def build_question_changes_view(core_question_issues: pl.DataFrame, en_label_diff: pl.DataFrame, tgt_label_diff: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Builds Question Changes rows with independent EN and target-language label checks.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `core_question_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `en_label_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `tgt_label_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def build_question_changes_view(
        core_question_issues: pl.DataFrame,
        en_label_diff: pl.DataFrame,
        tgt_label_diff: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """
        Builds Question Changes rows with independent EN and target-language label checks.

        Layout policy:
        - Current value / Reference / rule are always EN baseline.
        - For non-EN runs, target language values are added in separate columns.
        """
        is_en = str(target_lang).upper() == "EN"

        if is_en:
            label_view = (
                en_label_diff
                .with_columns([
                    pl.lit("").alias("set_name"),
                    pl.col("current").cast(pl.Utf8).fill_null("").alias("current"),
                    pl.col("reference").cast(pl.Utf8).fill_null("").alias("reference"),
                    pl.col("severity").cast(pl.Utf8).fill_null("info").alias("severity"),
                    pl.col("excel_row").cast(pl.Int64).alias("excel_row"),
                ])
                .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

            core_view = (
                core_question_issues
                .with_columns([
                    pl.col("set_name").cast(pl.Utf8).fill_null("").alias("set_name"),
                    pl.col("field").cast(pl.Utf8).fill_null("").alias("field"),
                    pl.col("current").cast(pl.Utf8).fill_null("").alias("current"),
                    pl.col("reference").cast(pl.Utf8).fill_null("").alias("reference"),
                    pl.col("severity").cast(pl.Utf8).fill_null("info").alias("severity"),
                    pl.col("excel_row").cast(pl.Int64),
                ])
                .select(["issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )
            return pl.concat([core_view, label_view], how="vertical")

        def _scope_view(label_diff: pl.DataFrame, scope: str) -> pl.DataFrame:
            return (
                label_diff
                .rename({
                    "current": f"current_{scope.lower()}",
                    "reference": f"reference_{scope.lower()}",
                    "severity": f"severity_{scope.lower()}",
                    "excel_row": f"excel_row_{scope.lower()}",
                })
                .select([
                    "issue_type", "Q Name", "field",
                    f"current_{scope.lower()}", f"reference_{scope.lower()}",
                    f"severity_{scope.lower()}", f"excel_row_{scope.lower()}",
                ])
            )

        en_view = _scope_view(en_label_diff, "EN")
        tgt_view = _scope_view(tgt_label_diff, "TGT")
        keys = ["issue_type", "Q Name", "field"]
        out = en_view.join(tgt_view, on=keys, how="full", suffix="_t")
        label_view = (
            out
            .with_columns([
                pl.coalesce([pl.col("issue_type"), pl.col("issue_type_t")]).alias("issue_type"),
                pl.coalesce([pl.col("Q Name"), pl.col("Q Name_t")]).alias("Q Name"),
                pl.coalesce([pl.col("field"), pl.col("field_t")]).alias("field"),
                pl.lit("").alias("set_name"),
                # EN baseline in primary columns
                pl.coalesce([pl.col("current_en"), pl.lit("")]).alias("current"),
                pl.coalesce([pl.col("reference_en"), pl.lit("")]).alias("reference"),
                # Target language shown in dedicated columns
                pl.coalesce([pl.col("current_tgt"), pl.lit("")]).alias("current_lang"),
                pl.coalesce([pl.col("reference_tgt"), pl.lit("")]).alias("reference_lang"),
                pl.when(pl.col("severity_tgt") == "high").then(pl.lit("high"))
                .when(pl.col("severity_en") == "high").then(pl.lit("high"))
                .when(pl.col("severity_tgt") == "medium").then(pl.lit("medium"))
                .when(pl.col("severity_en") == "medium").then(pl.lit("medium"))
                .otherwise(pl.lit("info")).alias("severity"),
                pl.coalesce([pl.col("excel_row_tgt"), pl.col("excel_row_en")]).alias("excel_row"),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "field", "current", "reference",
                "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )

        core_view = (
            core_question_issues
            .with_columns([
                pl.col("set_name").cast(pl.Utf8).fill_null("").alias("set_name"),
                pl.col("field").cast(pl.Utf8).fill_null("").alias("field"),
                pl.col("current").cast(pl.Utf8).fill_null("").alias("current"),
                pl.col("reference").cast(pl.Utf8).fill_null("").alias("reference"),
                pl.lit("").alias("current_lang"),
                pl.lit("").alias("reference_lang"),
                pl.col("severity").cast(pl.Utf8).fill_null("info").alias("severity"),
                pl.col("excel_row").cast(pl.Int64),
            ])
            .select([
                "issue_type", "set_name", "Q Name", "field", "current", "reference",
                "current_lang", "reference_lang", "severity", "excel_row",
            ])
        )

        return pl.concat([core_view, label_view], how="vertical")
    ```

### `build_question_changes_view._scope_view` {#fn--scope-view-2997}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:2997`

**Signature**

```python
def _scope_view(label_diff: pl.DataFrame, scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label_diff` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `scope` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _scope_view(label_diff: pl.DataFrame, scope: str) -> pl.DataFrame:
            return (
                label_diff
                .rename({
                    "current": f"current_{scope.lower()}",
                    "reference": f"reference_{scope.lower()}",
                    "severity": f"severity_{scope.lower()}",
                    "excel_row": f"excel_row_{scope.lower()}",
                })
                .select([
                    "issue_type", "Q Name", "field",
                    f"current_{scope.lower()}", f"reference_{scope.lower()}",
                    f"severity_{scope.lower()}", f"excel_row_{scope.lower()}",
                ])
            )
    ```

### `compare_option_labels_single` {#fn-compare-option-labels-single-3064}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3064`

**Signature**

```python
def compare_option_labels_single(current_options: pl.DataFrame, reference_options: pl.DataFrame, lang_scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Option label changes for matching Q Name + option_code.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_labels_single(
        current_options : pl.DataFrame,
        reference_options: pl.DataFrame,
        lang_scope: str,
    ) -> pl.DataFrame:
        """
        Option label changes for matching Q Name + option_code.
        """
        return (
            current_options
            .join(reference_options, on=["Q Name", "option_code"], how="inner", suffix="_ref")
            .with_columns([
                normalize_text_expr("option_label").alias("option_label_norm"),
                normalize_text_expr("option_label_ref").alias("option_label_ref_norm"),
            ])
            .filter(pl.col("option_label_norm") != pl.col("option_label_ref_norm"))
            .with_columns([
                pl.lit("option_label_mismatch").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_code").cast(pl.Utf8)]).alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "field", "option_label", "option_label_ref", "severity", "excel_row", "lang_scope"])
        )
    ```

### `compare_option_presence_single` {#fn-compare-option-presence-single-3090}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3090`

**Signature**

```python
def compare_option_presence_single(current_options: pl.DataFrame, reference_options: pl.DataFrame, lang_scope: str) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Added/removed options for one language scope.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_presence_single(
        current_options : pl.DataFrame,
        reference_options: pl.DataFrame,
        lang_scope: str,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """
        Added/removed options for one language scope.
        """
        key_cols = ["Q Name", "option_code"]

        removed_options = (
            reference_options.select(key_cols + ["option_label"])
            .join(current_options.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("removed_option").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_code").cast(pl.Utf8)]).alias("field"),
                pl.lit("high").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "field", "option_label", "severity", "lang_scope"])
        )

        added_options = (
            current_options.select(key_cols + ["option_label"])
            .join(reference_options.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("added_option").alias("issue_type"),
                pl.concat_str([pl.lit("option_"), pl.col("option_code").cast(pl.Utf8)]).alias("field"),
                pl.lit("medium").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select(["issue_type", "Q Name", "field", "option_label", "severity", "lang_scope"])
        )

        return added_options, removed_options
    ```

### `compare_option_code_renumber_single` {#fn-compare-option-code-renumber-single-3127}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3127`

**Signature**

```python
def compare_option_code_renumber_single(current_options: pl.DataFrame, reference_options: pl.DataFrame, lang_scope: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Detect explicit option-position renumbering for the same normalized label

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `reference_options` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `lang_scope` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def compare_option_code_renumber_single(
        current_options: pl.DataFrame,
        reference_options: pl.DataFrame,
        lang_scope: str,
    ) -> pl.DataFrame:
        """
        Detect explicit option-position renumbering for the same normalized label
        within the same question: e.g., position 12 becomes 15.

        We only emit when label->code mapping is 1:1 on both sides to avoid
        ambiguous many-to-many matches.
        """
        cur = (
            current_options
            .with_columns(normalize_text_expr("option_label").alias("label_norm"))
            .filter(pl.col("label_norm") != "")
            .group_by(["Q Name", "label_norm"])
            .agg([
                pl.col("option_code").n_unique().alias("cur_n_codes"),
                pl.col("option_code").first().alias("new_code"),
                pl.col("option_label").first().alias("option_label"),
                pl.col("excel_row").min().alias("excel_row"),
            ])
        )

        ref = (
            reference_options
            .with_columns(normalize_text_expr("option_label").alias("label_norm"))
            .filter(pl.col("label_norm") != "")
            .group_by(["Q Name", "label_norm"])
            .agg([
                pl.col("option_code").n_unique().alias("ref_n_codes"),
                pl.col("option_code").first().alias("old_code"),
                pl.col("option_label").first().alias("option_label_ref"),
            ])
        )

        return (
            cur.join(ref, on=["Q Name", "label_norm"], how="inner")
            .filter(
                (pl.col("cur_n_codes") == 1)
                & (pl.col("ref_n_codes") == 1)
                & (pl.col("new_code") != pl.col("old_code"))
            )
            .with_columns([
                pl.lit("option_position_renumbered_same_label").alias("issue_type"),
                pl.concat_str([
                    pl.lit("position_"),
                    pl.col("old_code").cast(pl.Utf8),
                    pl.lit("_to_"),
                    pl.col("new_code").cast(pl.Utf8),
                ]).alias("field"),
                pl.lit("high").alias("severity"),
                pl.lit(lang_scope).alias("lang_scope"),
            ])
            .select([
                "issue_type", "Q Name", "field",
                "old_code", "new_code",
                "option_label", "option_label_ref",
                "severity", "excel_row", "lang_scope",
            ])
        )
    ```

### `compare_codes_presence_single` {#fn-compare-codes-presence-single-3191}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3191`

**Signature**

```python
def compare_codes_presence_single(current_codes: pl.DataFrame, reference_codes: pl.DataFrame) -> tuple[pl.DataFrame, pl.DataFrame]:
```

**Returns:** `tuple[pl.DataFrame, pl.DataFrame]`

**What it does:** Added/removed numeric code entries in the survey 'Codes' column.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_codes_presence_single(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
    ) -> tuple[pl.DataFrame, pl.DataFrame]:
        """Added/removed numeric code entries in the survey 'Codes' column."""
        key_cols = ["Q Name", "code_num"]

        removed_codes = (
            reference_codes.select(key_cols + ["code_token"])
            .join(current_codes.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("codes_col_removed").alias("issue_type"),
                pl.concat_str([pl.lit("codes_"), pl.col("code_num").cast(pl.Utf8)]).alias("field"),
                pl.lit("high").alias("severity"),
            ])
            .select(["issue_type", "Q Name", "field", "code_num", "code_token", "severity"])
        )

        added_codes = (
            current_codes.select(key_cols + ["code_token", "excel_row"])
            .join(reference_codes.select(key_cols), on=key_cols, how="anti")
            .with_columns([
                pl.lit("codes_col_added").alias("issue_type"),
                pl.concat_str([pl.lit("codes_"), pl.col("code_num").cast(pl.Utf8)]).alias("field"),
                pl.lit("medium").alias("severity"),
            ])
            .select(["issue_type", "Q Name", "field", "code_num", "code_token", "severity", "excel_row"])
        )

        return added_codes, removed_codes
    ```

### `compare_codes_token_mismatch_single` {#fn-compare-codes-token-mismatch-single-3223}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3223`

**Signature**

```python
def compare_codes_token_mismatch_single(current_codes: pl.DataFrame, reference_codes: pl.DataFrame, renumber_codes: pl.DataFrame | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Same code number exists in both, but token text differs in 'Codes' column.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `renumber_codes` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_codes_token_mismatch_single(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
        renumber_codes: pl.DataFrame | None = None,
    ) -> pl.DataFrame:
        """
        Same code number exists in both, but token text differs in 'Codes' column.

        Precedence rule:
        - If a code position is already explained by a same-token renumber event
          (old_code_num->new_code_num) for the same Q Name, suppress token-mismatch
          rows on those positions to avoid double-reporting reorder as rename.
        """
        mismatch = (
            current_codes
            .join(reference_codes, on=["Q Name", "code_num"], how="inner", suffix="_ref")
            .with_columns([
                normalize_code_token_expr("code_token").alias("code_token_norm"),
                normalize_code_token_expr("code_token_ref").alias("code_token_ref_norm"),
            ])
            .filter(pl.col("code_token_norm") != pl.col("code_token_ref_norm"))
            .with_columns([
                pl.lit("codes_col_token_mismatch").alias("issue_type"),
                pl.concat_str([pl.lit("codes_"), pl.col("code_num").cast(pl.Utf8)]).alias("field"),
                pl.lit("high").alias("severity"),
            ])
            .select([
                "issue_type", "Q Name", "field", "code_num",
                "code_token", "code_token_ref", "severity", "excel_row",
            ])
        )

        if renumber_codes is None or renumber_codes.height == 0:
            return mismatch

        renumber_positions = (
            pl.concat([
                renumber_codes.select([
                    pl.col("Q Name"),
                    pl.col("old_code_num").cast(pl.Int64).alias("code_num"),
                ]),
                renumber_codes.select([
                    pl.col("Q Name"),
                    pl.col("new_code_num").cast(pl.Int64).alias("code_num"),
                ]),
            ], how="vertical")
            .unique()
        )

        return mismatch.join(renumber_positions, on=["Q Name", "code_num"], how="anti")
    ```

### `compare_codes_renumber_single` {#fn-compare-codes-renumber-single-3275}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3275`

**Signature**

```python
def compare_codes_renumber_single(current_codes: pl.DataFrame, reference_codes: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Detect same normalized code token moved to a different number in 'Codes'.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `reference_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def compare_codes_renumber_single(
        current_codes: pl.DataFrame,
        reference_codes: pl.DataFrame,
    ) -> pl.DataFrame:
        """
        Detect same normalized code token moved to a different number in 'Codes'.
        Emits only 1:1 token->number mappings to avoid ambiguous many-to-many cases.
        """
        cur = (
            current_codes
            .with_columns(normalize_code_token_expr("code_token").alias("token_norm"))
            .filter(pl.col("token_norm") != "")
            .group_by(["Q Name", "token_norm"])
            .agg([
                pl.col("code_num").n_unique().alias("cur_n_nums"),
                pl.col("code_num").first().alias("new_code_num"),
                pl.col("code_token").first().alias("code_token"),
                pl.col("excel_row").min().alias("excel_row"),
            ])
        )

        ref = (
            reference_codes
            .with_columns(normalize_code_token_expr("code_token").alias("token_norm"))
            .filter(pl.col("token_norm") != "")
            .group_by(["Q Name", "token_norm"])
            .agg([
                pl.col("code_num").n_unique().alias("ref_n_nums"),
                pl.col("code_num").first().alias("old_code_num"),
                pl.col("code_token").first().alias("code_token_ref"),
            ])
        )

        return (
            cur.join(ref, on=["Q Name", "token_norm"], how="inner")
            .filter(
                (pl.col("cur_n_nums") == 1)
                & (pl.col("ref_n_nums") == 1)
                & (pl.col("new_code_num") != pl.col("old_code_num"))
            )
            .with_columns([
                pl.lit("codes_col_renumbered_same_token").alias("issue_type"),
                pl.concat_str([
                    pl.lit("codes_"),
                    pl.col("old_code_num").cast(pl.Utf8),
                    pl.lit("_to_"),
                    pl.col("new_code_num").cast(pl.Utf8),
                ]).alias("field"),
                pl.lit("high").alias("severity"),
            ])
            .select([
                "issue_type", "Q Name", "field",
                "old_code_num", "new_code_num",
                "code_token", "code_token_ref",
                "severity", "excel_row",
            ])
        )
    ```

### `build_codes_changes_view` {#fn-build-codes-changes-view-3334}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3334`

**Signature**

```python
def build_codes_changes_view(token_mismatch: pl.DataFrame, added_codes: pl.DataFrame, removed_codes: pl.DataFrame, renumber_codes: pl.DataFrame, target_lang: str) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Converts Codes-column checks to the common Option Changes view schema.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `token_mismatch` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `added_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `removed_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `renumber_codes` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `target_lang` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def build_codes_changes_view(
        token_mismatch: pl.DataFrame,
        added_codes: pl.DataFrame,
        removed_codes: pl.DataFrame,
        renumber_codes: pl.DataFrame,
        target_lang: str,
    ) -> pl.DataFrame:
        """Converts Codes-column checks to the common Option Changes view schema."""
        rows = []

        if token_mismatch.height > 0:
            rows.append(
                token_mismatch.with_columns([
                    pl.col("code_token").alias("current"),
                    pl.col("code_token_ref").alias("reference"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if added_codes.height > 0:
            rows.append(
                added_codes.with_columns([
                    pl.col("code_token").alias("current"),
                    pl.lit(_not_in_reference_text("Codes")).alias("reference"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if removed_codes.height > 0:
            rows.append(
                removed_codes.with_columns([
                    pl.lit("(removed from Codes)").alias("current"),
                    pl.col("code_token").alias("reference"),
                    pl.lit(None).cast(pl.Int64).alias("excel_row"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if renumber_codes.height > 0:
            rows.append(
                renumber_codes.with_columns([
                    pl.concat_str([
                        pl.col("new_code_num").cast(pl.Utf8), pl.lit(") "), pl.col("code_token")
                    ]).alias("current"),
                    pl.concat_str([
                        pl.col("old_code_num").cast(pl.Utf8), pl.lit(") "), pl.col("code_token_ref")
                    ]).alias("reference"),
                ]).select(["issue_type", "Q Name", "field", "current", "reference", "severity", "excel_row"])
            )

        if rows:
            base = pl.concat(rows, how="vertical")
        else:
            base = pl.DataFrame(schema={
                "issue_type": pl.Utf8, "Q Name": pl.Utf8, "field": pl.Utf8,
                "current": pl.Utf8, "reference": pl.Utf8,
                "severity": pl.Utf8, "excel_row": pl.Int64,
            })

        if str(target_lang).upper() == "EN":
            return base.with_columns(pl.lit("").alias("set_name")).select([
                "issue_type", "set_name", "Q Name", "field", "current", "reference", "severity", "excel_row"
            ])

        return base.with_columns([
            pl.lit("").alias("set_name"),
            pl.lit("").alias("current_lang"),
            pl.lit("").alias("reference_lang"),
        ]).select([
            "issue_type", "set_name", "Q Name", "field", "current", "reference",
            "current_lang", "reference_lang", "severity", "excel_row",
        ])
    ```

### `validate_critical_sets` {#fn-validate-critical-sets-3409}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3409`

**Signature**

```python
def validate_critical_sets(questions_df: pl.DataFrame, exact_sets: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Checks that each critical question group is fully present with the expected

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `exact_sets` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_critical_sets(
        questions_df: pl.DataFrame,
        exact_sets  : dict,
    ) -> pl.DataFrame:
        """
        Checks that each critical question group is fully present with the expected
        Mandatory value. Rules come from critical_sets.yaml -> exact_sets.

        required=true  -> missing = issue_type 'missing_critical_question', severity HIGH
        required=false -> missing = issue_type 'advisory_question',          severity MEDIUM
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }

        if not exact_sets:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        if "Mandatory_norm" not in questions_df.columns:
            questions_df = questions_df.with_columns(
                normalize_mandatory_expr("Mandatory").alias("Mandatory_norm")
            )

        present_qnames = set(questions_df["Q Name"].to_list())
        issues = []

        for set_name, rules in exact_sets.items():
            required_names   = [r["q_name"] for r in rules if r.get("required", True)]
            present_in_set   = [r["q_name"] for r in rules if r["q_name"] in present_qnames]
            present_required = [q for q in required_names if q in present_qnames]

            if 0 < len(present_required) < len(required_names):
                issues.append({
                    "issue_type": "partial_critical_set",
                    "set_name"  : set_name, "Q Name": "",
                    "field"     : "Q Name",
                    "current"   : ", ".join(sorted(present_in_set)),
                    "reference" : f"Expected all {len(required_names)} required questions",
                    "severity"  : "high", "excel_row": None,
                })

            for rule in rules:
                q_name   = rule["q_name"]
                expected = rule.get("expected_mandatory", "")
                required = rule.get("required", True)

                if q_name not in present_qnames:
                    issues.append({
                        "issue_type": "missing_critical_question" if required else "advisory_question",
                        "set_name"  : set_name, "Q Name": q_name,
                        "field"     : "Q Name", "current": "",
                        "reference" : "present",
                        "severity"  : "high" if required else "medium",
                        "excel_row" : None,
                    })
                    continue

                if not expected:
                    continue

                row = (
                    questions_df
                    .filter(pl.col("Q Name") == q_name)
                    .select(["Q Name", "Mandatory", "Mandatory_norm", "excel_row"])
                    .to_dicts()
                )
                if not row:
                    continue
                row = row[0]
                if row["Mandatory_norm"] != expected:
                    issues.append({
                        "issue_type": "critical_mandatory_mismatch",
                        "set_name"  : set_name, "Q Name": q_name,
                        "field"     : "Mandatory",
                        "current"   : row["Mandatory"], "reference": expected,
                        "severity"  : "high", "excel_row": row.get("excel_row"),
                    })

        if not issues:
            return pl.DataFrame(schema=EMPTY_SCHEMA)
        return pl.DataFrame(issues)
    ```

### `validate_prefix_counts` {#fn-validate-prefix-counts-3494}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3494`

**Signature**

```python
def validate_prefix_counts(current_questions: pl.DataFrame, min_count_sets: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Checks that questions with a given prefix appear at least min_count times.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `min_count_sets` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_prefix_counts(
        current_questions: pl.DataFrame,
        min_count_sets   : dict,
    ) -> pl.DataFrame:
        """
        Checks that questions with a given prefix appear at least min_count times.
        Covers CS groups (cs_stress_*, cs_crisis_*, cs_emergency_*) and HDDS count.
        Rules come from critical_sets.yaml -> min_count_sets.
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not min_count_sets:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        all_qnames = current_questions["Q Name"].to_list()
        issues = []
        for set_name, rule in min_count_sets.items():
            prefix    = rule.get("prefix", "")
            min_count = rule.get("min_count", 1)
            desc      = rule.get("description", f"At least {min_count} '{prefix}*' questions required")
            matched   = sorted(q for q in all_qnames if q.startswith(prefix))
            if len(matched) < min_count:
                found_str = f"{len(matched)} found" + (f": {', '.join(matched)}" if matched else " (none)")
                issues.append({
                    "issue_type": "below_minimum_count", "set_name": set_name, "Q Name": "",
                    "field": "count", "current": found_str, "reference": desc,
                    "severity": "high", "excel_row": None,
                })

        if not issues:
            return pl.DataFrame(schema=EMPTY_SCHEMA)
        return pl.DataFrame(issues)
    ```

### `validate_crop_harvest` {#fn-validate-crop-harvest-3531}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3531`

**Signature**

```python
def validate_crop_harvest(current_questions: pl.DataFrame, crop_rules: dict) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Questionnaire must contain EITHER only the minimal set OR all questions in

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_rules` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def validate_crop_harvest(
        current_questions: pl.DataFrame,
        crop_rules       : dict,
    ) -> pl.DataFrame:
        """
        Questionnaire must contain EITHER only the minimal set OR all questions in
        the full set. Rules come from critical_sets.yaml -> crop_harvest.
        """
        EMPTY_SCHEMA = {
            "issue_type": pl.Utf8, "set_name": pl.Utf8, "Q Name": pl.Utf8,
            "field": pl.Utf8, "current": pl.Utf8, "reference": pl.Utf8,
            "severity": pl.Utf8, "excel_row": pl.Int64,
        }
        if not crop_rules:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        minimal = set(crop_rules.get("minimal", []))
        full    = set(crop_rules.get("full", []))
        if not minimal and not full:
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        all_qnames     = set(current_questions["Q Name"].to_list())
        relevant_found = {q for q in all_qnames if q in full or q in minimal}

        if relevant_found == minimal or full.issubset(all_qnames):
            return pl.DataFrame(schema=EMPTY_SCHEMA)

        issues = [{
            "issue_type": "crop_harvest_violation", "set_name": "CRP_HARV", "Q Name": "",
            "field": "Q Name",
            "current"  : f"found: {', '.join(sorted(relevant_found)) or 'none'}",
            "reference": f"either only [{', '.join(sorted(minimal))}] OR all of [{', '.join(sorted(full))}]",
            "severity" : "high", "excel_row": None,
        }]
        return pl.DataFrame(issues)
    ```

### `_tick` {#fn--tick-3576}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3576`

**Signature**

```python
def _tick(label: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `label` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _tick(label: str):
        global _t_prev
        _now = time.perf_counter()
        print(f"[timing] {label:<34} {_now - _t_prev:8.3f}s", flush=True)
        _t_prev = _now
    ```

### `_add_issue_reason` {#fn--add-issue-reason-3760}

**Pipeline stage:** `Step 9 Run the full pipeline`

**Location:** `scripts/geopoll_validator.py:3760`

**Signature**

```python
def _add_issue_reason(_df: pl.DataFrame, _reason: str) -> None:
```

**Returns:** `None`

**What it does:** Implements logic in the `Step 9 Run the full pipeline` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 9 Run the full pipeline` stage. |
| `_reason` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 9 Run the full pipeline` stage. |

??? note "Function source"

    ```python
    def _add_issue_reason(_df: pl.DataFrame, _reason: str) -> None:
        if _df is None or _df.height == 0 or "Q Name" not in _df.columns:
            return
        for _q in _df["Q Name"].drop_nulls().to_list():
            _q = str(_q).strip()
            if not _q:
                continue
            skip_option_issue_reasons.setdefault(_q, set()).add(_reason)
    ```

### `_header_row` {#fn--header-row-4127}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4127`

**Signature**

```python
def _header_row(ws, row, values):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `values` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _header_row(ws, row, values):
        for col, val in enumerate(values, 1):
            c = ws.cell(row=row, column=col, value=val)
            c.fill = FILL_HEADER; c.font = FONT_HEADER
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.row_dimensions[row].height = 18
    ```

### `_section_header` {#fn--section-header-4134}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4134`

**Signature**

```python
def _section_header(ws, row, title, n_cols):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `title` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `n_cols` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _section_header(ws, row, title, n_cols):
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=n_cols)
        c = ws.cell(row=row, column=1, value=title)
        c.fill = FILL_SECTION; c.font = FONT_SECTION
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[row].height = 20
    ```

### `_data_row` {#fn--data-row-4141}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4141`

**Signature**

```python
def _data_row(ws, row, n_cols, severity='', fill=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `n_cols` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `severity` | positional_or_keyword | No | `''` | `-` | Severity label used for final issue classification. |
| `fill` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _data_row(ws, row, n_cols, severity="", fill=None):
        use_fill = fill or SEVERITY_FILL.get(severity)
        for col in range(1, n_cols + 1):
            c = ws.cell(row=row, column=col)
            c.font = FONT_NORMAL; c.border = THIN_BORDER
            c.alignment = Alignment(vertical="top", wrap_text=True)
            if use_fill:
                c.fill = use_fill
    ```

### `_autofit` {#fn--autofit-4150}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4150`

**Signature**

```python
def _autofit(ws, mn=12, mx=55):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `mn` | positional_or_keyword | No | `12` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `mx` | positional_or_keyword | No | `55` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _autofit(ws, mn=12, mx=55):
        for col_cells in ws.columns:
            w = max((len(str(c.value)) if c.value else 0) for c in col_cells)
            ws.column_dimensions[get_column_letter(col_cells[0].column)].width = min(max(w + 2, mn), mx)
    ```

### `_action_for_issue_type` {#fn--action-for-issue-type-4195}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4195`

**Signature**

```python
def _action_for_issue_type(issue_type: str) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_type` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _action_for_issue_type(issue_type: str) -> str:
        key = str(issue_type or "").strip()
        return ISSUE_ACTION_MAP.get(key, "Review issue details")
    ```

### `_issues_col_map` {#fn--issues-col-map-4200}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4200`

**Signature**

```python
def _issues_col_map():
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

No parameters.

??? note "Function source"

    ```python
    def _issues_col_map():
        lang_code = str(globals().get("target_lang", "")).upper().strip()
        lang_label = lang_code if (lang_code and lang_code != "EN") else "Language"
        return [
            ("issue_type",    "Issue type"),
            ("mandatory_cat", "Type"),
            ("set_name",      "Set"),
            ("Q Name",        "Q Name"),
            ("field",         "Field"),
            ("current",       "Current value"),
            ("reference",     "Reference / rule"),
            ("current_lang",    f"Current value ({lang_label})"),
            ("reference_lang",  f"Reference / rule ({lang_label})"),
            ("current_en",    "Current value (EN)"),
            ("reference_en",  "Reference / rule (EN)"),
            ("action",        "Action"),
            ("severity",      "Severity"),
            ("excel_row",     "Excel row"),
        ]
    ```

### `_issues_table` {#fn--issues-table-4221}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4221`

**Signature**

```python
def _issues_table(ws, start_row, df):
```

**Returns:** `None or implicit return`

**What it does:** Renders a header + data table. Only columns present in df are shown.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _issues_table(ws, start_row, df):
        """Renders a header + data table. Only columns present in df are shown."""
        if "issue_type" in df.columns and "action" not in df.columns:
            df = df.with_columns(
                pl.col("issue_type")
                .map_elements(_action_for_issue_type, return_dtype=pl.Utf8)
                .alias("action")
            )
        cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        _header_row(ws, start_row, [d for _, d in cols])
        r = start_row + 1
        if df.height == 0:
            c = ws.cell(row=r, column=1, value="No issues in this category")
            c.font = Font(bold=True, color="274E13", size=10)
            return r + 2
        for row_data in df.to_dicts():
            for col, (src, _) in enumerate(cols, 1):
                ws.cell(row=r, column=col, value=row_data.get(src))
            _data_row(ws, r, len(cols), row_data.get("severity", ""))
            r += 1
        ws.freeze_panes = f"A{start_row + 1}"
        ws.auto_filter.ref = f"A{start_row}:{get_column_letter(len(cols))}{start_row}"
        return r + 1
    ```

### `_tokenize_for_word_diff` {#fn--tokenize-for-word-diff-4257}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4257`

**Signature**

```python
def _tokenize_for_word_diff(text: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _tokenize_for_word_diff(text: str):
        raw = re.findall(r"\s+|\S+", text)
        out = []
        for tok in raw:
            if tok.isspace() and out:
                out[-1] = out[-1] + tok
            else:
                out.append(tok)
        return out
    ```

### `_coalesce_segments` {#fn--coalesce-segments-4268}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4268`

**Signature**

```python
def _coalesce_segments(parts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `parts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _coalesce_segments(parts):
        merged = []
        for txt, is_equal in parts:
            if not txt:
                continue
            if merged and merged[-1][1] == is_equal:
                merged[-1] = (merged[-1][0] + txt, is_equal)
            else:
                merged.append((txt, is_equal))
        return merged
    ```

### `_build_diff_segments` {#fn--build-diff-segments-4280}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4280`

**Signature**

```python
def _build_diff_segments(current_text: str, reference_text: str):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `reference_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _build_diff_segments(current_text: str, reference_text: str):
        a = _tokenize_for_word_diff(current_text)
        b = _tokenize_for_word_diff(reference_text)
        sm = difflib.SequenceMatcher(a=a, b=b)
        current_parts, reference_parts = [], []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                current_parts.append(("".join(a[i1:i2]), True))
                reference_parts.append(("".join(b[j1:j2]), True))
            elif tag == "replace":
                current_parts.append(("".join(a[i1:i2]), False))
                reference_parts.append(("".join(b[j1:j2]), False))
            elif tag == "delete":
                current_parts.append(("".join(a[i1:i2]), False))
            elif tag == "insert":
                reference_parts.append(("".join(b[j1:j2]), False))
        return _coalesce_segments(current_parts), _coalesce_segments(reference_parts)
    ```

### `_set_rich_text` {#fn--set-rich-text-4299}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4299`

**Signature**

```python
def _set_rich_text(cell, full_text: str, parts):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `cell` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `full_text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `parts` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _set_rich_text(cell, full_text: str, parts):
        if not _RICH_TEXT_AVAILABLE:
            cell.value = full_text
            return
        blocks = []
        for txt, is_equal in parts:
            if not txt:
                continue
            color = "FF000000" if is_equal else "FFFF0000"
            blocks.append(TextBlock(InlineFont(color=color), txt))
        if not blocks:
            cell.value = full_text
            return
        cell.value = CellRichText(*blocks)
    ```

### `_apply_inline_diff_for_issue` {#fn--apply-inline-diff-for-issue-4315}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4315`

**Signature**

```python
def _apply_inline_diff_for_issue(ws, start_row, df, issue_types):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `start_row` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `issue_types` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _apply_inline_diff_for_issue(ws, start_row, df, issue_types):
        if df.height == 0:
            return

        cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        cidx = {src: i for i, (src, _) in enumerate(cols, start=1)}

        _allowed = set(issue_types or [])

        def _match_issue(issue_val: str) -> bool:
            for allowed in _allowed:
                if isinstance(allowed, str) and allowed.endswith("*"):
                    if issue_val.startswith(allowed[:-1]):
                        return True
                elif issue_val == allowed:
                    return True
            return False

        compare_pairs = [("current", "reference")]
        if "current_lang" in cidx and "reference_lang" in cidx:
            compare_pairs.append(("current_lang", "reference_lang"))
        if "current_en" in cidx and "reference_en" in cidx:
            compare_pairs.append(("current_en", "reference_en"))

        for offset, rd in enumerate(df.to_dicts(), start=1):
            issue_val = str(rd.get("issue_type") or "")
            if not _match_issue(issue_val):
                continue

            for cur_key, ref_key in compare_pairs:
                cur_txt = str(rd.get(cur_key) or "")
                ref_txt = str(rd.get(ref_key) or "")
                if cur_txt == ref_txt:
                    continue
                cur_parts, ref_parts = _build_diff_segments(cur_txt, ref_txt)
                _set_rich_text(ws.cell(row=start_row + offset, column=cidx[cur_key]), cur_txt, cur_parts)
                _set_rich_text(ws.cell(row=start_row + offset, column=cidx[ref_key]), ref_txt, ref_parts)
    ```

### `_apply_inline_diff_for_issue._match_issue` {#fn--match-issue-4324}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4324`

**Signature**

```python
def _match_issue(issue_val: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `issue_val` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _match_issue(issue_val: str) -> bool:
            for allowed in _allowed:
                if isinstance(allowed, str) and allowed.endswith("*"):
                    if issue_val.startswith(allowed[:-1]):
                        return True
                elif issue_val == allowed:
                    return True
            return False
    ```

### `_set_status` {#fn--set-status-4356}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4356`

**Signature**

```python
def _set_status(all_issues, rules):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `rules` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _set_status(all_issues, rules):
        results = []
        for set_name in rules.get("exact_sets", {}).keys():
            si   = all_issues.filter(pl.col("set_name") == set_name)
            high = si.filter(pl.col("severity") == "high").height
            med  = si.filter(pl.col("severity") == "medium").height
            if high > 0:
                status  = "FAIL"
                details = "; ".join(f"{r['Q Name'] or r['current']}" for r in si.filter(pl.col("severity") == "high").to_dicts())
            elif med > 0:
                status  = "WARNING"
                details = "; ".join(f"{r['Q Name'] or r['current']}" for r in si.to_dicts())
            else:
                status, details = "PASS", "All required questions present and correct"
            results.append({"set": set_name, "status": status, "details": details})
        for set_name, rule in rules.get("min_count_sets", {}).items():
            si = all_issues.filter(pl.col("set_name") == set_name)
            if si.filter(pl.col("severity").is_in(["high", "medium"])).height > 0:
                status, details = "FAIL", si["current"].to_list()[0]
            else:
                status  = "PASS"
                details = f">={rule.get('min_count',0)} {rule.get('prefix','')}* questions confirmed"
            results.append({"set": set_name, "status": status, "details": details})
        if rules.get("crop_harvest"):
            crp = all_issues.filter(pl.col("set_name") == "CRP_HARV")
            if crp.height > 0:
                status, details = "FAIL", crp["current"].to_list()[0]
            else:
                status, details = "PASS", "Crop harvest rule respected"
            results.append({"set": "CRP_HARV", "status": status, "details": details})

        return results
    ```

### `_cat_counts` {#fn--cat-counts-4390}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4390`

**Signature**

```python
def _cat_counts(df):
```

**Returns:** `None or implicit return`

**What it does:** Returns counts by mandatory_cat for the four standard categories.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _cat_counts(df):
        """Returns counts by mandatory_cat for the four standard categories."""
        cats = ["mandatory", "mandatory-panel", "non-mandatory", "optional"]
        if "mandatory_cat" not in df.columns or df.height == 0:
            return {c: 0 for c in cats}
        return {cat: df.filter(pl.col("mandatory_cat") == cat).height for cat in cats}
    ```

### `write_summary_sheet` {#fn-write-summary-sheet-4399}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4399`

**Signature**

```python
def write_summary_sheet(wb, all_issues, rules, replacement_status=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `rules` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `replacement_status` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def write_summary_sheet(wb, all_issues, rules, replacement_status=None):
        ws = wb.create_sheet("Summary")
        ws.sheet_view.showGridLines = False
        # A=category/set  B=total/status  C=mandatory/details  D=m-panel  E=non-mand.  F=optional  G=severity
        for col, w in zip("ABCDEFG", [32, 8, 13, 10, 13, 10, 14]):
            ws.column_dimensions[col].width = w

        ws.merge_cells("A1:G1")
        ws["A1"] = "GeoPoll Questionnaire Validation Report"
        ws["A1"].font = FONT_TITLE
        ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[1].height = 26
        ws.merge_cells("A2:G2")
        ws["A2"] = f"Comparison basis: {_reference_scope_label()}"
        ws["A2"].font = Font(size=10, color="274E13", italic=True)
        ws["A2"].alignment = Alignment(horizontal="left", vertical="center")

        r = 3
        #  Critical sets 
        _section_header(ws, r, "CRITICAL SETS STATUS", 7); r += 1
        _header_row(ws, r, ["Critical set", "Status", "Details", "", "", "", ""]); r += 1
        for row_data in _set_status(all_issues, rules):
            fill = STATUS_FILL.get(row_data["status"])
            ws.cell(row=r, column=1, value=row_data["set"])
            ws.cell(row=r, column=2, value=row_data["status"])
            ws.cell(row=r, column=3, value=row_data["details"])
            _data_row(ws, r, 7, fill=fill); r += 1

        r += 1
        #  Structure checks (aligned with KoBo summary order)
        _section_header(ws, r, "QUESTIONNAIRE STRUCTURE CHECKS", 7); r += 1
        _header_row(ws, r, ["Check", "Status", "Details", "", "", "", ""]); r += 1

        _skip_df = all_issues.filter(pl.col("issue_type").is_in(list(SKIP_PATTERN_ISSUE_TYPES)))
        _skip_high = _skip_df.filter(pl.col("severity") == "high").height
        _skip_med = _skip_df.filter(pl.col("severity") == "medium").height
        _skip_info = _skip_df.filter(pl.col("severity") == "info").height

        ws.cell(row=r, column=1, value="Skip logic references")
        ws.cell(row=r, column=2, value="FAIL" if _skip_high > 0 else "PASS")
        ws.cell(row=r, column=3, value=(f"High severity issues: {_skip_high}" if _skip_high > 0 else "No high severity issues"))
        _data_row(ws, r, 7, fill=STATUS_FILL.get("FAIL" if _skip_high > 0 else "PASS")); r += 1

        _skip_warn_total = _skip_med + _skip_info
        ws.cell(row=r, column=1, value="Skip logic references")
        ws.cell(row=r, column=2, value="WARN" if _skip_warn_total > 0 else "PASS")
        ws.cell(row=r, column=3, value=(f"Medium severity issues: {_skip_med}; Info: {_skip_info}" if _skip_warn_total > 0 else "No medium/info issues"))
        _data_row(ws, r, 7, fill=STATUS_FILL.get("WARN" if _skip_warn_total > 0 else "PASS")); r += 1

        _dup_n = all_issues.filter(pl.col("issue_type") == "duplicate_qname").height
        _dup_st = "FAIL" if _dup_n > 0 else "PASS"
        ws.cell(row=r, column=1, value="Duplicate Q Names")
        ws.cell(row=r, column=2, value=_dup_st)
        ws.cell(row=r, column=3, value=f"{_dup_n} duplicate(s) found" if _dup_n else "No duplicates")
        _data_row(ws, r, 7, fill=STATUS_FILL.get(_dup_st)); r += 1

        _qt_df = all_issues.filter(pl.col("issue_type").is_in(list(QTYPE_ISSUE_TYPES)))
        _qt_high = _qt_df.filter(pl.col("severity") == "high").height
        _qt_med = _qt_df.filter(pl.col("severity") == "medium").height
        _qt_info = _qt_df.filter(pl.col("severity") == "info").height
        _qt_status = "FAIL" if _qt_high > 0 else ("WARN" if (_qt_med + _qt_info) > 0 else "PASS")
        ws.cell(row=r, column=1, value="Q Type integrity")
        ws.cell(row=r, column=2, value=_qt_status)
        ws.cell(row=r, column=3, value=f"High: {_qt_high}; Medium: {_qt_med}; Info: {_qt_info}")
        _data_row(ws, r, 7, fill=STATUS_FILL.get(_qt_status)); r += 1

        r += 1
        #  Replacement status
        _section_header(ws, r, "REPLACEMENT STATUS (validated questionnaire output)", 7); r += 1
        _header_row(ws, r, ["Check", "Status", "Details", "", "", "", ""]); r += 1

        _repl_rows = (replacement_status or {}).get("rows", [])
        if not _repl_rows:
            ws.cell(row=r, column=1, value="Replacement step not run")
            ws.cell(row=r, column=2, value="INFO")
            ws.cell(row=r, column=3, value="No replacement diagnostics available for this run.")
            _data_row(ws, r, 7, "info"); r += 1
        else:
            for rd in _repl_rows:
                sev = rd.get("severity", "info")
                st = str(rd.get("status", "INFO") or "INFO").upper()
                ws.cell(row=r, column=1, value=rd.get("check", ""))
                ws.cell(row=r, column=2, value=st)
                ws.cell(row=r, column=3, value=rd.get("details", ""))
                row_fill = STATUS_FILL.get(st) or SEVERITY_FILL.get(sev)
                _data_row(ws, r, 7, fill=row_fill)
                if st == "PASS":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="274E13")
                elif st in {"WARN", "WARNING"}:
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="B45F06")
                elif st == "FAIL":
                    ws.cell(row=r, column=2).font = Font(bold=True, size=10, color="CC0000")
                r += 1

        r += 1
        #  Question changes (7 cols with mandatory breakdown)
        _section_header(ws, r, "QUESTION CHANGES", 7); r += 1
        _header_row(ws, r, ["Category", "Total", "Mandatory", "M-Panel", "Non-mand.", "Optional", "Severity"]); r += 1
        for label, itype, sev_filter, disp_sev in [
            ("Mandatory flag changes",     "mandatory_column_mismatch", None,   "high"),
            ("Mandatory to optional",      "mandatory_to_optional",     None,   "high"),
            ("Questions removed (high)",   "removed_question",          "high", "high"),
            ("Questions removed (info)",   "removed_question",          "info", "info"),
            ("Questions added",            "added_question",            None,   "info"),
            ("Q Type changed (high)",      "qtype_changed",             "high", "high"),
            ("Q Type changed (medium)",    "qtype_changed",             "medium", "medium"),
            ("Conditional changed",        "conditional_changed",       None,   "medium"),
            ("Randomize changed",          "randomize_changed",         None,   "medium"),
            ("Programming instructions changed", "programming_instructions_changed", None, "medium"),
            ("Core questions-only changed", "core_questions_only_changed", None, "medium"),
            ("Question labels changed",    "question_label_mismatch",   None,   "medium"),
        ]:
            q = all_issues.filter(pl.col("issue_type") == itype)
            if sev_filter:
                q = q.filter(pl.col("severity") == sev_filter)
            counts = _cat_counts(q)
            ws.cell(row=r, column=1, value=label)
            ws.cell(row=r, column=2, value=q.height)
            ws.cell(row=r, column=3, value=counts["mandatory"])
            ws.cell(row=r, column=4, value=counts["mandatory-panel"])
            ws.cell(row=r, column=5, value=counts["non-mandatory"])
            ws.cell(row=r, column=6, value=counts["optional"])
            if q.height == 0:
                ws.cell(row=r, column=7, value="none")
                _data_row(ws, r, 7, fill=FILL_PASS)
            else:
                ws.cell(row=r, column=7, value=disp_sev)
                _data_row(ws, r, 7, disp_sev)
            r += 1

        r += 1
        #  Option changes (7 cols with mandatory breakdown)
        _section_header(ws, r, "OPTION CHANGES (questions present in both files)", 7); r += 1
        _header_row(ws, r, ["Category", "Total", "Mandatory", "M-Panel", "Non-mand.", "Optional", "Severity"]); r += 1
        for label, itype, disp_sev in [
            ("Options removed",                 "removed_option",                     "high"),
            ("Options added",                   "added_option",                       "medium"),
            ("Option labels changed",           "option_label_mismatch",              "medium"),
            ("Option positions changed",   "option_position_renumbered_same_label",  "high"),
            ("Codes token mismatch",            "codes_col_token_mismatch",           "high"),
            ("Codes removed",                   "codes_col_removed",                  "high"),
            ("Codes added",                     "codes_col_added",                    "medium"),
            ("Codes renumbered (same token)",   "codes_col_renumbered_same_token",    "high"),
        ]:
            q = all_issues.filter(pl.col("issue_type") == itype)
            counts = _cat_counts(q)
            ws.cell(row=r, column=1, value=label)
            ws.cell(row=r, column=2, value=q.height)
            ws.cell(row=r, column=3, value=counts["mandatory"])
            ws.cell(row=r, column=4, value=counts["mandatory-panel"])
            ws.cell(row=r, column=5, value=counts["non-mandatory"])
            ws.cell(row=r, column=6, value=counts["optional"])
            if q.height == 0:
                ws.cell(row=r, column=7, value="none")
                _data_row(ws, r, 7, fill=FILL_PASS)
            else:
                ws.cell(row=r, column=7, value=disp_sev)
                _data_row(ws, r, 7, disp_sev)
            r += 1
    ```

### `write_structure_skip_sheet` {#fn-write-structure-skip-sheet-4561}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4561`

**Signature**

```python
def write_structure_skip_sheet(wb, all_issues: pl.DataFrame):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_structure_skip_sheet(wb, all_issues: pl.DataFrame):
        ws = wb.create_sheet("Questionnaire Structure")
        ws.sheet_view.showGridLines = False

        def _sorted(df: pl.DataFrame) -> pl.DataFrame:
            if df.height == 0:
                return df
            return (
                df.with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )

        skip_df = _sorted(all_issues.filter(pl.col("issue_type").is_in(list(SKIP_PATTERN_ISSUE_TYPES))))
        qtype_df = _sorted(all_issues.filter(pl.col("issue_type").is_in(list(QTYPE_ISSUE_TYPES))))
        dup_df = _sorted(all_issues.filter(pl.col("issue_type") == "duplicate_qname"))

        _section_header(ws, 1, "QUESTIONNAIRE STRUCTURE  Skip pattern issues", 8)
        next_row = _issues_table(ws, 2, skip_df)

        _section_header(ws, next_row, "Q TYPE INTEGRITY ISSUES", 8)
        next_row = _issues_table(ws, next_row + 1, qtype_df)

        _section_header(ws, next_row, "DUPLICATE Q NAME ISSUES", 8)
        _issues_table(ws, next_row + 1, dup_df)

        ws.freeze_panes = "A3"
        _autofit(ws)
    ```

### `write_structure_skip_sheet._sorted` {#fn--sorted-4565}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4565`

**Signature**

```python
def _sorted(df: pl.DataFrame) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def _sorted(df: pl.DataFrame) -> pl.DataFrame:
            if df.height == 0:
                return df
            return (
                df.with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )
    ```

### `write_replacement_issues_sheet` {#fn-write-replacement-issues-sheet-4596}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4596`

**Signature**

```python
def write_replacement_issues_sheet(wb, all_issues: pl.DataFrame):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_replacement_issues_sheet(wb, all_issues: pl.DataFrame):
        ws = wb.create_sheet("Replacement Issues")
        ws.sheet_view.showGridLines = False

        df = all_issues.filter(
            pl.col("issue_type").is_in(list(REPLACEMENT_ISSUE_TYPES))
        )
        if df.height > 0:
            df = (
                df.with_columns(
                    pl.when(pl.col("severity") == "high").then(pl.lit(0))
                    .when(pl.col("severity") == "medium").then(pl.lit(1))
                    .otherwise(pl.lit(2))
                    .alias("_s")
                )
                .sort(["_s", "issue_type", "Q Name"])
                .drop("_s")
            )

        _section_header(ws, 1, "REPLACEMENT ISSUES  Placeholder/additional-info diagnostics", 8)
        _issues_table(ws, 2, df)
        ws.freeze_panes = "A3"
        _autofit(ws)
    ```

### `write_critical_sets_sheet` {#fn-write-critical-sets-sheet-4622}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4622`

**Signature**

```python
def write_critical_sets_sheet(wb, all_issues, found_info=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def write_critical_sets_sheet(wb, all_issues, found_info=None):
        ws = wb.create_sheet("Critical Sets")
        ws.sheet_view.showGridLines = False

        df = all_issues.filter(
            pl.col("issue_type").is_in(list(CRITICAL_SET_ISSUE_TYPES))
        ).sort(["set_name", "severity", "Q Name"])

        _section_header(ws, 1, "CRITICAL SETS  Structural validation issues", 8)
        next_row = _issues_table(ws, 2, df)

        if found_info:
            next_row += 1
            _section_header(ws, next_row, "QUESTIONS FOUND IN CURRENT QUESTIONNAIRE", 3)
            next_row += 1
            _header_row(ws, next_row, ["Set", "Count found", "Questions"])
            next_row += 1
            for set_name, questions in found_info.items():
                ws.cell(row=next_row, column=1, value=set_name)
                ws.cell(row=next_row, column=2, value=len(questions))
                ws.cell(row=next_row, column=3, value=", ".join(questions) if questions else "none found")
                _data_row(ws, next_row, 3, "info" if questions else "high")
                next_row += 1

        _autofit(ws)
    ```

### `write_question_changes_sheet` {#fn-write-question-changes-sheet-4650}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4650`

**Signature**

```python
def write_question_changes_sheet(wb, question_changes_view):
```

**Returns:** `None or implicit return`

**What it does:** All question-level changes sorted highinfo. The 'Type' column shows

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `question_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_question_changes_sheet(wb, question_changes_view):
        """
        All question-level changes sorted highinfo. The 'Type' column shows
        mandatory / mandatory-panel / non-mandatory / optional for each question.
        The 'Field' column is omitted  it is implicit from the issue type.
        """
        ws = wb.create_sheet("Question Changes")
        ws.sheet_view.showGridLines = False

        df = question_changes_view
        df = (
            df.with_columns(
                pl.when(pl.col("severity") == "high"  ).then(pl.lit(0))
                .when(  pl.col("severity") == "medium").then(pl.lit(1))
                .otherwise(pl.lit(2))
                .alias("_s")
            )
            .sort(["_s", "issue_type", "Q Name"])
            .drop("_s")
        )
        for col in ("set_name", "field"):
            if col in df.columns:
                df = df.drop(col)

        _section_header(ws, 1, "QUESTION CHANGES  Presence, mandatory, type and control-field changes", 10)
        _issues_table(ws, 2, df)
        _apply_inline_diff_for_issue(ws, 2, df, {"question_label_mismatch", "conditional_changed", "programming_instructions_changed", "core_questions_only_changed"})
        _autofit(ws)
    ```

### `write_option_changes_sheet` {#fn-write-option-changes-sheet-4681}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4681`

**Signature**

```python
def write_option_changes_sheet(wb, option_changes_view):
```

**Returns:** `None or implicit return`

**What it does:** Option-level changes for questions present in both files. The 'Field'

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `wb` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `option_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |

??? note "Function source"

    ```python
    def write_option_changes_sheet(wb, option_changes_view):
        """
        Option-level changes for questions present in both files. The 'Field'
        column shows option_1 / option_2 /  so you know which answer choice is
        affected. The 'Type' column shows the mandatory category of the parent question.
        """
        ws = wb.create_sheet("Option Changes")
        ws.sheet_view.showGridLines = False

        df = option_changes_view
        if "set_name" in df.columns:
            df = df.drop("set_name")

        code_issue_types = {
            "codes_col_token_mismatch",
            "codes_col_removed",
            "codes_col_added",
            "codes_col_renumbered_same_token",
        }
        option_df = df.filter(~pl.col("issue_type").is_in(list(code_issue_types)))
        codes_df = df.filter(pl.col("issue_type").is_in(list(code_issue_types)))

        _section_header(ws, 1, "OPTION CHANGES  Answer options for questions in both files", max(8, len(df.columns)))
        option_table_start = 2
        next_row = _issues_table(ws, option_table_start, option_df)
        _apply_inline_diff_for_issue(ws, option_table_start, option_df, {"option_label_mismatch", "option_position_renumbered_same_label"})

        next_row += 1
        _section_header(ws, next_row, "CODES COLUMN CHECKS  Number/token consistency in 'Codes'", max(8, len(df.columns)))
        codes_table_start = next_row + 1
        _issues_table(ws, codes_table_start, codes_df)
        _apply_inline_diff_for_issue(ws, codes_table_start, codes_df, {"codes_col_token_mismatch", "codes_col_renumbered_same_token"})

        # Keep sheet navigation usable: second table must not move freeze panes down.
        ws.freeze_panes = "A3"
        _cols = [(s, d) for s, d in _issues_col_map() if s in df.columns]
        if _cols:
            _n = len(_cols)
            _hdr = option_table_start if option_df.height > 0 else codes_table_start
            ws.auto_filter.ref = f"A{_hdr}:{get_column_letter(_n)}{_hdr}"
        _autofit(ws)
    ```

### `export_validation_report` {#fn-export-validation-report-4725}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4725`

**Signature**

```python
def export_validation_report(all_issues, question_changes_view, option_changes_view, result_file, rules, found_info=None, replacement_status=None):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `all_issues` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `question_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `option_changes_view` | positional_or_keyword | Yes | `-` | `-` | Polars DataFrame carrying records for this processing stage. |
| `result_file` | positional_or_keyword | Yes | `-` | `-` | Filesystem path used for reading inputs or writing outputs. |
| `rules` | positional_or_keyword | Yes | `-` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `found_info` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |
| `replacement_status` | positional_or_keyword | No | `None` | `-` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def export_validation_report(all_issues, question_changes_view, option_changes_view, result_file, rules, found_info=None, replacement_status=None):
        wb = Workbook()
        wb.remove(wb.active)
        write_summary_sheet(wb, all_issues, rules, replacement_status=replacement_status)
        write_critical_sets_sheet(wb, all_issues, found_info=found_info)
        write_structure_skip_sheet(wb, all_issues)
        write_replacement_issues_sheet(wb, all_issues)
        write_question_changes_sheet(wb, question_changes_view)
        write_option_changes_sheet(wb, option_changes_view)
        wb.save(result_file)
        print(f"Report saved to: {result_file}")
        print(f"Sheets: {wb.sheetnames}")
    ```

### `_resolve_survey_sheet` {#fn--resolve-survey-sheet-4739}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4739`

**Signature**

```python
def _resolve_survey_sheet(workbook):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `workbook` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |

??? note "Function source"

    ```python
    def _resolve_survey_sheet(workbook):
        ws = next((workbook[n] for n in workbook.sheetnames if n.strip().lower() == "survey"), None)
        if ws is None:
            raise KeyError(f"Survey sheet not found. Available sheets: {workbook.sheetnames}")
        return ws
    ```

### `_sheet_header_map` {#fn--sheet-header-map-4746}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4746`

**Signature**

```python
def _sheet_header_map(ws, header_row: int=3) -> dict[str, int]:
```

**Returns:** `dict[str, int]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `header_row` | positional_or_keyword | No | `3` | `int` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _sheet_header_map(ws, header_row: int = 3) -> dict[str, int]:
        mapping = {}
        for col in range(1, ws.max_column + 1):
            value = ws.cell(row=header_row, column=col).value
            if value is None:
                continue
            mapping[str(value).strip()] = col
        return mapping
    ```

### `_count_selected_crops` {#fn--count-selected-crops-4756}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4756`

**Signature**

```python
def _count_selected_crops(crop_df: pl.DataFrame, language: str) -> tuple[int, int, str]:
```

**Returns:** `tuple[int, int, str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _count_selected_crops(crop_df: pl.DataFrame, language: str) -> tuple[int, int, str]:
        meta = extract_crop_metadata(crop_df, language)
        total_candidates = len(meta.get("labels", []))
        select_col = meta.get("select_col")
        if not select_col or select_col not in crop_df.columns:
            return 0, total_candidates, "missing_select_column"
        selected_values = crop_df.get_column(select_col).to_list()
        selected_count = sum(
            1 for v in selected_values
            if str(v or "").strip() not in {"", "0", "0.0", "none", "nan"}
        )
        return selected_count, total_candidates, "ok"
    ```

### `_placeholder_scan_columns` {#fn--placeholder-scan-columns-4770}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4770`

**Signature**

```python
def _placeholder_scan_columns(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _placeholder_scan_columns(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]] = None) -> list[str]:
        cols = [c for c in (candidate_columns or RESTORE_TEXT_COLUMNS) if c in questions_df.columns]
        if "Codes" in questions_df.columns and "Codes" not in cols:
            cols.append("Codes")
        return cols
    ```

### `_extract_placeholder_tokens` {#fn--extract-placeholder-tokens-4777}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4777`

**Signature**

```python
def _extract_placeholder_tokens(text: str) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _extract_placeholder_tokens(text: str) -> list[str]:
        return re.findall(r"\$[^$\r\n]+\$", str(text or ""))
    ```

### `_has_broken_placeholder_token` {#fn--has-broken-placeholder-token-4781}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4781`

**Signature**

```python
def _has_broken_placeholder_token(text: str) -> bool:
```

**Returns:** `bool`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `text` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _has_broken_placeholder_token(text: str) -> bool:
        txt = str(text or "")
        if "$" not in txt:
            return False
        stripped = re.sub(r"\$[^$\r\n]+\$", "", txt)
        return "$" in stripped
    ```

### `_count_unresolved_placeholders` {#fn--count-unresolved-placeholders-4789}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4789`

**Signature**

```python
def _count_unresolved_placeholders(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]]=None) -> int:
```

**Returns:** `int`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `candidate_columns` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _count_unresolved_placeholders(questions_df: pl.DataFrame, candidate_columns: Optional[list[str]] = None) -> int:
        cols = _placeholder_scan_columns(questions_df, candidate_columns)
        if not cols:
            return 0
        unresolved = 0
        for row in questions_df.select(cols).iter_rows(named=True):
            for col in cols:
                txt = str(row.get(col) or "")
                if _extract_placeholder_tokens(txt):
                    unresolved += 1
        return unresolved
    ```

### `_selected_crop_labels` {#fn--selected-crop-labels-4802}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4802`

**Signature**

```python
def _selected_crop_labels(crop_df: pl.DataFrame, language: str, limit: int=15) -> list[str]:
```

**Returns:** `list[str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `limit` | positional_or_keyword | No | `15` | `int` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _selected_crop_labels(crop_df: pl.DataFrame, language: str, limit: int = 15) -> list[str]:
        meta = extract_crop_metadata(crop_df, language)
        label_col = meta.get("label_col")
        select_col = meta.get("select_col")
        if not label_col or not select_col or label_col not in crop_df.columns or select_col not in crop_df.columns:
            return []
        labels = []
        for row in crop_df.select([label_col, select_col]).iter_rows(named=True):
            sel = str(row.get(select_col) or "").strip().lower()
            if sel not in {"", "0", "0.0", "none", "nan"}:
                lbl = str(row.get(label_col) or "").strip()
                if lbl:
                    labels.append(lbl)
        if len(labels) > limit:
            return labels[:limit] + [f"... (+{len(labels) - limit} more)"]
        return labels
    ```

### `_selected_crop_entries` {#fn--selected-crop-entries-4820}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4820`

**Signature**

```python
def _selected_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
```

**Returns:** `list[dict]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _selected_crop_entries(crop_df: pl.DataFrame, language: str) -> list[dict]:
        if crop_df is None or crop_df.height == 0:
            return []
        meta = extract_crop_metadata(crop_df, language)
        label_col = meta.get("label_col")
        dataset_col = meta.get("dataset_col")
        select_col = meta.get("select_col")
        if not label_col or not select_col or label_col not in crop_df.columns or select_col not in crop_df.columns:
            return []

        cols = [label_col, select_col]
        if dataset_col and dataset_col in crop_df.columns:
            cols.append(dataset_col)

        out = []
        for row in crop_df.select(cols).iter_rows(named=True):
            if not _is_selected_crop_value(row.get(select_col)):
                continue
            label = str(row.get(label_col) or "").strip()
            code = str(row.get(dataset_col) or "").strip() if dataset_col and dataset_col in crop_df.columns else ""
            if not label and not code:
                continue
            key = code.lower() if code else label.lower()
            display = f"{code} - {label}" if code and label else (label or code)
            out.append({"key": key, "display": display})
        return out
    ```

### `_join_short` {#fn--join-short-4848}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4848`

**Signature**

```python
def _join_short(items: list[str], limit: int=12) -> str:
```

**Returns:** `str`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `items` | positional_or_keyword | Yes | `-` | `list[str]` | Input used by the `Step 10 Export to Excel` stage. |
| `limit` | positional_or_keyword | No | `12` | `int` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _join_short(items: list[str], limit: int = 12) -> str:
        if not items:
            return "none"
        if len(items) <= limit:
            return ", ".join(items)
        return ", ".join(items[:limit]) + f", ... (+{len(items) - limit} more)"
    ```

### `_build_crop_round_delta_issue_rows` {#fn--build-crop-round-delta-issue-rows-4856}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4856`

**Signature**

```python
def _build_crop_round_delta_issue_rows(current_crop_df: pl.DataFrame, reference_crop_df: pl.DataFrame, language: str, crop_qnames: Optional[list[str]]=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `current_crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `reference_crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `crop_qnames` | positional_or_keyword | No | `None` | `Optional[list[str]]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _build_crop_round_delta_issue_rows(
        current_crop_df: pl.DataFrame,
        reference_crop_df: pl.DataFrame,
        language: str,
        crop_qnames: Optional[list[str]] = None,
    ) -> pl.DataFrame:
        schema = {
            "issue_type": pl.Utf8,
            "set_name": pl.Utf8,
            "Q Name": pl.Utf8,
            "field": pl.Utf8,
            "current": pl.Utf8,
            "reference": pl.Utf8,
            "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }
        if reference_crop_df is None or reference_crop_df.height == 0:
            return pl.DataFrame(schema=schema)

        cur_entries = _selected_crop_entries(current_crop_df, language)
        ref_entries = _selected_crop_entries(reference_crop_df, language)
        if not cur_entries and not ref_entries:
            return pl.DataFrame(schema=schema)

        cur_map = {e["key"]: e["display"] for e in cur_entries}
        ref_map = {e["key"]: e["display"] for e in ref_entries}
        cur_keys = set(cur_map.keys())
        ref_keys = set(ref_map.keys())

        added = sorted(cur_map[k] for k in (cur_keys - ref_keys))
        removed = sorted(ref_map[k] for k in (ref_keys - cur_keys))
        qname_txt = ", ".join(crop_qnames) if crop_qnames else "crop placeholder question(s)"

        row = {
            "issue_type": "replacement_crop_round_delta",
            "set_name": "REPLACEMENT",
            "Q Name": qname_txt,
            "field": "Crop list (selected top 10)",
            "current": (
                f"Current selected ({len(cur_entries)}): {_join_short(sorted(cur_map.values()))} | "
                f"Added vs reference ({len(added)}): {_join_short(added)}"
            ),
            "reference": (
                f"Reference selected ({len(ref_entries)}): {_join_short(sorted(ref_map.values()))} | "
                f"Removed vs reference ({len(removed)}): {_join_short(removed)}"
            ),
            "severity": "info",
            "excel_row": None,
        }
        return pl.DataFrame([row], schema=schema)
    ```

### `_build_replacement_issue_rows` {#fn--build-replacement-issue-rows-4908}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4908`

**Signature**

```python
def _build_replacement_issue_rows(validated_questions: pl.DataFrame, replacements: dict[str, str], crop_df: pl.DataFrame, language: str, reference_questions: pl.DataFrame | None=None, additional_info_diag: dict | None=None, replacements_by_language: dict[str, dict[str, str]] | None=None) -> pl.DataFrame:
```

**Returns:** `pl.DataFrame`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `validated_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 10 Export to Excel` stage. |
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `reference_questions` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Questionnaire structure table used by comparison and checks. |
| `additional_info_diag` | positional_or_keyword | No | `None` | `dict | None` | Input used by the `Step 10 Export to Excel` stage. |
| `replacements_by_language` | positional_or_keyword | No | `None` | `dict[str, dict[str, str]] | None` | Language selector used for language-specific text columns. |

??? note "Function source"

    ```python
    def _build_replacement_issue_rows(
        validated_questions: pl.DataFrame,
        replacements: dict[str, str],
        crop_df: pl.DataFrame,
        language: str,
        reference_questions: pl.DataFrame | None = None,
        additional_info_diag: dict | None = None,
        replacements_by_language: dict[str, dict[str, str]] | None = None,
    ) -> pl.DataFrame:
        schema = {
            "issue_type": pl.Utf8,
            "set_name": pl.Utf8,
            "Q Name": pl.Utf8,
            "field": pl.Utf8,
            "current": pl.Utf8,
            "reference": pl.Utf8,
            "severity": pl.Utf8,
            "excel_row": pl.Int64,
        }
        rows = []

        selected_count, total_candidates, crop_mode = _count_selected_crops(crop_df, language)
        if crop_mode == "missing_select_column":
            rows.append({
                "issue_type": "replacement_crop_selection_mismatch",
                "set_name": "REPLACEMENT",
                "Q Name": "",
                "field": "Crop list",
                "current": f"selection column missing ({total_candidates} candidate crops)",
                "reference": "Crop list should mark exactly 10 selected crops",
                "severity": "medium",
                "excel_row": None,
            })
        elif selected_count != 10:
            selected_labels = _selected_crop_labels(crop_df, language)
            rows.append({
                "issue_type": "replacement_crop_selection_mismatch",
                "set_name": "REPLACEMENT",
                "Q Name": "",
                "field": "Crop list",
                "current": f"{selected_count}/10 selected | {', '.join(selected_labels) if selected_labels else 'no selected labels'}",
                "reference": "Expected exactly 10 selected crops for $TEN MOST COMMON CROPS$ / $CROP CODES$ substitution",
                "severity": "medium",
                "excel_row": None,
            })

        if not replacements and not any((replacements_by_language or {}).values()):
            detail = "No replacement keys loaded"
            if additional_info_diag:
                detail = (
                    f"No replacement keys loaded | rows={additional_info_diag.get('rows_with_any_data', 0)} "
                    f"placeholder-style={additional_info_diag.get('rows_with_placeholder_style_original', 0)} "
                    f"plain-style={additional_info_diag.get('rows_with_non_placeholder_original', 0)}"
                )
            rows.append({
                "issue_type": "replacement_additional_info_missing",
                "set_name": "REPLACEMENT",
                "Q Name": "",
                "field": "Additional information",
                "current": detail,
                "reference": "Additional information must define all $...$ placeholders used in survey",
                "severity": "high",
                "excel_row": None,
            })

        def _effective_replacements_for_col(col_name: str) -> dict[str, str]:
            lang = _language_code_for_text_column(col_name)
            if replacements_by_language and lang and replacements_by_language.get(lang):
                return replacements_by_language[lang]
            return replacements or {}

        seen = set()
        missing_key_locs = set()

        if reference_questions is not None and reference_questions.height > 0:
            ref_cols = _placeholder_scan_columns(reference_questions)
            for row in reference_questions.select(["Q Name", "excel_row"] + ref_cols).iter_rows(named=True):
                qname = str(row.get("Q Name") or "")
                excel_row = row.get("excel_row")
                for col in ref_cols:
                    txt = str(row.get(col) or "")
                    if not txt:
                        continue
                    col_repl = _effective_replacements_for_col(col)
                    col_idx = _build_placeholder_index(col_repl)
                    for token in _extract_placeholder_tokens(txt):
                        if _is_crop_placeholder_token(token):
                            continue
                        if _lookup_placeholder_replacement(token, col_repl, col_idx) is not None:
                            continue
                        tok_norm = _normalize_placeholder_token(token)
                        key = ("replacement_missing_key", qname, col, token)
                        if key in seen:
                            continue
                        seen.add(key)
                        missing_key_locs.add((qname, col, tok_norm))
                        sev = "high"
                        rows.append({
                            "issue_type": "replacement_missing_key",
                            "set_name": "REPLACEMENT",
                            "Q Name": qname,
                            "field": col,
                            "current": token,
                            "reference": "Placeholder key missing/blank in Additional information",
                            "severity": sev,
                            "excel_row": excel_row,
                        })

        cols = _placeholder_scan_columns(validated_questions)
        for row in validated_questions.select(["Q Name", "excel_row"] + cols).iter_rows(named=True):
            qname = str(row.get("Q Name") or "")
            excel_row = row.get("excel_row")
            for col in cols:
                txt = str(row.get(col) or "")
                if not txt:
                    continue

                if _has_broken_placeholder_token(txt):
                    key = ("replacement_malformed_placeholder", qname, col, txt)
                    if key not in seen:
                        seen.add(key)
                        rows.append({
                            "issue_type": "replacement_malformed_placeholder",
                            "set_name": "REPLACEMENT",
                            "Q Name": qname,
                            "field": col,
                            "current": txt,
                            "reference": "Placeholder token should be balanced and closed (example: $season$)",
                            "severity": "medium",
                            "excel_row": excel_row,
                        })

                col_repl = _effective_replacements_for_col(col)
                col_idx = _build_placeholder_index(col_repl)
                for token in _extract_placeholder_tokens(txt):
                    tok_norm = _normalize_placeholder_token(token)
                    if _is_crop_placeholder_token(token):
                        issue_type = "replacement_unresolved_placeholder"
                        severity = "high"
                        reference = "Crop placeholders must be fully expanded in validated output"
                    elif _lookup_placeholder_replacement(token, col_repl, col_idx) is None:
                        issue_type = "replacement_missing_key"
                        severity = "high"
                        reference = "Placeholder key missing from Additional information"
                        missing_key_locs.add((qname, col, tok_norm))
                    else:
                        if (qname, col, tok_norm) in missing_key_locs:
                            continue
                        issue_type = "replacement_unresolved_placeholder"
                        severity = "medium"
                        reference = "Placeholder replacement exists but token remained unresolved"

                    key = (issue_type, qname, col, token)
                    if key in seen:
                        continue
                    seen.add(key)
                    rows.append({
                        "issue_type": issue_type,
                        "set_name": "REPLACEMENT",
                        "Q Name": qname,
                        "field": col,
                        "current": token,
                        "reference": reference,
                        "severity": severity,
                        "excel_row": excel_row,
                    })

        if not rows:
            return pl.DataFrame(schema=schema)
        return pl.DataFrame(rows, schema=schema)
    ```

### `_build_replacement_issue_rows._effective_replacements_for_col` {#fn--effective-replacements-for-col-4973}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:4973`

**Signature**

```python
def _effective_replacements_for_col(col_name: str) -> dict[str, str]:
```

**Returns:** `dict[str, str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `col_name` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _effective_replacements_for_col(col_name: str) -> dict[str, str]:
            lang = _language_code_for_text_column(col_name)
            if replacements_by_language and lang and replacements_by_language.get(lang):
                return replacements_by_language[lang]
            return replacements or {}
    ```

### `_fetch_admin_reference` {#fn--fetch-admin-reference-5080}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:5080`

**Signature**

```python
def _fetch_admin_reference(admin_level: str, iso3: str) -> tuple[list[dict], str]:
```

**Returns:** `tuple[list[dict], str]`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `admin_level` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _fetch_admin_reference(admin_level: str, iso3: str) -> tuple[list[dict], str]:
        import urllib.request
        import json

        iso3 = str(iso3 or "").upper().strip()
        if not iso3:
            return [], "missing_iso3"

        urls = {
            "Admin 1": "https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services/Administrative_Boundaries_Reference_(view_layer)/FeatureServer/1/query?where=adm0_ISO3%20%3D%20'{iso3}'&outFields=adm1_name,adm1_name_local,adm1_pcode,adm0_name,adm0_ISO3&returnGeometry=false&outSR=4326&f=json",
            "Admin 2": "https://services5.arcgis.com/sjP4Ugu5s0dZWLjd/arcgis/rest/services/Administrative_Boundaries_Reference_(view_layer)/FeatureServer/0/query?where=adm0_ISO3%20%3D%20'{iso3}'&outFields=adm2_name,adm2_name_local,adm2_pcode,adm1_name,adm1_pcode,adm0_name,adm0_ISO3&returnGeometry=false&outSR=4326&f=json",
        }
        rename = {
            "Admin 1": {
                "adm1_name": "adm1_name",
                "adm1_name_local": "adm1_name_local",
                "adm1_pcode": "adm1_pcode",
                "adm0_name": "adm0_name",
                "adm0_ISO3": "adm0_ISO3",
            },
            "Admin 2": {
                "adm2_name": "adm2_name",
                "adm2_name_local": "adm2_name_local",
                "adm2_pcode": "adm2_pcode",
                "adm1_name": "adm1_name",
                "adm1_pcode": "adm1_pcode",
                "adm0_name": "adm0_name",
                "adm0_ISO3": "adm0_ISO3",
            },
        }

        if admin_level not in urls:
            return [], f"unsupported_admin_level:{admin_level}"

        url = urls[admin_level].format(iso3=iso3)
        try:
            with urllib.request.urlopen(url, timeout=25) as resp:
                data = json.loads(resp.read().decode())
        except Exception as e:
            return [], str(e)

        features = data.get("features", []) or []
        mapping = rename[admin_level]
        rows = []
        for feat in features:
            attrs = feat.get("attributes", {}) or {}
            rows.append({dst: attrs.get(src) for src, dst in mapping.items()})
        return rows, ""
    ```

### `_write_table_sheet` {#fn--write-table-sheet-5130}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:5130`

**Signature**

```python
def _write_table_sheet(ws, rows: list[dict]):
```

**Returns:** `None or implicit return`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `ws` | positional_or_keyword | Yes | `-` | `-` | Excel workbook/sheet handle used for report writing. |
| `rows` | positional_or_keyword | Yes | `-` | `list[dict]` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _write_table_sheet(ws, rows: list[dict]):
        if not rows:
            ws.cell(row=1, column=1, value="No rows")
            return 0
        headers = list(rows[0].keys())
        for c, h in enumerate(headers, 1):
            ws.cell(row=1, column=c, value=h)
        r = 2
        for rd in rows:
            for c, h in enumerate(headers, 1):
                ws.cell(row=r, column=c, value=rd.get(h))
            r += 1
        return len(rows)
    ```

### `_apply_admin_sheets` {#fn--apply-admin-sheets-5145}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:5145`

**Signature**

```python
def _apply_admin_sheets(output_questionnaire_path: Path, iso3: str) -> dict:
```

**Returns:** `dict`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `output_questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _apply_admin_sheets(output_questionnaire_path: Path, iso3: str) -> dict:
        rows = []
        fetched = {}
        errors = {}
        for lvl in ["Admin 1", "Admin 2"]:
            data_rows, err = _fetch_admin_reference(lvl, iso3)
            if err:
                errors[lvl] = err
            else:
                fetched[lvl] = data_rows

        if fetched:
            details = ", ".join([
                f"admin1={len(fetched.get('Admin 1', []))}",
                f"admin2={len(fetched.get('Admin 2', []))}",
            ])
            rows.append({"check": "AGOL fetch", "status": "PASS" if not errors else "WARN", "details": details, "severity": "info" if not errors else "medium"})
        else:
            err_txt = "; ".join(f"{k}: {v}" for k, v in errors.items()) or "AGOL returned no data"
            rows.append({"check": "AGOL fetch", "status": "FAIL", "details": err_txt, "severity": "high"})
            return {"rows": rows}

        try:
            wb = openpyxl.load_workbook(output_questionnaire_path)
            for lvl, data_rows in fetched.items():
                sheet_name = f"{lvl} info"
                if sheet_name in wb.sheetnames:
                    del wb[sheet_name]
                ws = wb.create_sheet(sheet_name)
                n = _write_table_sheet(ws, data_rows)
                rows.append({
                    "check": f"Admin sheet added: {lvl.lower().replace(' ', '')}",
                    "status": "PASS",
                    "details": f"{n} rows written",
                    "severity": "info",
                })
            wb.save(output_questionnaire_path)
        except Exception as e:
            rows.append({"check": "Admin sheet write", "status": "FAIL", "details": str(e), "severity": "high"})

        return {"rows": rows}
    ```

### `_build_replacement_status_rows` {#fn--build-replacement-status-rows-5188}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:5188`

**Signature**

```python
def _build_replacement_status_rows(validated_questions: pl.DataFrame, crop_df: pl.DataFrame, replacements: dict[str, str], language: str, iso3: str, output_questionnaire_path: Optional[Path], write_status: dict, additional_info_diag: dict | None=None, replacement_issues: pl.DataFrame | None=None) -> dict:
```

**Returns:** `dict`

**What it does:** Implements logic in the `Step 10 Export to Excel` phase.

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `validated_questions` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |
| `crop_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Input used by the `Step 10 Export to Excel` stage. |
| `replacements` | positional_or_keyword | Yes | `-` | `dict[str, str]` | Input used by the `Step 10 Export to Excel` stage. |
| `language` | positional_or_keyword | Yes | `-` | `str` | Language selector used for language-specific text columns. |
| `iso3` | positional_or_keyword | Yes | `-` | `str` | Input used by the `Step 10 Export to Excel` stage. |
| `output_questionnaire_path` | positional_or_keyword | Yes | `-` | `Optional[Path]` | Filesystem path used for reading inputs or writing outputs. |
| `write_status` | positional_or_keyword | Yes | `-` | `dict` | Input used by the `Step 10 Export to Excel` stage. |
| `additional_info_diag` | positional_or_keyword | No | `None` | `dict | None` | Input used by the `Step 10 Export to Excel` stage. |
| `replacement_issues` | positional_or_keyword | No | `None` | `pl.DataFrame | None` | Input used by the `Step 10 Export to Excel` stage. |

??? note "Function source"

    ```python
    def _build_replacement_status_rows(
        validated_questions: pl.DataFrame,
        crop_df: pl.DataFrame,
        replacements: dict[str, str],
        language: str,
        iso3: str,
        output_questionnaire_path: Optional[Path],
        write_status: dict,
        additional_info_diag: dict | None = None,
        replacement_issues: pl.DataFrame | None = None,
    ) -> dict:
        rows = []

        selected_count, total_candidates, crop_mode = _count_selected_crops(crop_df, language)
        if crop_mode == "missing_select_column":
            rows.append({
                "check": "Crop selection (top 10)",
                "status": "WARN",
                "details": f"selection column not found; {total_candidates} candidates detected",
                "severity": "medium",
            })
        else:
            crop_status = "PASS" if selected_count == 10 else "WARN"
            crop_sev = "info" if crop_status == "PASS" else "medium"
            rows.append({
                "check": "Crop selection (top 10)",
                "status": crop_status,
                "details": f"{selected_count}/10 selected ({total_candidates} candidates)",
                "severity": crop_sev,
            })

        repl_df = replacement_issues if replacement_issues is not None else pl.DataFrame(schema={"issue_type": pl.Utf8, "severity": pl.Utf8})
        miss_high = repl_df.filter((pl.col("issue_type") == "replacement_missing_key") & (pl.col("severity") == "high")).height if repl_df.height > 0 else 0
        miss_med = repl_df.filter((pl.col("issue_type") == "replacement_missing_key") & (pl.col("severity") == "medium")).height if repl_df.height > 0 else 0
        unresolved_high = repl_df.filter((pl.col("issue_type") == "replacement_unresolved_placeholder") & (pl.col("severity") == "high")).height if repl_df.height > 0 else 0
        unresolved_med = repl_df.filter((pl.col("issue_type") == "replacement_unresolved_placeholder") & (pl.col("severity") == "medium")).height if repl_df.height > 0 else 0
        malformed_n = repl_df.filter(pl.col("issue_type") == "replacement_malformed_placeholder").height if repl_df.height > 0 else 0

        key_load_ok = bool(replacements)
        key_load_details = f"{len(replacements)} placeholder key(s) loaded from Additional information"
        if not key_load_ok:
            if additional_info_diag:
                key_load_details = (
                    f"No replacement keys loaded | rows={additional_info_diag.get('rows_with_any_data', 0)} "
                    f"placeholder-style={additional_info_diag.get('rows_with_placeholder_style_original', 0)} "
                    f"plain-style={additional_info_diag.get('rows_with_non_placeholder_original', 0)}"
                )
            else:
                key_load_details = "No replacement keys loaded from Additional information"

        fail_parts = []
        if miss_high > 0:
            fail_parts.append(f"missing keys (high)={miss_high}")
        if unresolved_high > 0:
            fail_parts.append(f"unresolved placeholders (high)={unresolved_high}")

        warn_parts = []
        if miss_med > 0:
            warn_parts.append(f"missing keys (medium)={miss_med}")
        if unresolved_med > 0:
            warn_parts.append(f"unresolved placeholders (medium)={unresolved_med}")
        if malformed_n > 0:
            warn_parts.append(f"malformed placeholders={malformed_n}")

        check_statuses = []
        check_statuses.append("PASS" if key_load_ok else "FAIL")
        check_statuses.append("FAIL" if fail_parts else "PASS")
        check_statuses.append("WARN" if warn_parts else "PASS")

        fail_n = sum(1 for s in check_statuses if s == "FAIL")
        warn_n = sum(1 for s in check_statuses if s == "WARN")
        pass_n = sum(1 for s in check_statuses if s == "PASS")

        if fail_n > 0:
            summary_status = "FAIL"
            summary_sev = "high"
        elif warn_n > 0:
            summary_status = "WARN"
            summary_sev = "medium"
        else:
            summary_status = "PASS"
            summary_sev = "info"

        detail_parts = [f"{summary_status} (pass={pass_n}, warn={warn_n}, fail={fail_n})", key_load_details]
        if fail_parts:
            detail_parts.append("; ".join(fail_parts))
        if warn_parts:
            detail_parts.append("; ".join(warn_parts))

        rows.append({
            "check": "Additional info replacement",
            "status": summary_status,
            "details": " | ".join([p for p in detail_parts if p]),
            "severity": summary_sev,
        })

        if write_status.get("status") == "OK" and output_questionnaire_path is not None:
            rows.extend(_apply_admin_sheets(output_questionnaire_path, iso3).get("rows", []))
        else:
            rows.append({
                "check": "AGOL fetch",
                "status": "WARN",
                "details": "Skipped because validated questionnaire could not be written",
                "severity": "medium",
            })

        return {"rows": rows}
    ```

### `write_validated_questionnaire` {#fn-write-validated-questionnaire-5297}

**Pipeline stage:** `Step 10 Export to Excel`

**Location:** `scripts/geopoll_validator.py:5297`

**Signature**

```python
def write_validated_questionnaire(source_questionnaire_path: Path, output_questionnaire_path: Path, questions_df: pl.DataFrame) -> None:
```

**Returns:** `None`

**What it does:** Creates a validated questionnaire workbook by copying the original file and

**Parameters**

| Parameter | Kind | Required | Default | Annotation | Description |
|---|---|---|---|---|---|
| `source_questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `output_questionnaire_path` | positional_or_keyword | Yes | `-` | `Path` | Filesystem path used for reading inputs or writing outputs. |
| `questions_df` | positional_or_keyword | Yes | `-` | `pl.DataFrame` | Questionnaire structure table used by comparison and checks. |

??? note "Function source"

    ```python
    def write_validated_questionnaire(
        source_questionnaire_path: Path,
        output_questionnaire_path: Path,
        questions_df: pl.DataFrame,
    ) -> None:
        """
        Creates a validated questionnaire workbook by copying the original file and
        writing the converted survey values row-by-row using Q Name as key.
        """
        copyfile(source_questionnaire_path, output_questionnaire_path)

        wb = openpyxl.load_workbook(output_questionnaire_path)
        ws = _resolve_survey_sheet(wb)
        header_map = _sheet_header_map(ws, header_row=3)

        q_col = header_map.get("Q Name")
        if not q_col:
            raise KeyError("Column 'Q Name' not found in survey header row.")

        qname_to_row = {}
        for row_idx in range(4, ws.max_row + 1):
            qname = ws.cell(row=row_idx, column=q_col).value
            key = str(qname).strip() if qname is not None else ""
            if key:
                qname_to_row[key] = row_idx

        writable_cols = [
            col for col in questions_df.columns
            if col not in {"Q Name", "excel_row", "source_file"} and col in header_map
        ]

        for row in questions_df.select(["Q Name"] + writable_cols).to_dicts():
            qname = str(row.get("Q Name") or "").strip()
            target_row = qname_to_row.get(qname)
            if not target_row:
                continue
            for col_name in writable_cols:
                cell = ws.cell(row=target_row, column=header_map[col_name])
                if not isinstance(cell, openpyxl.cell.cell.MergedCell):
                    cell.value = row.get(col_name)

        wb.save(output_questionnaire_path)
        print(f"Validated questionnaire saved to: {output_questionnaire_path}")
        return {"status": "OK", "path": str(output_questionnaire_path)}
    ```
