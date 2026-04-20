#!/usr/bin/env python3
"""
Figma Variables Review

Reads:
  - inputs/inputs.json              (componentName)
  - inputs/component-tokens.csv     (source of truth)
  - inputs/figma-variables.json     (Figma state)
  - tools/knowledge/figma-variable-scoping-rules.md (human-readable; rules encoded below)
  - tools/3-figma-variables-review/knowledge/additional-rules.md (shadow/gradient
    exclusion + component-segment scoping)

Writes:
  - outputs/1-review/YYYY-MM-DD-HH-MM-{component}-figma-token-review.md
  - outputs/1-review/YYYY-MM-DD-HH-MM-{component}-figma-token-mapping.csv
  - inputs/mapped-component-tokens.csv   (fully overwritten every run, by design)
"""

import csv
import json
import os
import re
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
INPUTS_DIR = os.path.join(REPO_ROOT, "inputs")
OUTPUTS_DIR = os.path.join(REPO_ROOT, "outputs", "1-review")

INPUTS_JSON = os.path.join(INPUTS_DIR, "inputs.json")
CSV_PATH = os.path.join(INPUTS_DIR, "component-tokens.csv")
JSON_PATH = os.path.join(INPUTS_DIR, "figma-variables.json")
MAPPED_CSV_PATH = os.path.join(INPUTS_DIR, "mapped-component-tokens.csv")

STYLE_FOUNDATIONS = {"shadow", "gradient"}


def safe_segment(s):
    s = (s or "").strip().lower()
    s = re.sub(r"[\s/]+", "-", s)
    s = re.sub(r"[^a-z0-9_\-]+", "", s)
    return s or "component"


def load_component_name():
    with open(INPUTS_JSON) as f:
        data = json.load(f)
    return (data.get("componentName") or "").strip()


def read_csv_tokens(path):
    tokens = []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            full = (row.get("Full Token") or "").strip()
            if not full:
                continue
            tokens.append({
                "full_token": full,
                "foundation": (row.get("foundation") or "").strip().lower(),
                "component": (row.get("component") or "").strip().lower(),
                "all_modes": (row.get("All Modes") or "").strip(),
                "light_mode": (row.get("Light Mode") or "").strip(),
                "dark_mode": (row.get("Dark Mode") or "").strip(),
            })
    return tokens


def read_figma_variables(path):
    with open(path) as f:
        return json.load(f)


def csv_token_to_figma_name(full_token):
    t = full_token
    if t.startswith("affirm."):
        t = t[len("affirm."):]
    return t.replace(".", "/")


def component_segment(figma_name):
    parts = figma_name.split("/")
    return parts[1] if len(parts) > 1 else ""


def normalize_alias(name):
    if not name:
        return ""
    parts = name.split("/")
    return f"{parts[-2]}.{parts[-1]}" if len(parts) >= 2 else name


def normalize_csv_value(val):
    if not val:
        return ""
    parts = val.split(".")
    return f"{parts[-2]}.{parts[-1]}" if len(parts) >= 2 else val


def figma_mode_values(var):
    light, dark, all_modes = "", "", ""
    for _, mode_data in var.get("valuesByMode", {}).items():
        mode_name = (mode_data.get("modeName") or "").lower()
        value = mode_data.get("value")
        if isinstance(value, dict) and value.get("type") == "VARIABLE_ALIAS":
            short = normalize_alias(value.get("name", ""))
        elif value is None:
            short = ""
        else:
            short = str(value)
        if "light" in mode_name:
            light = short
        elif "dark" in mode_name:
            dark = short
        else:
            all_modes = short
    return all_modes, light, dark


