import ast
import re
from pathlib import Path
from textwrap import indent

ROOT = Path(r"c:/git/DIEM_Questionnaire_Validation")

TARGETS = [
    {
        "title": "KoBo Validator",
        "source": ROOT / "scripts" / "kobo_validator.py",
        "output": ROOT / "docs" / "function-reference" / "kobo-validator.md",
    },
    {
        "title": "GeoPoll Validator",
        "source": ROOT / "scripts" / "geopoll_validator.py",
        "output": ROOT / "docs" / "function-reference" / "geopoll-validator.md",
    },
]

SECTION_RE = re.compile(r"^\s*#\s*SECTION:\s*##\s*(.+?)\s*$")


def clean_section_title(raw: str) -> str:
    return re.sub(r"\s+", " ", raw.strip())


def parse_sections(lines):
    sections = [(1, "Runtime and logger helpers")]
    for i, line in enumerate(lines, start=1):
        m = SECTION_RE.match(line)
        if m:
            sections.append((i, clean_section_title(m.group(1))))
    sections.sort(key=lambda x: x[0])
    return sections


def find_section_for_line(sections, lineno):
    current = sections[0][1]
    for ln, title in sections:
        if ln <= lineno:
            current = title
        else:
            break
    return current


def get_signature(node):
    args_text = ast.unparse(node.args)
    sig = f"def {node.name}({args_text})"
    if node.returns is not None:
        sig += f" -> {ast.unparse(node.returns)}"
    sig += ":"
    return sig


def safe_unparse(node):
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def build_params(node):
    args = node.args
    rows = []

    pos = list(args.posonlyargs) + list(args.args)
    defaults = list(args.defaults)
    default_map = {}
    if defaults:
        start = len(pos) - len(defaults)
        for idx, default in enumerate(defaults, start=start):
            if 0 <= idx < len(pos):
                default_map[pos[idx].arg] = safe_unparse(default)

    for a in args.posonlyargs:
        rows.append((a.arg, "positional_only", default_map.get(a.arg), safe_unparse(a.annotation)))
    for a in args.args:
        rows.append((a.arg, "positional_or_keyword", default_map.get(a.arg), safe_unparse(a.annotation)))
    if args.vararg is not None:
        rows.append(("*" + args.vararg.arg, "var_positional", None, safe_unparse(args.vararg.annotation)))
    for a, d in zip(args.kwonlyargs, args.kw_defaults):
        rows.append((a.arg, "keyword_only", safe_unparse(d) if d is not None else None, safe_unparse(a.annotation)))
    if args.kwarg is not None:
        rows.append(("**" + args.kwarg.arg, "var_keyword", None, safe_unparse(args.kwarg.annotation)))

    return rows


def infer_param_description(name, stage):
    n = name.strip("*").lower()
    if n in {"run", "cfg", "config"}:
        return "Runtime configuration object for this validation run."
    if "path" in n or "file" in n or n.endswith("_dir"):
        return "Filesystem path used for reading inputs or writing outputs."
    if n in {"df", "issues", "all_issues", "question_changes_view", "option_changes_view"}:
        return "Polars DataFrame carrying records for this processing stage."
    if "survey" in n or "questions" in n or "choices" in n or "options" in n:
        return "Questionnaire structure table used by comparison and checks."
    if "language" in n or n in {"lang", "lang_scope", "lang_code"}:
        return "Language selector used for language-specific text columns."
    if "severity" in n:
        return "Severity label used for final issue classification."
    if n in {"ws", "wb", "workbook"}:
        return "Excel workbook/sheet handle used for report writing."
    if n in {"self", "a", "kw"}:
        return "Internal helper parameter used by runtime/logging wrapper code."
    if n in {"qname", "q", "q_name"}:
        return "Question identifier used to join or compare records."
    return f"Input used by the `{stage}` stage."


