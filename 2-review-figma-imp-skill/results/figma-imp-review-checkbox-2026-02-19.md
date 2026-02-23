# Figma Implementation Review — Checkbox

**Date:** 2026-02-19

---

## Inputs Used

| Input | Value |
|-------|-------|
| Component name | checkbox |
| Component URL | https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/VZAyxA1GEOoWqJohc0i1l0/…?node-id=3638-23291 |
| Data source | **Figma MCP** (`get_variable_defs` + `get_design_context`) |
| Component tokens CSV | Present (103 tokens) |
| Figma variables JSON | Not present (not required — MCP provided variable data) |
| Naming rules | Present (`knowledge/naming-rules.md`) |
| Additional rules | Present (`knowledge/additional-rules.md`) |

---

## 1. Token Coverage

**Source:** Component tokens CSV (`inputs/component-tokens.csv`) compared against variables returned by Figma MCP `get_variable_defs`.

### Tokens not used — Border width per-interaction tokens (15 tokens)

The component reuses `size/checkbox/indicator/border/width/selected/resting` and `…/unselected/resting` across all interaction states (hover, pressed, disabled) instead of binding the per-interaction border width tokens. Only `selected/resting`, `unselected/resting`, and `selected/focus_visible` border width tokens are applied.

| # | CSV Token (figma_name) | figma_id |
|---|------------------------|----------|
| 1 | `size/checkbox/indicator/border/width/error_selected/resting` | VariableID:19700:3921 |
| 2 | `size/checkbox/indicator/border/width/error_selected/hover` | VariableID:19700:3922 |
| 3 | `size/checkbox/indicator/border/width/error_selected/pressed` | VariableID:19700:3923 |
| 4 | `size/checkbox/indicator/border/width/error_selected/focus_visible` | VariableID:19700:3924 |
| 5 | `size/checkbox/indicator/border/width/error_unselected/resting` | VariableID:19700:3916 |
| 6 | `size/checkbox/indicator/border/width/error_unselected/hover` | VariableID:19700:3917 |
| 7 | `size/checkbox/indicator/border/width/error_unselected/pressed` | VariableID:19700:3918 |
| 8 | `size/checkbox/indicator/border/width/error_unselected/focus_visible` | VariableID:19700:3919 |
| 9 | `size/checkbox/indicator/border/width/selected/disabled` | VariableID:15554:32170 |
| 10 | `size/checkbox/indicator/border/width/selected/hover` | VariableID:15554:32167 |
| 11 | `size/checkbox/indicator/border/width/selected/pressed` | VariableID:15554:32168 |
| 12 | `size/checkbox/indicator/border/width/unselected/disabled` | VariableID:15554:32166 |
| 13 | `size/checkbox/indicator/border/width/unselected/focus_visible` | VariableID:15554:32165 |
| 14 | `size/checkbox/indicator/border/width/unselected/hover` | VariableID:15554:32163 |
| 15 | `size/checkbox/indicator/border/width/unselected/pressed` | VariableID:15554:32164 |

**Issue:** Each interaction variant should bind its own border width token so that border width can vary per interaction state. Currently, all non-focus selected variants use `…/selected/resting` (0 px) and all non-focus unselected variants use `…/unselected/resting` (2 px).

### Tokens not used — Unselected icon color tokens (9 tokens)

Unselected checkbox variants do not contain a checkmark icon node (they use a "visuals" node for border/background only). Because the icon node does not exist in unselected variants, icon color tokens for unselected states cannot be bound.

| # | CSV Token (figma_name) | figma_id |
|---|------------------------|----------|
| 1 | `color/checkbox/indicator/icon/unselected/resting` | VariableID:15324:5330 |
| 2 | `color/checkbox/indicator/icon/unselected/hover` | VariableID:15554:32174 |
| 3 | `color/checkbox/indicator/icon/unselected/pressed` | VariableID:15554:32175 |
| 4 | `color/checkbox/indicator/icon/unselected/focus_visible` | VariableID:15554:32176 |
| 5 | `color/checkbox/indicator/icon/unselected/disabled` | VariableID:15324:5331 |
| 6 | `color/checkbox/indicator/icon/error_unselected/resting` | VariableID:15554:32180 |
| 7 | `color/checkbox/indicator/icon/error_unselected/hover` | VariableID:15554:32181 |
| 8 | `color/checkbox/indicator/icon/error_unselected/pressed` | VariableID:15554:32182 |
| 9 | `color/checkbox/indicator/icon/error_unselected/focus_visible` | VariableID:15554:32183 |

