---
name: review-csv-tokens
description: Reviews a CSV of component-specific tokens against naming rules, assignment completeness, and logical token coverage. Use when reviewing component token CSVs, validating token naming, checking base-token assignments, or auditing for missing states (e.g. pressed, disabled, focus_visible).
---

# CSV Component Token Review

Review a CSV of component tokens against naming rules, assignment completeness, and logical coverage. Write findings to a single markdown file in `results/`.

---

## Inputs

Paths are relative to the skill root (`0-review-csv-tokens-skill/`).

| Source | Purpose |
|--------|--------|
| **inputs/inputs.json** | **Required.** Must include `componentName` (e.g. `link`, `button`). Used in the results filename. |
| **inputs/component-tokens.csv** | **Required.** CSV with one row per token. **One column per name segment** (no dot-separated full token). Segment columns plus assignment columns. |
| **knowledge/token-naming-rules.md** | **Required for naming check.** Defines each segment’s purpose, allowed values/patterns, and token-building examples. |

### CSV structure

- **Segment columns:** One column per name segment, in the order defined in token-naming-rules.md (e.g. Namespace, Foundation, Component, Variant, Size-Variant, Context, Polarity, Persistence, Part, Part-Variant, Subpart, Property, State, Interaction). Optional segments may be empty. Header names may vary (e.g. `namespace`, `foundation`, `component`); match by position or by normalizing header names.
- **Assignment columns (exact or normalized):**
  - **All Modes** — used for single-mode tokens (size, spacing, radius, position). Accept headers like `All Modes`, `all_modes`, `all`.
  - **Light Mode** / **Dark Mode** — used for dual-mode tokens (color, shadow). Accept headers like `Light Mode`, `Light`, `light`, and `Dark Mode`, `Dark`, `dark`.

---

## Review criteria

Run all three checks and report every finding. If an input is missing, note it and skip the checks that depend on it.

### 1. Naming issues

- **When:** `knowledge/token-naming-rules.md` exists and CSV has segment columns.
- **Check:** For each token row, compare each segment column value to the rules: purpose, allowed values/patterns, and token-building examples. Flag any segment that does not align (wrong value or violates an example).
- **Report:** List each token (reconstruct from segment columns for reference) and the segment(s) with the rule that was broken and the expected pattern or value. Mark as **naming issue**.

### 2. Tokens missing base-token assignments

- **When:** CSV has assignment columns (All Modes, Light Mode, Dark Mode).
- **Check:**
  - **Single-mode tokens:** Foundation column is one of `size`, `spacing`, `radius`, `position`, `motion`, `opacity`. These must have a non-empty **All Modes** value. Empty or whitespace-only = missing assignment.
  - **Dual-mode tokens:** Foundation is `color` or `shadow`. These must have non-empty **Light Mode** and **Dark Mode** values. Either empty = missing assignment.
- **Report:** List each token that is missing a required assignment, the missing column(s), and category. Mark as **missing assignment**.

### 3. Logically missing tokens

- **When:** CSV has enough tokens to infer patterns (e.g. same element with different states).
- **Check:** Infer state/variant patterns from existing tokens (e.g. `resting`, `hover`, `pressed`, `disabled`, `focus_visible`). For each (category, component, element) combination that has at least two states, consider the full set of expected states from the naming rules or from common patterns. If some states are present but others are missing (e.g. text has resting and hover but no pressed, disabled, or focus_visible), flag the missing ones as **potentially missing** for consideration.
- **Report:** List suggested token names or (category, component, element, state) that appear logically missing, with a short reason (e.g. “text has resting, hover; consider adding pressed, disabled, focus_visible”). Mark as **for consideration** (not a hard failure).

---

## Output

Write exactly one results file:

- **Path:** `results/csv-token-review-{component_name}-YYYY-MM-DD.md`
  - Use `componentName` from **inputs/inputs.json**. Sanitize for filenames: lowercase, replace spaces and invalid characters with hyphens (e.g. `Merchant Tile` → `merchant-tile`). If `componentName` is missing or empty, use `component`.
  - Use today’s date in ISO format for `YYYY-MM-DD`.
- **Contents:**
  1. **Inputs used** — componentName; paths to CSV and token-naming-rules (segment columns only).
  2. **1. Naming issues** — Per-token/segment violations of token-naming-rules.md, or “None” if no issues.
  3. **2. Tokens missing assignments** — Tokens missing required All Modes or Light/Dark Mode values, or “None”.
  4. **3. Logically missing tokens** — Suggested tokens or states for consideration, or “None”.
  5. **Summary** — Count of findings per category (naming, missing assignment, logically missing).

Use clear headings and bullet or table lists. If a section has no findings, write “None” or “No issues.” Do not modify input files; only write the results file.

---

## Workflow

1. Read **inputs/inputs.json** and get `componentName`. Resolve all paths relative to the skill root.
2. Read **inputs/component-tokens.csv**. Identify segment columns (by header name or position per token-naming-rules.md) and assignment columns (All Modes, Light Mode, Dark Mode) by header name.
3. Read **knowledge/token-naming-rules.md** to load segment definitions, allowed values, and token-building examples.
4. Run **Check 1 (naming):** For each row, read segment values from the segment columns. Validate each segment against the rules; record violations. Reconstruct token name from segments (e.g. for reporting) by joining non-empty segments with `.`.
5. Run **Check 2 (assignments):** For each row, read Foundation from the foundation segment column. Apply single-mode vs dual-mode rule; record tokens missing required assignments.
6. Run **Check 3 (logically missing):** Group tokens by (Foundation, Component, Part/Property as appropriate). For each group with multiple Interaction (or State) values, compare to full set of expected states; list suggested missing tokens for consideration.
7. Write **results/csv-token-review-{component_name}-YYYY-MM-DD.md** with inputs used, the three sections above, and the summary.

Ensure the **results** directory exists before writing (create it if necessary).