def collect_functions(source_text, tree, sections):
    funcs = []

    def visit(node, parent_qual=""):
        for child in getattr(node, "body", []):
            if isinstance(child, ast.ClassDef):
                class_qual = f"{parent_qual}.{child.name}" if parent_qual else child.name
                visit(child, class_qual)
            elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                qname = f"{parent_qual}.{child.name}" if parent_qual else child.name
                seg = ast.get_source_segment(source_text, child)
                if seg is None:
                    lines = source_text.splitlines()
                    start = child.lineno - 1
                    end = getattr(child, "end_lineno", child.lineno)
                    seg = "\n".join(lines[start:end])
                stage = find_section_for_line(sections, child.lineno)
                funcs.append(
                    {
                        "name": child.name,
                        "qname": qname,
                        "lineno": child.lineno,
                        "signature": get_signature(child),
                        "returns": safe_unparse(child.returns) if child.returns is not None else "None or implicit return",
                        "doc": (ast.get_docstring(child) or "").strip(),
                        "stage": stage,
                        "params": build_params(child),
                        "source": seg.rstrip(),
                    }
                )
                visit(child, qname)

    visit(tree)
    funcs.sort(key=lambda x: x["lineno"])
    return funcs


def format_param_table(func):
    if not func["params"]:
        return "No parameters."
    lines = [
        "| Parameter | Kind | Required | Default | Annotation | Description |",
        "|---|---|---|---|---|---|",
    ]
    for pname, pkind, pdefault, pann in func["params"]:
        required = "No" if pdefault not in (None, "") else "Yes"
        default = pdefault if pdefault not in (None, "") else "-"
        ann = pann if pann else "-"
        desc = infer_param_description(pname, func["stage"])
        pname_cell = "`" + pname.replace("|", "\\|") + "`"
        lines.append(f"| {pname_cell} | {pkind} | {required} | `{default}` | `{ann}` | {desc} |")
    return "\n".join(lines)


def details_block(code: str):
    code_block = "```python\n" + code + "\n```"
    return "??? note \"Function source\"\n\n" + indent(code_block, "    ")


def render_doc(title, source_path, funcs, sections):
    grouped = {}
    for f in funcs:
        grouped.setdefault(f["stage"], []).append(f)

    ordered_stage_names = []
    for _, stage in sections:
        if stage not in ordered_stage_names and stage in grouped:
            ordered_stage_names.append(stage)
    for stage in grouped:
        if stage not in ordered_stage_names:
            ordered_stage_names.append(stage)

    rel_source = source_path.as_posix().split("/DIEM_Questionnaire_Validation/")[-1]
    lines = [
        f"# {title} (`{rel_source}`)",
        "",
        "This page is organized by the validator pipeline stages used in the script.",
        "Use the stage map to navigate quickly, then open each function spec for parameters and full source.",
        "",
        f"Total functions documented: **{len(funcs)}**",
        "",
        "## Pipeline Function Map",
        "",
    ]

    for idx, stage in enumerate(ordered_stage_names, start=1):
        lines.append(f"### {idx}. {stage}")
        lines.append("")
        for f in grouped.get(stage, []):
            anchor = f"fn-{f['name'].lower().replace('_', '-')}-{f['lineno']}"
            label = f"`{f['qname']}`" if f["qname"] != f["name"] else f"`{f['name']}`"
            lines.append(f"- [{label}](#{anchor})")
        lines.append("")

    lines.append("## Full Specifications")
    lines.append("")

    for f in funcs:
        anchor = f"fn-{f['name'].lower().replace('_', '-')}-{f['lineno']}"
        title_name = f["qname"] if f["qname"] != f["name"] else f["name"]
        lines.extend([
            f"### `{title_name}` {{#{anchor}}}",
            "",
            f"**Pipeline stage:** `{f['stage']}`",
            "",
            f"**Location:** `{rel_source}:{f['lineno']}`",
            "",
            "**Signature**",
            "",
            "```python",
            f["signature"],
            "```",
            "",
            f"**Returns:** `{f['returns']}`",
            "",
        ])
        if f["doc"]:
            lines.append(f"**What it does:** {f['doc'].splitlines()[0].strip()}")
        else:
            lines.append(f"**What it does:** Implements logic in the `{f['stage']}` phase.")
        lines.extend([
            "",
            "**Parameters**",
            "",
            format_param_table(f),
            "",
            details_block(f["source"]),
            "",
        ])

    return "\n".join(lines).rstrip() + "\n"


def main():
    for target in TARGETS:
        source_text = target["source"].read_text(encoding="utf-8")
        sections = parse_sections(source_text.splitlines())
        tree = ast.parse(source_text)
        funcs = collect_functions(source_text, tree, sections)
        md = render_doc(target["title"], target["source"], funcs, sections)
        target["output"].write_text(md, encoding="utf-8")
        print(f"Wrote {target['output']} ({len(funcs)} functions)")


if __name__ == "__main__":
    main()
