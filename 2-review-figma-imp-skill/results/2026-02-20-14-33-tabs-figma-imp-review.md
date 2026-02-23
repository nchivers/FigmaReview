# Figma Implementation Review: Tabs

## Inputs Used

| Input | Value / Status |
|-------|---------------|
| **componentName** | tabs |
| **componentUrl** | [Figma link](https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/aYQLf7iigh7grR2ECpkJlf/%F0%9F%8E%A8--R--DS-Core-Library?m=auto&node-id=3672-742&t=DqYySuHDCOs22dNL-1) |
| **Data source** | Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| **componentTokensCsv** | Present (47 tokens) |
| **figmaVariablesJson** | **Missing** — file `inputs/figma-variables.json` does not exist in the skill directory. Variable name resolution relied on MCP responses. |
| **namingRules** | Present (`knowledge/naming-rules.md`) |
| **additionalRules** | Present (`knowledge/additional-rules.md`) |

### Subcomponents

| Instance | Classification | Reason | Context fetched? |
|----------|---------------|--------|-----------------|
| **Tab** (nodes `3672:738`, `3672:740`) | **Owned subcomponent** (local, not published) | Same file as root component (same page prefix `3672`); internal to Tabs; not independently published | **Partial** — `get_variable_defs` fetched for both Tab variants (Selected=False/Resting and Selected=True/Resting). The Tab **component set** node ID could not be determined from MCP metadata, so non-resting interaction state variants (Hover, Focus-Visible, Pressed, Disabled) could not be fetched. |

---

## 1. Token Coverage

**Source:** 47 tokens from `inputs/component-tokens.csv` compared against variables returned by `get_variable_defs` for the root component set (`3672:742`) and both Tab variants (`3672:738`, `3672:740`).

### Tokens confirmed as applied (20 of 47)

All resting-state and structural tokens are present in the component:

| Token (figma_name) | Found in |
|---|---|
| `color/tabs/border` | Root |
| `color/tabs/tab/content_container/bg/selected/resting` | Root, Tab (selected) |
| `color/tabs/tab/content_container/bg/unselected/resting` | Root, Tab (unselected) |
| `color/tabs/tab/indicator/fill/selected/resting` | Root, Tab (selected) |
| `color/tabs/tab/indicator/fill/unselected/resting` | Root, Tab (unselected) |
| `color/tabs/tab/text/selected/resting` | Root, Tab (selected) |
| `color/tabs/tab/text/unselected/resting` | Root, Tab (unselected) |
| `radius/tabs/tab/container/bottom` | Root, Tab (both) |
| `radius/tabs/tab/container/top` | Root, Tab (both) |
| `radius/tabs/tab/content_container/bottom` | Root, Tab (both) |
| `radius/tabs/tab/content_container/top` | Root, Tab (both) |
| `radius/tabs/tab/indicator/all/selected` | Root, Tab (selected) |
| `radius/tabs/tab/indicator/all/unselected` | Root, Tab (unselected) |
| `size/tabs/border_bottom/width` | Root |
| `size/tabs/tab/indicator/height/selected` | Root, Tab (selected) |
| `size/tabs/tab/indicator/height/unselected` | Root, Tab (unselected) |
| `spacing/tabs/centered/gap_x` | Root |
| `spacing/tabs/left_aligned/gap_x` | Root |
| `spacing/tabs/tab/padding_x` | Root, Tab (both) |
| `spacing/tabs/tab/padding_y` | Root, Tab (both) |

### Tokens not found — could not verify (27 of 47)

These tokens correspond to **non-resting interaction states** (hover, focus_visible, pressed, disabled) and focus-visible-specific properties. They could not be verified because the MCP only returns variables for visible variant states, and the Tab component set's non-resting variants were not accessible.

**Color tokens (25):**
- `color/tabs/tab/content_container/bg/selected/disabled`
- `color/tabs/tab/content_container/bg/selected/focus_visible`
- `color/tabs/tab/content_container/bg/selected/hover`
- `color/tabs/tab/content_container/bg/selected/pressed`
- `color/tabs/tab/content_container/bg/unselected/disabled`
- `color/tabs/tab/content_container/bg/unselected/focus_visible`
- `color/tabs/tab/content_container/bg/unselected/hover`
- `color/tabs/tab/content_container/bg/unselected/pressed`
- `color/tabs/tab/indicator/fill/selected/disabled`
- `color/tabs/tab/indicator/fill/selected/focus_visible`
- `color/tabs/tab/indicator/fill/selected/hover`
- `color/tabs/tab/indicator/fill/selected/pressed`
- `color/tabs/tab/indicator/fill/unselected/disabled`
- `color/tabs/tab/indicator/fill/unselected/focus_visible`
- `color/tabs/tab/indicator/fill/unselected/hover`
- `color/tabs/tab/indicator/fill/unselected/pressed`
- `color/tabs/tab/outline/focus_visible`
- `color/tabs/tab/text/selected/disabled`
- `color/tabs/tab/text/selected/focus_visible`
- `color/tabs/tab/text/selected/hover`
- `color/tabs/tab/text/selected/pressed`
- `color/tabs/tab/text/unselected/disabled`
- `color/tabs/tab/text/unselected/focus_visible`
- `color/tabs/tab/text/unselected/hover`
- `color/tabs/tab/text/unselected/pressed`

