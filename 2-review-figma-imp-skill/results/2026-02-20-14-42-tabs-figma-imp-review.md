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
| **Tab** (component set `3672:733`, name `.Tab`) | **Owned subcomponent** (local, not published) | Same file as root; dot-prefixed name (`.Tab`) indicates local/internal component; not independently published | **Yes** — full context fetched: `get_variable_defs`, `get_design_context`, and `get_metadata` for the Tab component set (`3672:733`), covering all 10 variants (Selected True/False × Interaction Resting/Hover/Pressed/Focus Visible/Disabled). |

No other subcomponent instances were identified. All Tab instances within the Tabs variants reference the same `.Tab` component set.

---

## 1. Token Coverage

**Source:** 47 tokens from `inputs/component-tokens.csv` compared against variables returned by `get_variable_defs` for the root component set (`3672:742`) and the Tab component set (`3672:733`).

### Result: 47 of 47 tokens found (100% coverage)

All tokens from the CSV are present as used variables across the root Tabs component and the owned Tab subcomponent.

| Token category | Count | All found? |
|---|---|---|
| Color — text (selected/unselected × 5 states) | 10 | Yes |
| Color — indicator fill (selected/unselected × 5 states) | 10 | Yes |
| Color — content_container bg (selected/unselected × 5 states) | 10 | Yes |
| Color — outline focus_visible | 1 | Yes |
| Color — border | 1 | Yes |
| Radius — container, content_container, indicator | 6 | Yes |
| Size — border_bottom width, indicator height, outline width | 4 | Yes |
| Spacing — gap_x, padding, outline offset | 5 | Yes |
| **Total** | **47** | **Yes** |

No position tokens were present in the CSV, so no exclusions were needed per the position token rule.

---

## 2. Raw Values and Direct Base Tokens

### Raw values

**Root component (Tabs):** No issues. All color, spacing, radius, size, and border properties use variable references (confirmed via `get_variable_defs` and `get_design_context` CSS custom properties).

**Subcomponent Tab:** One issue identified on the **focus-visible-outline** layer.

- **Issue:** Subcomponent Tab — The `focus-visible-outline` layer (nodes `19719:6478` / `19719:6471`) uses **raw border-radius values** instead of variable references:
  - `rounded-tl-[12px]` — raw `12px` (expected: `var(--radius/tabs/tab/container/top)`)
  - `rounded-tr-[12px]` — raw `12px` (expected: `var(--radius/tabs/tab/container/top)`)
  - `rounded-bl-[4px]` — raw `4px` (expected: `var(--radius/tabs/tab/container/bottom)`)
  - `rounded-br-[4px]` — raw `4px` (expected: `var(--radius/tabs/tab/container/bottom)`)

  The parent Tab container correctly uses `var(--radius/tabs/tab/container/top)` and `var(--radius/tabs/tab/container/bottom)` for the same visual radii. The focus-visible-outline overlay should use the same variable bindings to stay in sync.

All other Tab properties across all 10 variants use variable references correctly:
- Content container background colors: `var(--color/tabs/tab/content_container/bg/...)` per state
- Text colors: `var(--color/tabs/tab/text/...)` per state
- Indicator fills: `var(--color/tabs/tab/indicator/fill/...)` per state
- Padding: `var(--spacing/tabs/tab/padding_x)`, `var(--spacing/tabs/tab/padding_y)`
- Indicator height: `var(--size/tabs/tab/indicator/height/...)`
- Indicator radius: `var(--radius/tabs/tab/indicator/all/...)`
- Content container radius: `var(--radius/tabs/tab/content_container/...)`
- Outline width: `var(--size/tabs/tab/outline/width/focus_visible)`
- Outline color: `var(--color/tabs/tab/outline/focus_visible)`
- Outline offset: `var(--spacing/tabs/tab/outline/offset/focus_visible)` (bound in Figma; value is 0)

### Direct base tokens

No variables with names starting with `base/` were detected in any `get_variable_defs` response. No issues.

---

## 3. Typography

**Styles used:**

| Style name | Applied to | Compliant? |
|---|---|---|
| `typography/component/singleline/Medium-HighImp` | Selected tab label text (all interaction states) | Yes — from `component/` set |
| `typography/component/singleline/Medium-MidImp` | Unselected tab label text (all interaction states) | Yes — from `component/` set |

Both typography styles are from the `typography/component/` category, satisfying the `affirm.typography/component/` requirement (the `affirm.` prefix corresponds to the library namespace; Figma variable paths use `typography/component/` internally).

All text nodes across all 10 Tab variants use defined library styles. No ad-hoc font/size/lineHeight values were found outside of the named styles.

No issues.

---

## 4. Component Property Naming

### Root component: Tabs (component set `3672:742`)

| Property | Type | Values | Compliant? | Notes |
|---|---|---|---|---|
| **Alignment** | Variant | Left, Center | Yes | Title Case noun; clear, semantic values |
| **Tabs** | Variant | 2, 3, 4, 5, 6, 7, 8 | Yes | Title Case noun; short and specific; numeric values clearly represent tab count |

### Subcomponent: Tab (component set `3672:733`)

| Property | Type | Values | Compliant? | Notes |
|---|---|---|---|---|
| **Selected** | Variant (boolean-like) | True, False | Yes | Boolean-like variant with True/False values per naming rules |
| **Interaction** | Variant | Resting, Hover, Pressed, Focus Visible, Disabled | Yes | Uses "Interaction" not "State" per rules; Disabled is a value in Interaction (not a separate boolean); all values Title Case |
| **Label** | Text | (editable) | Yes | Meaningful, role-based name; matches naming rules example |

No issues.

---

## Summary

| Category | Issues | Status |
|---|---|---|
| **1. Token coverage** | 0 issues — all 47 tokens applied | Pass |
| **2. Raw values / base tokens** | **1 issue** — focus-visible-outline uses raw border-radius values (4 properties) | Issue |
| **3. Typography** | 0 issues | Pass |
| **4. Component property naming** | 0 issues | Pass |

**Total: 1 issue (4 raw border-radius values on the focus-visible-outline layer in the Tab subcomponent).**

### Missing input note

The `figmaVariablesJson` file (`inputs/figma-variables.json`) was not found in the skill directory. This did not block the review since all variable names were available from MCP `get_variable_defs` responses and no `base/`-prefixed variables were detected. For future reviews, having this file enables additional cross-referencing of variable IDs and alias chain resolution.