**Issue:** These tokens are defined in the CSV but cannot be applied because the icon node is absent in unselected variants. If unselected states are intended to have a hidden (transparent) checkmark icon, the node should exist with these tokens bound so that values are controlled by variables rather than by node absence.

### Tokens not used — Outline width for non-focus states (3 tokens)

The component only renders the outline ring on the `Focus visible` interaction variant. Outline width tokens for `hover`, `pressed`, and `resting` are not bound anywhere.

| # | CSV Token (figma_name) | figma_id |
|---|------------------------|----------|
| 1 | `size/checkbox/outline/width/hover` | VariableID:15324:5325 |
| 2 | `size/checkbox/outline/width/pressed` | VariableID:15324:5328 |
| 3 | `size/checkbox/outline/width/resting` | VariableID:6056:9881 |

**Issue:** These three outline width tokens are in the CSV but are not applied in the component. The outline is only visible during focus so these may be intentionally unused, but they should be bound (with value 0) to ensure outline width is always token-controlled.

### Wrong variable applied (2 tokens)

These CSV tokens are not used because a **different** variable is bound in their place.

| # | CSV Token (expected) | Actually used in Figma | Variant affected |
|---|---------------------|----------------------|-----------------|
| 1 | `color/checkbox/label/text/unselected/focus_visible` (VariableID:15554:32190) | `color/checkbox/label/text/selected/focus_visible` | Error=False, Selected=False, Interaction=Focus visible (node 19740:9731) |
| 2 | `color/checkbox/indicator/border/error_selected/focus_visible` (VariableID:15254:11142) | `color/checkbox/indicator/border/selected/focus_visible` | Error=True, Selected=True, Interaction=Focus visible (node 19740:9834) |

**Issue:** These are likely copy/paste errors. The unselected focus_visible label text should use the `unselected` token, and the error_selected focus_visible border should use the `error_selected` token.

### Tokens with no figma_name in CSV (2 tokens — not scored as issues)

| # | CSV Token | Notes |
|---|-----------|-------|
| 1 | `affirm.color.checkbox.container.outline.focus_visible` | Likely corresponds to `color/checkbox/outline/focus_visible` which IS used in the component. CSV is missing the figma_name and figma_id for matching. |
| 2 | `affirm.size.checkbox.outline.width.focus_visible` | Likely corresponds to `size/checkbox/outline/width/focus_outline` which IS used. Note the naming mismatch: CSV says `focus_visible`, Figma variable says `focus_outline`. |

**Note:** These tokens appear to be applied in the component under slightly different names. The CSV should be updated with correct figma_name and figma_id values.

### Position tokens

No position tokens were found in the CSV. The additional-rules exception for position tokens did not apply.

### Token coverage summary

- **103** tokens in CSV
- **2** tokens with no figma_name (cannot match; likely present under different names)
- **29** tokens with figma_names not found in variable defs (**issues**)
  - 15 border-width per-interaction tokens
  - 9 unselected icon color tokens
  - 3 outline-width non-focus tokens
  - 2 wrong-variable-applied tokens

---

## 2. Raw Values and Direct Base Tokens

### Raw values (no variable binding)

| # | Node / Layer | Property | Raw Value | Expected Variable | Variants Affected |
|---|-------------|----------|-----------|-------------------|-------------------|
| 1 | "wrap" (19740:9717) | gap | `8px` | `spacing/checkbox/gap_x` | Error=False, Selected=True, Interaction=Focus visible |
| 2 | "wrap" (19740:9831) | gap | `8px` | `spacing/checkbox/gap_x` | Error=True, Selected=True, Interaction=Focus visible |
| 3 | "wrap" (19740:9726) | gap | `8px` | `spacing/checkbox/gap_x` | Error=False, Selected=False, Interaction=Focus visible |
| 4 | "wrap" (19740:9838) | gap | `8px` | `spacing/checkbox/gap_x` | Error=True, Selected=False, Interaction=Focus visible |

**Issue:** All four Focus visible variants have a raw `8px` gap on the inner "wrap" div instead of the `spacing/checkbox/gap_x` variable. Non-focus variants correctly bind this variable. The outer container in focus variants has `spacing/checkbox/gap_x` bound (with value 0), but the inner "wrap" div lost the variable binding.