def evaluate_scoping(var):
    """
    Returns list of (rule_desc, expected_scopes, mode, expected_hidden_or_None).
    Encodes tools/knowledge/figma-variable-scoping-rules.md. `hidden=None` means
    the rule file does not constrain hiddenFromPublishing.
    """
    name = var.get("name", "")
    collection = var.get("collection", "")
    rules = []

    # --- COLOR ---
    if re.match(r"^color/text/", name):
        rules.append(("color/text/* → scopes must equal [TEXT_FILL], hidden=false",
                      ["TEXT_FILL"], "equal", False))
    elif re.match(r"^color/icon/", name):
        rules.append(("color/icon/* → scopes must include SHAPE_FILL, hidden=false",
                      ["SHAPE_FILL"], "include", False))
    elif re.match(r"^color/bg/", name) or re.match(r"^color/fill/", name):
        rules.append(("color/bg|fill/* → scopes must equal [FRAME_FILL, SHAPE_FILL], hidden=false",
                      ["FRAME_FILL", "SHAPE_FILL"], "equal", False))
    elif re.match(r"^color/border/", name):
        rules.append(("color/border/* → scopes must equal [STROKE_COLOR], hidden=false",
                      ["STROKE_COLOR"], "equal", False))
    elif re.match(r"^color/divider/", name):
        rules.append(("color/divider/* → scopes must equal [STROKE_COLOR], hidden=true",
                      ["STROKE_COLOR"], "equal", True))
    elif re.match(r"^color/[^/]+/", name):
        # Component color (public API): color/{component}/…
        if "/text/" in name or name.endswith("/text"):
            rules.append(("color/{component}/…/text/… → [TEXT_FILL], hidden=true",
                          ["TEXT_FILL"], "equal", True))
        elif "/icon/" in name or name.endswith("/icon"):
            rules.append(("color/{component}/…/icon/… → include SHAPE_FILL, hidden=true",
                          ["SHAPE_FILL"], "include", True))
        elif "/bg/" in name or name.endswith("/bg"):
            rules.append(("color/{component}/…/bg/… → [FRAME_FILL, SHAPE_FILL], hidden=true",
                          ["FRAME_FILL", "SHAPE_FILL"], "equal", True))
        elif "/fill/" in name or name.endswith("/fill"):
            rules.append(("color/{component}/…/fill/… → [FRAME_FILL, SHAPE_FILL], hidden=true",
                          ["FRAME_FILL", "SHAPE_FILL"], "equal", True))
        elif "/border/" in name or name.endswith("/border") or "/border" in name:
            rules.append(("color/{component}/…/border… → [STROKE_COLOR], hidden=true",
                          ["STROKE_COLOR"], "equal", True))
        elif "/outline/" in name or name.endswith("/outline"):
            rules.append(("color/{component}/…/outline/… → [STROKE_COLOR], hidden=true",
                          ["STROKE_COLOR"], "equal", True))

    # --- SPACING ---
    if (collection == "spacing"
            or name.startswith("spacing/")
            or "/padding" in name
            or "/gap" in name
            or "/margin" in name):
        # Component-scoped spacing (spacing/{component}/…) → hidden=true
        hidden = True if (name.startswith("spacing/") and len(name.split("/")) >= 3) else None
        rules.append(("spacing → scopes must equal [GAP]"
                      + ("; component-scoped → hidden=true" if hidden else ""),
                      ["GAP"], "equal", hidden))

    # --- SIZE ---
    if name.startswith("semantic/size/"):
        rules.append(("semantic/size/* → [FONT_SIZE]",
                      ["FONT_SIZE"], "equal", None))
    if name.startswith("breakpoint/"):
        rules.append(("breakpoint/* → [WIDTH_HEIGHT], hidden=false",
                      ["WIDTH_HEIGHT"], "equal", False))
    if name.startswith("size/") and len(name.split("/")) >= 3:
        if "/border" in name:
            rules.append(("size/{component}/…/border… → [STROKE_FLOAT], hidden=true",
                          ["STROKE_FLOAT"], "equal", True))
        elif "/outline/" in name or name.endswith("/outline"):
            rules.append(("size/{component}/…/outline/… → [STROKE_FLOAT], hidden=true",
                          ["STROKE_FLOAT"], "equal", True))
        else:
            rules.append(("size/{component}/… (dimension) → [WIDTH_HEIGHT], hidden=true",
                          ["WIDTH_HEIGHT"], "equal", True))

    # --- RADIUS ---
    if name.startswith("radius/"):
        rules.append(("radius/* → [CORNER_RADIUS]",
                      ["CORNER_RADIUS"], "equal", None))

    # --- TYPOGRAPHY ---
    if "lineHeight" in name:
        rules.append(("name contains lineHeight → [LINE_HEIGHT]",
                      ["LINE_HEIGHT"], "equal", None))
    if "letterSpacing" in name:
        rules.append(("name contains letterSpacing → [LETTER_SPACING]",
                      ["LETTER_SPACING"], "equal", None))
    if "fontFamily" in name:
        rules.append(("name contains fontFamily → [FONT_FAMILY]",
                      ["FONT_FAMILY"], "equal", None))
    if "weight" in name:
        rules.append(("name contains weight → [FONT_STYLE]",
                      ["FONT_STYLE"], "equal", None))

    return rules


