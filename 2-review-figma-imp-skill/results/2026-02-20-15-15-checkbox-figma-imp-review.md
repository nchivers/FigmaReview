# Figma Component Implementation Review — Checkbox

## Inputs Used

| Input | Value / Status |
|-------|---------------|
| **componentName** | checkbox |
| **componentUrl** | `https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/VZAyxA1GEOoWqJohc0i1l0/…?node-id=3638-23291` |
| **Data source** | Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| **componentTokensCsv** | Present (inputs/component-tokens.csv — 100 tokens) |
| **figmaVariablesJson** | Listed in inputs.json but not required; variable names resolved from MCP responses |
| **namingRules** | Present (knowledge/naming-rules.md) |
| **additionalRules** | Present (knowledge/additional-rules.md) |

### Subcomponent classification

| Instance | Classification | Rationale |
|----------|---------------|-----------|
| `_Checkbox.base` | **Not a subcomponent** (FRAME node) | Metadata confirms type is `<frame>`, not `<instance>`. It is structural markup within each variant, not an instance of another component. |
| `icon_checkmark_small` | **Override-only** (assumed remote / published) | Instance of component `3696:2458`. Named as a generic icon, consistent with a shared icon library. MCP metadata does not expose local/published status; treated as override-only per the additional rules guidance to assume override-only when status cannot be determined. |

No owned (local, unpublished) subcomponents were identified. All review checks below apply to the root component only.

---

## 1. Token Coverage

**12 tokens from the CSV are not applied as variables in the component.**

### Missing border-width size tokens (11)

The component reuses a small set of border-width tokens (e.g. `selected/resting` and the non-error `unselected/{state}` equivalents) across multiple interaction and error states, instead of binding the per-state tokens defined in the CSV.

| # | Missing token (figma_name) | figma_id | Notes |
|---|---------------------------|----------|-------|
| 1 | `size/checkbox/indicator/border/width/error_selected/resting` | VariableID:19700:3921 | Uses `selected/resting` instead |
| 2 | `size/checkbox/indicator/border/width/error_selected/hover` | VariableID:19700:3922 | Uses `selected/resting` instead |
| 3 | `size/checkbox/indicator/border/width/error_selected/pressed` | VariableID:19700:3923 | Uses `selected/resting` instead |
| 4 | `size/checkbox/indicator/border/width/error_selected/focus_visible` | VariableID:19700:3924 | Uses `selected/focus_visible` instead |
| 5 | `size/checkbox/indicator/border/width/error_unselected/resting` | VariableID:19700:3916 | Uses `unselected/resting` instead |
| 6 | `size/checkbox/indicator/border/width/error_unselected/hover` | VariableID:19700:3917 | Uses `unselected/hover` instead |
| 7 | `size/checkbox/indicator/border/width/error_unselected/pressed` | VariableID:19700:3918 | Uses `unselected/pressed` instead |
| 8 | `size/checkbox/indicator/border/width/error_unselected/focus_visible` | VariableID:19700:3919 | Uses `unselected/focus_visible` instead |
| 9 | `size/checkbox/indicator/border/width/selected/hover` | VariableID:15554:32167 | Uses `selected/resting` instead |
| 10 | `size/checkbox/indicator/border/width/selected/pressed` | VariableID:15554:32168 | Uses `selected/resting` instead |
| 11 | `size/checkbox/indicator/border/width/selected/disabled` | VariableID:15554:32170 | Uses `selected/resting` instead |

### Missing border-color token (1)

| # | Missing token (figma_name) | figma_id | Notes |
|---|---------------------------|----------|-------|
| 12 | `color/checkbox/indicator/border/error_selected/focus_visible` | VariableID:15254:11142 | Error=True, Selected=True, Focus visible variant uses `color/checkbox/indicator/border/selected/focus_visible` (non-error equivalent) instead |

### Excluded per additional rules

- **`spacing/checkbox/container/outline/offset/focus_visible`** (VariableID:19700:3927) — Excluded from unused-token reporting per the **position token rule**. This token controls the focus-visible outline offset, which in Figma is achieved through absolute positioning (x/y constraints). Figma does not allow variables to be bound to position properties.

---

## 2. Raw Values and Direct Base Tokens

### Raw values (hex / non-variable)

No issues. All color, spacing, border-radius, border-width, and stroke properties in the component use variable references (confirmed via `get_variable_defs` and `get_design_context` CSS custom property bindings).

### Direct base tokens (`base/` prefix)

No issues. None of the variables used in the component have names starting with `base/`.

### Note

- The variable `size/025` (value: 2) appears in `get_variable_defs`. It does not start with `base/` and is likely referenced as an internal alias by `size/checkbox/outline/width/focus_visible`. Not flagged as an issue.

---

## 3. Typography

**1 issue.**

- **Issue:** The component uses typography style **`typography/body-Large`** for all label text nodes. Per the additional rules, all typography must come from the **`affirm.typography/component/`** set (style names must begin with `affirm.typography/component/`). The style `typography/body-Large` does **not** begin with `affirm.typography/component/`.
  - Affected nodes: All label `<p>` text nodes across every variant (e.g. nodes `3638:23295`, `19717:3925`, `19717:3974`, `19740:9803`, `19740:9809`, etc.)
  - Current style: `typography/body-Large`
  - Expected: A style beginning with `affirm.typography/component/`

---

## 4. Component Property Naming

**1 issue.**

### Properties and values

| Property | Type | Values | Status |
|----------|------|--------|--------|
| **Error** | Variant (boolean-like) | True, False | Pass |
| **Selected** | Variant (boolean-like) | True, False | Pass |
| **Interaction** | Variant | Resting, Hover, Pressed, **Focus visible**, Disabled | **Issue** |
| **Has Label** | Boolean | true, false | Pass |
| **Label** | Text | (editable) | Pass |

### Issues

- **"Focus visible" should be "Focus Visible"** — The Interaction value "Focus visible" uses a lowercase "v". Per the naming rules, all property values must use **Title Case**. The correct value is **"Focus Visible"**.

---

## Summary

| Category | Issues |
|----------|--------|
| 1. Token coverage | **12** (11 border-width size tokens + 1 border-color token not applied; 1 spacing token excluded per position rule) |
| 2. Raw values / base tokens | **0** |
| 3. Typography | **1** (style not from `affirm.typography/component/` set) |
| 4. Component property naming | **1** ("Focus visible" not Title Case) |
| **Total** | **14 issues** |

### Key observations

- The bulk of the token-coverage issues (11 of 12) follow the same pattern: **border-width tokens for error states and non-resting selected interaction states are not individually bound**. The component reuses `selected/resting` for all selected interaction states and uses the non-error equivalent tokens for all error states. If the design intent is for these border widths to vary independently per state (which is why distinct tokens exist), each variant should bind the corresponding token.
- The single missing **color** token (`color/checkbox/indicator/border/error_selected/focus_visible`) follows the same pattern — the error-selected focus-visible variant uses the non-error selected border color instead.
- The **typography** issue affects all text nodes uniformly — a single style change to an `affirm.typography/component/` style would resolve it.
- The **naming** issue is a single capitalization fix on one variant value.