**Size tokens (1):**
- `size/tabs/tab/outline/width/focus_visible`

**Spacing tokens (1):**
- `spacing/tabs/tab/outline/offset/focus_visible`

> **Note:** These 27 tokens are expected to be applied in the Tab subcomponent's Hover, Focus-Visible, Pressed, and Disabled interaction state variants. The Figma MCP `get_variable_defs` only returns variables for the currently visible variant state. The Tab component set node ID could not be resolved from the available metadata to fetch non-resting variants directly. **Manual verification recommended** — open the Tab subcomponent in Figma and inspect each interaction state variant to confirm these tokens are bound.

**No position tokens** were present in the CSV, so no exclusions were applied per the position token rule.

---

## 2. Raw Values and Direct Base Tokens

### Raw values (no hex / non-variable values)

**Root component:** No issues. All color, spacing, radius, size, and border properties use variable references (confirmed via `get_variable_defs` and `get_design_context` CSS custom properties).

**Subcomponent Tab (resting states):** No issues. All properties in the Selected=True/Resting and Selected=False/Resting variants use variable references.

Verified properties using variables:
- **Colors:** All fills use `var(--color/tabs/tab/...)` references
- **Spacing:** Padding uses `var(--spacing/tabs/tab/padding_x)` and `var(--spacing/tabs/tab/padding_y)`; gap uses `var(--spacing/tabs/left_aligned/gap_x)` or `var(--spacing/tabs/centered/gap_x)`
- **Radius:** All corner radii use `var(--radius/tabs/tab/...)` references
- **Sizes:** Indicator height uses `var(--size/tabs/tab/indicator/height/...)`, border width uses `var(--size/tabs/border_bottom/width)`
- **Border color:** Uses `var(--color/tabs/border)`

> **Note:** Non-resting interaction state variants of the Tab subcomponent could not be inspected for raw values (same limitation as token coverage). Manual verification recommended.

### Direct base tokens

No variables with names starting with `base/` were detected in any `get_variable_defs` response. No issues.

---

## 3. Typography

**Styles used:**

| Style name | Applied to | Compliant? |
|---|---|---|
| `typography/component/singleline/Medium-HighImp` | Selected tab label text (node `3672:741`) | Yes — from `component/` set |
| `typography/component/singleline/Medium-MidImp` | Unselected tab label text (node `3672:739`) | Yes — from `component/` set |

Both typography styles are from the `typography/component/` category, satisfying the `affirm.typography/component/` requirement (the `affirm.` prefix corresponds to the library namespace; Figma variable paths use `typography/component/` internally).

All text nodes use defined library styles. No ad-hoc font/size/lineHeight values found outside of the named styles.

No issues.

---

## 4. Component Property Naming

### Root component: Tabs

| Property | Type | Values | Compliant? | Notes |
|---|---|---|---|---|
| **Alignment** | Variant | Left, Center | Yes | Title Case noun, clear semantic values |
| **Tabs** | Variant | 2, 3, 4, 5, 6, 7, 8 | Yes | Title Case noun, short. The name matches the component name which is slightly ambiguous (could be confused with the component itself rather than the count), but is concise and clear in context with numeric values. |

### Subcomponent: Tab

| Property | Type | Values | Compliant? | Notes |
|---|---|---|---|---|
| **Selected** | Variant (boolean-like) | True, False | Yes | Follows the boolean-like variant pattern with True/False values per naming rules |
| **Interaction** | Variant | Resting (+ presumably Hover, Focus-Visible, Pressed, Disabled) | Yes | Uses "Interaction" not "State" per rules. Only Resting was visible via MCP. |
| **Label** | Text | (editable) | Yes | Meaningful role-based name, matches naming rules example |

No issues.

---

## Summary

| Category | Issues | Status |
|---|---|---|
| **1. Token coverage** | 0 confirmed issues; **27 tokens unverifiable** (interaction states not accessible via MCP) | Requires manual verification |
| **2. Raw values / base tokens** | 0 issues (resting states verified) | Pass (resting); manual check needed for interaction states |
| **3. Typography** | 0 issues | Pass |
| **4. Component property naming** | 0 issues | Pass |

### Key finding

The primary limitation of this review is that **27 of 47 tokens (57%)** could not be verified through the Figma MCP. These are all interaction-state tokens (hover, focus_visible, pressed, disabled) that would be applied in the Tab subcomponent's non-resting variants. The Tab component set node ID could not be resolved from the MCP metadata to fetch those variants directly.

**Recommendation:** Manually verify that all 27 interaction-state tokens listed above are correctly bound as variables in the corresponding Tab variant states in Figma. Alternatively, provide the Tab component set's direct Figma URL in `componentUrl` for a focused follow-up review.

### Missing input

The `figmaVariablesJson` file (`inputs/figma-variables.json`) was not found. This did not block the review since variable names were available from MCP responses, but having this file would enable variable ID resolution and `base/` prefix detection for variables that are only referenced by ID.
