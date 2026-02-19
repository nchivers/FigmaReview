# Figma Implementation Review — Link

**Date:** 2026-02-19

---

## Inputs Used

| Input | Value |
|-------|-------|
| componentName | link |
| componentUrl | https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/2qvJPV2B0c8o8TJqFAdVqv/…?node-id=3672-620 |
| Data source | Figma MCP (get_variable_defs, get_design_context, get_screenshot) |
| componentTokensCsv | inputs/component-tokens.csv (32 tokens) |
| figmaVariablesJson | Not provided |
| namingRules | knowledge/naming-rules.md |
| additionalRules | knowledge/additional-rules.md |

---

## 1. Token Coverage

**All 32 tokens from the CSV are present in the component's used variables.** No missing tokens.

Tokens verified (all found in get_variable_defs response):

- **Color (16):** color/link/text/{resting,hover,pressed,focus_visible,disabled}, color/link/container/bg/{resting,hover,pressed,focus_visible,disabled}, color/link/icon/{resting,hover,pressed,focus_visible,disabled}, color/link/outline/focus_visible
- **Radius (10):** radius/link/container/top/{resting,hover,pressed,focus_visible,disabled}, radius/link/container/bottom/{resting,hover,pressed,focus_visible,disabled}
- **Size (4):** size/link/{large,medium,small}/icon/all, size/link/outline/width/focus_visible
- **Spacing (2):** spacing/link/gap_x, spacing/link/outline/offset/focus_visible

No position tokens in the CSV, so no exclusions were needed per the position-token additional rule.

**Issues: None**

---

## 2. Raw Values and Direct Base Tokens

### Raw values

| Node / Layer | Property | Raw Value | Notes |
|---|---|---|---|
| Focus_visible outer wrapper (all sizes: nodes 19056:6266, 19056:6270, 19056:6262) | border-radius (top-left, top-right) | `10px` | The focus outline wrapper uses a hardcoded 10px top-left and top-right border-radius instead of a variable. This appears to be a calculated value (8px inner radius + 2px outline offset) but is not bound to a variable. |

### Direct base tokens

No variables starting with `base/` were detected. All variable names use component-level or semantic paths (e.g., `color/link/...`, `radius/link/...`, `semantic/...`).

### Subcomponent notes

The `icon_new_window` instances do not start with `.` or `_` and are treated as external components per additional rules. Their internal structure was not reviewed. All icon instances show a 24px container size in the generated code; the icon size tokens (size/link/{large,medium,small}/icon/all with values 20, 16, 14) are confirmed as used by get_variable_defs, so the binding appears correct even though the code generator renders a static 24px.

**Issues: 1** (raw 10px border-radius on focus outline wrapper)

---

## 3. Typography

### Library styles used

The component uses three typography styles returned by get_variable_defs:

| Style Name | Details |
|---|---|
| `typography/body/support/Large • Link` | Calibre Medium, 18/27, 0 letter-spacing |
| `typography/body/support/Medium • Link` | Calibre Medium, 16/24, 0 letter-spacing |
| `typography/body/support/Small • Link` | Calibre Medium, 14/21, 0 letter-spacing |

All three are **defined library styles** (not ad-hoc font settings) — individual typography attributes (font family, size, weight, line height, letter spacing) are bound to semantic variables (e.g., `semantic/fontFamily/body`, `semantic/size/body/Medium`).

### Typography set compliance (additional rule)

Per additional rules, all typography must come from the `affirm.typography/component/` set. The style names above start with `typography/body/support/`, **not** `affirm.typography/component/`.

| Style Name | Expected Prefix | Actual Prefix | Status |
|---|---|---|---|
| typography/body/support/Large • Link | affirm.typography/component/ | typography/body/support/ | **Issue** |
| typography/body/support/Medium • Link | affirm.typography/component/ | typography/body/support/ | **Issue** |
| typography/body/support/Small • Link | affirm.typography/component/ | typography/body/support/ | **Issue** |

**Note:** The style names returned by Figma MCP may use a different naming format than what appears in the Figma style library panel. If the library styles are actually published under the `affirm.typography/component/` collection but the MCP returns a shortened path, this may be a false positive. Verify in Figma directly.

**Issues: 3** (typography styles do not match required `affirm.typography/component/` prefix)

---

## 4. Component Property Naming

The component exposes the following properties (inferred from get_design_context variant data):

| Property | Type | Values |
|---|---|---|
| Size | Variant | Large, Medium, Small |
| Interaction | Variant | Resting, Hover, Pressed, Focus_visible, Disabled |
| External Link | Boolean | true, false |
| Link Text | Text | (editable, default: "Inline link text") |

### Findings

| Property | Actual Name/Value | Rule Violated | Expected | Status |
|---|---|---|---|---|
| Interaction | Value: **Focus_visible** | "Use spaces, not slashes, pipes, or punctuation" and "Use Title Case" | **Focus Visible** | **Issue** |
| External Link (boolean) | Property name: **External Link** | Boolean properties "must start with **Has**" | **Has External Link** | **Issue** |

### Compliant properties

- **Size** — Title Case noun, clear semantic values (Large, Medium, Small). ✓
- **Interaction** — Title Case noun (matches rule "Use 'Interaction' instead of 'State'"). Values Resting, Hover, Pressed, Disabled are correct. Disabled is correctly a value of Interaction, not a separate boolean. ✓
- **Link Text** — Describes the role of the text, not generic. ✓

**Issues: 2** (Focus_visible naming; boolean missing "Has" prefix)

---

## Summary

| Category | Issues |
|---|---|
| 1. Token coverage | **0** — All 32 tokens applied |
| 2. Raw values / base tokens | **1** — Raw 10px border-radius on focus outline wrapper |
| 3. Typography | **3** — Styles not from `affirm.typography/component/` set (may be a naming-format difference; verify in Figma) |
| 4. Component property naming | **2** — "Focus_visible" should be "Focus Visible"; boolean "External Link" should be "Has External Link" |
| **Total** | **6 issues** |

### Critical vs non-critical

- The **token coverage is complete** — all component tokens are applied, which is the highest-priority check.
- The **raw 10px border-radius** on the focus outline wrapper is a concrete issue that should be corrected (bind to a variable or create a new token).
- The **typography prefix** findings should be verified in Figma — if the MCP returns a simplified style path, the actual library styles may comply.
- The **naming issues** (Focus_visible underscore, missing "Has" prefix) are straightforward to fix and improve consistency across the design system.