def check_scoping(var):
    actual_scopes = sorted(var.get("scopes", []))
    actual_hidden = var.get("hiddenFromPublishing", False)
    violations = []
    for rule_desc, expected, mode, expected_hidden in evaluate_scoping(var):
        expected_sorted = sorted(expected) if expected else []
        if mode == "include":
            scope_ok = all(s in actual_scopes for s in expected_sorted)
        else:
            scope_ok = actual_scopes == expected_sorted
        hidden_ok = True if expected_hidden is None else (actual_hidden == expected_hidden)
        if not scope_ok or not hidden_ok:
            violations.append({
                "rule": rule_desc,
                "expected_scopes": expected_sorted,
                "expected_scope_mode": mode,
                "actual_scopes": actual_scopes,
                "scope_ok": scope_ok,
                "expected_hidden": expected_hidden,
                "actual_hidden": actual_hidden,
                "hidden_ok": hidden_ok,
            })
    return violations


def main():
    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    component_name = load_component_name() or "component"
    safe_comp = safe_segment(component_name)
    ts = datetime.now().strftime("%Y-%m-%d-%H-%M")
    md_path = os.path.join(OUTPUTS_DIR, f"{ts}-{safe_comp}-figma-token-review.md")
    dated_csv_path = os.path.join(OUTPUTS_DIR, f"{ts}-{safe_comp}-figma-token-mapping.csv")

    csv_tokens = read_csv_tokens(CSV_PATH)
    figma_vars = read_figma_variables(JSON_PATH)

    # In-scope component segments are derived from the CSV itself — this supports
    # reviews that include subcomponents (e.g. dropdown + listbox).
    in_scope_components = sorted({
        component_segment(csv_token_to_figma_name(ct["full_token"]))
        for ct in csv_tokens
        if component_segment(csv_token_to_figma_name(ct["full_token"]))
    })

    figma_by_name = {v["name"]: v for v in figma_vars}
    figma_by_norm = {v["name"].lower().replace(" ", "_"): v for v in figma_vars}

    missing_in_figma = []
    excluded_missing = []
    naming_discrepancies = []
    assignment_discrepancies = []
    matched_pairs = []
    matched_ids = set()

    for ct in csv_tokens:
        csv_fname = csv_token_to_figma_name(ct["full_token"])
        var = figma_by_name.get(csv_fname)
        if not var:
            var = figma_by_norm.get(csv_fname.lower().replace(" ", "_"))
            if var and var["name"] != csv_fname:
                naming_discrepancies.append({
                    "csv_token": ct["full_token"],
                    "csv_figma_name": csv_fname,
                    "figma_name": var["name"],
                    "issue": "Differs only by case/spacing",
                })
        if not var:
            if ct["foundation"] in STYLE_FOUNDATIONS:
                excluded_missing.append(ct)
            else:
                missing_in_figma.append(ct)
            continue

        matched_pairs.append((ct, var))
        matched_ids.add(var.get("id"))

        all_modes, light, dark = figma_mode_values(var)
        if ct["light_mode"] and normalize_csv_value(ct["light_mode"]) != light:
            assignment_discrepancies.append({
                "csv_token": ct["full_token"], "mode": "Light",
                "csv_value": ct["light_mode"], "figma_value": light or "(none)",
            })
        if ct["dark_mode"] and normalize_csv_value(ct["dark_mode"]) != dark:
            assignment_discrepancies.append({
                "csv_token": ct["full_token"], "mode": "Dark",
                "csv_value": ct["dark_mode"], "figma_value": dark or "(none)",
            })
        if ct["all_modes"] and normalize_csv_value(ct["all_modes"]) != all_modes:
            assignment_discrepancies.append({
                "csv_token": ct["full_token"], "mode": "All Modes",
                "csv_value": ct["all_modes"], "figma_value": all_modes or "(none)",
            })

    extra_in_figma = [
        v for v in figma_vars
        if component_segment(v["name"]) in in_scope_components
        and v.get("id") not in matched_ids
    ]

    scoping_violations = []
    for ct, var in matched_pairs:
        for viol in check_scoping(var):
            scoping_violations.append({
                "csv_token": ct["full_token"],
                "figma_name": var["name"],
                "scopes": var.get("scopes", []),
                "hidden": var.get("hiddenFromPublishing", False),
                **viol,
            })

    # --- Write mapping CSV (dated + inputs) ---
    mapping_rows = []
    for ct in csv_tokens:
        csv_fname = csv_token_to_figma_name(ct["full_token"])
        var = figma_by_name.get(csv_fname) or figma_by_norm.get(csv_fname.lower().replace(" ", "_"))
        mapping_rows.append({
            "csv_token": ct["full_token"],
            "figma_name": var["name"] if var else "",
            "figma_id": var["id"] if var else "",
        })
    for path in (dated_csv_path, MAPPED_CSV_PATH):
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["csv_token", "figma_name", "figma_id"])
            w.writeheader()
            w.writerows(mapping_rows)

    # --- Write Markdown report ---
    figma_in_scope = [v for v in figma_vars if component_segment(v["name"]) in in_scope_components]
    lines = []
    lines.append(f"# Figma Variables Review — {component_name}")
    lines.append("")
    lines.append(f"**Date:** {ts}")
    lines.append("")
    lines.append("## Inputs used")
    lines.append("")
    lines.append(f"- componentName: `{component_name}` (filename segment: `{safe_comp}`)")
    lines.append("- Additional rules (`tools/3-figma-variables-review/knowledge/additional-rules.md`): **present and applied**.")
    lines.append("  - Shadow/gradient composite tokens excluded from the missing-in-Figma check (Figma styles, not variables).")
    lines.append(f"  - Component-segment scoping applied: only Figma variables whose component segment is in `{in_scope_components}` were considered for Extra-in-Figma and Task 2. The in-scope set was derived from the component segments present in the CSV.")
    lines.append(f"- CSV tokens read: {len(csv_tokens)}")
    lines.append(f"- Figma variables read: {len(figma_vars)}")
    lines.append(f"- Figma variables with in-scope component segment: {len(figma_in_scope)}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---|")
    lines.append(f"| CSV tokens | {len(csv_tokens)} |")
    lines.append(f"| Matched | {len(matched_pairs)} |")
    lines.append(f"| Missing in Figma | {len(missing_in_figma)} |")
    lines.append(f"| Shadow/gradient excluded from missing check | {len(excluded_missing)} |")
    lines.append(f"| Extra in Figma (component-scoped) | {len(extra_in_figma)} |")
    lines.append(f"| Naming discrepancies | {len(naming_discrepancies)} |")
    lines.append(f"| Assignment discrepancies | {len(assignment_discrepancies)} |")
    lines.append(f"| Scoping violations | {len(scoping_violations)} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Task 1: CSV vs Figma")
    lines.append("")

    lines.append("### Missing in Figma")
    lines.append("")
    if missing_in_figma:
        lines.append("| CSV Token | Expected Figma Name |")
        lines.append("|---|---|")
        for ct in missing_in_figma:
            lines.append(f"| `{ct['full_token']}` | `{csv_token_to_figma_name(ct['full_token'])}` |")
    else:
        lines.append("None.")
    lines.append("")
    if excluded_missing:
        lines.append("_Excluded per additional-rules.md (shadow/gradient are Figma styles, not variables):_")
        for ct in excluded_missing:
            lines.append(f"- `{ct['full_token']}`")
        lines.append("")

    lines.append("### Extra in Figma")
    lines.append("")
    if extra_in_figma:
        lines.append("Figma variables with in-scope component segment that are not listed in the CSV:")
        lines.append("")
        lines.append("| Figma Variable | Collection | ID |")
        lines.append("|---|---|---|")
        for v in extra_in_figma:
            lines.append(f"| `{v['name']}` | {v.get('collection','')} | {v.get('id','')} |")
        lines.append("")
        lines.append(f"_Per additional-rules.md, only Figma variables with component segment in `{in_scope_components}` were considered._")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("### Naming discrepancies")
    lines.append("")
    if naming_discrepancies:
        lines.append("| CSV Token | Expected Figma Name | Actual Figma Name | Issue |")
        lines.append("|---|---|---|---|")
        for nd in naming_discrepancies:
            lines.append(f"| `{nd['csv_token']}` | `{nd['csv_figma_name']}` | `{nd['figma_name']}` | {nd['issue']} |")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("### Assignment discrepancies")
    lines.append("")
    if assignment_discrepancies:
        lines.append("| CSV Token | Mode | CSV Value | Figma Value |")
        lines.append("|---|---|---|---|")
        for ad in assignment_discrepancies:
            lines.append(f"| `{ad['csv_token']}` | {ad['mode']} | `{ad['csv_value']}` | `{ad['figma_value']}` |")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Task 2: Scoping rule violations")
    lines.append("")
    lines.append(f"_Evaluated {len(matched_pairs)} matched variables (tokens present in both CSV and Figma, component segment in `{in_scope_components}`)._")
    lines.append("")
    if scoping_violations:
        for sv in scoping_violations:
            lines.append(f"#### `{sv['figma_name']}`")
            lines.append("")
            lines.append(f"- CSV Token: `{sv['csv_token']}`")
            lines.append(f"- Rule: {sv['rule']}")
            if not sv["scope_ok"]:
                mode_label = "include" if sv["expected_scope_mode"] == "include" else "equal"
                lines.append(f"- Scopes: expected ({mode_label}) `{sv['expected_scopes']}`, actual `{sv['actual_scopes']}`")
            if not sv["hidden_ok"]:
                lines.append(f"- hiddenFromPublishing: expected `{sv['expected_hidden']}`, actual `{sv['actual_hidden']}`")
            lines.append("")
    else:
        lines.append("None.")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Token mapping")
    lines.append("")
    lines.append(f"- Dated: `outputs/1-review/{os.path.basename(dated_csv_path)}`")
    lines.append("- Inputs (overwritten): `inputs/mapped-component-tokens.csv`")
    lines.append("")

    with open(md_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Component: {component_name} (segment: {safe_comp})")
    print(f"In-scope component segments: {in_scope_components}")
    print(f"CSV tokens: {len(csv_tokens)}  Figma variables: {len(figma_vars)}  In-scope Figma: {len(figma_in_scope)}")
    print(f"Matched: {len(matched_pairs)}  Missing: {len(missing_in_figma)}  Excluded(style): {len(excluded_missing)}  Extra: {len(extra_in_figma)}")
    print(f"Naming: {len(naming_discrepancies)}  Assignment: {len(assignment_discrepancies)}  Scoping: {len(scoping_violations)}")
    print(f"Report: {md_path}")
    print(f"Mapping (dated): {dated_csv_path}")
    print(f"Mapping (inputs): {MAPPED_CSV_PATH}")


if __name__ == "__main__":
    main()