### Direct base tokens (`base/` prefix)

None. No variables starting with `base/` are used in the component.

### Additional observations (not scored as issues)

| Variable | Value | Notes |
|----------|-------|-------|
| `size/button/medium/icon/all` | 20 | A **button** token used inside the checkbox component. May be inherited from a shared icon instance rather than intentionally applied. |
| `size/025` | 2 | A primitive size token (not `base/`-prefixed, so not flagged by rules). Used somewhere in the component structure. |
| `component/checkbox/all` | 4 | Used for border-radius on `_Checkbox.base` in unselected states. Not in the component tokens CSV. May be intentional but should be documented if so. |

---

## 3. Typography

### Typography style used

The component uses one typography style across all variants:

> **`typography/body-Large`** — Font family: `semantic/fontFamily/body` ("Calibre"), weight: `semantic/weight/body/Default` (Regular/400), size: `semantic/size/body/Large` (18px), line-height: `semantic/lineHeight/body/Large` (27px), letter-spacing: `semantic/letterSpacing/body/Large` (0px).

This is a **named library style** (not ad-hoc font properties), which is correct.

### Typography set compliance

| # | Style Name | Expected Prefix | Status |
|---|-----------|----------------|--------|
| 1 | `typography/body-Large` | `affirm.typography/component/` | **Issue** — Does not start with `affirm.typography/component/` |

**Issue:** Per additional rules, all typography in components must come from the `affirm.typography/component/` set. The style `typography/body-Large` does not match this requirement. It should reference a style from `affirm.typography/component/` (e.g. `affirm.typography/component/body-Large` or equivalent).

---

## 4. Component Property Naming

### Component properties found

From the component set (via `data-name` attributes and generated props):

| Property | Type | Values |
|----------|------|--------|
| Error | Variant (boolean-like) | True, False |
| Selected | Variant (boolean-like) | True, False |
| Interaction | Variant | Resting, Hover, Pressed, Focus visible, Disabled |
| Has Label | Boolean | true, false |
| Label | Text | "Label" |

### Naming rule violations

| # | Property | Value | Rule Violated | Expected |
|---|----------|-------|--------------|----------|
| 1 | Interaction | **Focus visible** | Title Case for all values | **Focus Visible** (capital "V") |

**Issue:** The value "Focus visible" uses a lowercase "v". Per global naming rules, all property names and values must use Title Case.

### Compliant properties

- **Error** — Explicitly allowed per naming rules: "For interactive elements that can error, may have a boolean named 'Error' that has values 'True' and 'False'." Compliant.
- **Selected** — Boolean-like variant with True/False values. The name is an adjective rather than a noun (variant rules prefer nouns), but this is a common pattern for boolean-like variants representing state. Borderline — consider renaming to "Selection" for strict noun compliance, but current usage is understandable.
- **Interaction** — Correctly uses "Interaction" instead of "State" per specific rules. "Disabled" is correctly a value within this property. Compliant.
- **Has Label** — Boolean starting with "Has" + noun. Compliant.
- **Label** — Text property named by role. Compliant.

---

## Summary

| Category | Issues |
|----------|--------|
| 1. Token coverage | **29** tokens not used (15 border-width, 9 unselected-icon, 3 outline-width, 2 wrong-variable) |
| 2. Raw values / base tokens | **4** raw gap values in Focus visible variants |
| 3. Typography | **1** style not from `affirm.typography/component/` set |
| 4. Property naming | **1** value not in Title Case ("Focus visible") |
| **Total** | **35 issues** |

### Critical issues

- **Wrong variables applied** (Check 1, items 1–2 in "Wrong variable applied"): The unselected focus_visible label uses the selected token, and the error_selected focus_visible border uses the non-error token. These would cause incorrect colors if the selected and unselected values ever diverge.
- **Raw gap in Focus visible variants** (Check 2): The `spacing/checkbox/gap_x` variable is not bound on the inner "wrap" layer in all four Focus visible variants, meaning gap changes via the variable would not propagate to these states.

### Non-critical observations

- 2 CSV tokens have no figma_name/id and could not be matched by variable ID; they appear to be present under slightly different Figma variable names (naming mismatch between CSV and Figma).
- 3 non-checkbox variables (`size/button/medium/icon/all`, `size/025`, `component/checkbox/all`) are used in the component but are not in the component tokens CSV.
- "Selected" as a variant name is an adjective rather than a noun — borderline per naming rules.
