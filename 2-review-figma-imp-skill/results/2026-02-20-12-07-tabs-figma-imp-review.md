# Figma Implementation Review — Tabs

## Inputs Used

| Input | Value |
|-------|-------|
| **componentName** | tabs |
| **componentUrl** | https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/aYQLf7iigh7grR2ECpkJlf/%F0%9F%8E%A8--R--DS-Core-Library?m=auto&node-id=3672-742 |
| **Data source** | Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| **componentTokensCsv** | Present (47 tokens) |
| **figmaVariablesJson** | Not present (file does not exist) |
| **namingRules** | Present (`knowledge/naming-rules.md`) |
| **additionalRules** | Present (`knowledge/additional-rules.md`) |

### Component Structure

The component set **🎨 [R] Tabs** (node `3672:742`) contains 14 variants across two properties:

- **Alignment**: Left, Center
- **Tabs**: 2, 3, 4, 5, 6, 7, 8

Each variant contains **Tab** instances — a local subcomponent with properties: **Interaction** (Resting), **Selected** (boolean), and **Label** (text). The MCP data captured only the **Resting** interaction state of Tab, because the Tabs component set uses Tab instances exclusively in the Resting state; other interaction states (Hover, Pressed, Focus-Visible, Disabled) exist as separate variants on the Tab subcomponent itself.

### Subcomponent Classification

| Instance | Classification | Rationale |
|----------|---------------|-----------|
| **Tab** | Owned subcomponent (local, assumed not published) | Defined within the same component set; appears as an internal building block of Tabs. Full review criteria applied. |

---

## 1. Token Coverage

**Summary:** 20 of 47 CSV tokens confirmed as variables used in the component. 27 tokens not found — all are interaction-state tokens (hover, pressed, focus_visible, disabled) or outline/focus tokens that belong to non-resting Tab variants not captured by the MCP call on the parent component set.

### Tokens Confirmed Present (20)

| # | Token (figma_name) | Status |
|---|-------------------|--------|
| 1 | `color/tabs/border` | ✅ Used |
| 2 | `color/tabs/tab/content_container/bg/selected/resting` | ✅ Used |
| 3 | `color/tabs/tab/content_container/bg/unselected/resting` | ✅ Used |
| 4 | `color/tabs/tab/indicator/fill/selected/resting` | ✅ Used |
| 5 | `color/tabs/tab/indicator/fill/unselected/resting` | ✅ Used |
| 6 | `color/tabs/tab/text/selected/resting` | ✅ Used |
| 7 | `color/tabs/tab/text/unselected/resting` | ✅ Used |
| 8 | `radius/tabs/tab/container/bottom` | ✅ Used |
| 9 | `radius/tabs/tab/container/top` | ✅ Used |
| 10 | `radius/tabs/tab/content_container/bottom` | ✅ Used |
| 11 | `radius/tabs/tab/content_container/top` | ✅ Used |
| 12 | `radius/tabs/tab/indicator/all/selected` | ✅ Used |
| 13 | `radius/tabs/tab/indicator/all/unselected` | ✅ Used |
| 14 | `size/tabs/border_bottom/width` | ✅ Used |
| 15 | `size/tabs/tab/indicator/height/selected` | ✅ Used |
| 16 | `size/tabs/tab/indicator/height/unselected` | ✅ Used |
| 17 | `spacing/tabs/centered/gap_x` | ✅ Used |
| 18 | `spacing/tabs/left_aligned/gap_x` | ✅ Used |
| 19 | `spacing/tabs/tab/padding_x` | ✅ Used |
| 20 | `spacing/tabs/tab/padding_y` | ✅ Used |

### Tokens Not Found (27) — Interaction-State Tokens

All 27 missing tokens belong to non-resting interaction states of the Tab subcomponent. The Tabs component set only instantiates Tab in the **Resting** state; hover, pressed, focus_visible, and disabled states are separate variants of the Tab component that were not captured by the MCP call on the parent component set.

**Color — content_container/bg (8):**

| Token | Interaction State |
|-------|------------------|
| `color/tabs/tab/content_container/bg/selected/disabled` | Disabled |
| `color/tabs/tab/content_container/bg/selected/focus_visible` | Focus-Visible |
| `color/tabs/tab/content_container/bg/selected/hover` | Hover |
| `color/tabs/tab/content_container/bg/selected/pressed` | Pressed |
| `color/tabs/tab/content_container/bg/unselected/disabled` | Disabled |
| `color/tabs/tab/content_container/bg/unselected/focus_visible` | Focus-Visible |
| `color/tabs/tab/content_container/bg/unselected/hover` | Hover |
| `color/tabs/tab/content_container/bg/unselected/pressed` | Pressed |

**Color — indicator/fill (8):**

| Token | Interaction State |
|-------|------------------|
| `color/tabs/tab/indicator/fill/selected/disabled` | Disabled |
| `color/tabs/tab/indicator/fill/selected/focus_visible` | Focus-Visible |
| `color/tabs/tab/indicator/fill/selected/hover` | Hover |
| `color/tabs/tab/indicator/fill/selected/pressed` | Pressed |
| `color/tabs/tab/indicator/fill/unselected/disabled` | Disabled |
| `color/tabs/tab/indicator/fill/unselected/focus_visible` | Focus-Visible |
| `color/tabs/tab/indicator/fill/unselected/hover` | Hover |
| `color/tabs/tab/indicator/fill/unselected/pressed` | Pressed |

**Color — text (8):**

| Token | Interaction State |
|-------|------------------|
| `color/tabs/tab/text/selected/disabled` | Disabled |
| `color/tabs/tab/text/selected/focus_visible` | Focus-Visible |
| `color/tabs/tab/text/selected/hover` | Hover |
| `color/tabs/tab/text/selected/pressed` | Pressed |
| `color/tabs/tab/text/unselected/disabled` | Disabled |
| `color/tabs/tab/text/unselected/focus_visible` | Focus-Visible |
| `color/tabs/tab/text/unselected/hover` | Hover |
| `color/tabs/tab/text/unselected/pressed` | Pressed |

**Color — outline (1):**

| Token | Interaction State |
|-------|------------------|
| `color/tabs/tab/outline/focus_visible` | Focus-Visible |

**Size — outline (1):**

| Token | Interaction State |
|-------|------------------|
| `size/tabs/tab/outline/width/focus_visible` | Focus-Visible |

**Spacing — outline (1):**

| Token | Interaction State |
|-------|------------------|
| `spacing/tabs/tab/outline/offset/focus_visible` | Focus-Visible |

> **Note:** These 27 tokens are **not confirmed as issues**. They are expected to be applied on the Tab subcomponent's non-resting interaction variants. To fully verify, the Tab component set should be reviewed directly using its own node ID. No position tokens were present in the CSV, so the position-token exception (per additional rules) did not apply.

### Additional Variables Found (Not in CSV)

The component uses these variables that are **not listed in the CSV**:

| Variable | Resolved Value | Notes |
|----------|---------------|-------|
| `size/tabs/tab/border_bottom/width/selected` | 2 | Component token; may be missing from CSV |
| `size/tabs/tab/border_bottom/width/unselected` | 0 | Component token; may be missing from CSV |

Typography variables (`component/fontFamily`, `component/size/Medium`, `component/weight/highImp`, `component/weight/midImp`, `component/lineHeight/Medium • tight`, `component/letterSpacing/Medium`) are shared typography primitives used by the typography styles and are not expected in the component-specific CSV.

---

## 2. Raw Values and Direct Base Tokens

### Raw Values

| Layer / Context | Property | Raw Value | Severity | Notes |
|----------------|----------|-----------|----------|-------|
| `content_container` (Tab subcomponent) | gap (auto-layout item spacing) | `10px` | **Issue** | No variable bound for the gap between children. In practice the indicator is absolutely positioned so this gap has no visual effect on the current layout, but it should use a variable for consistency. |

All other spacing, color, border-radius, and stroke properties use variable references:

- **Spacing:** `padding_x`, `padding_y`, `gap_x` (left-aligned and centered), all use variables.
- **Color:** Border, text, indicator fills, content_container backgrounds — all use variables.
- **Border radius:** Container top/bottom, content_container top/bottom, indicator — all use variables.
- **Size/stroke:** Border bottom width, indicator height — all use variables.

### Direct Base Tokens

No variables with names starting with `base/` were found in the component. No issues.

---

## 3. Typography

### Styles Used

| Style Name | Applied To | Status |
|------------|-----------|--------|
| `typography/component/singleline/Medium-HighImp` | Selected tab label text | ✅ Uses library style; starts with `typography/component/` (maps to `affirm.typography/component/`) |
| `typography/component/singleline/Medium-MidImp` | Unselected tab label text | ✅ Uses library style; starts with `typography/component/` (maps to `affirm.typography/component/`) |

Both typography styles are from the `affirm.typography/component/` set as required by the additional rules. No issues.

---

## 4. Component Property Naming

### RTabs (Main Component Set)

| Property | Type | Values | Rule Check | Status |
|----------|------|--------|------------|--------|
| **Alignment** | Variant | Left, Center | Title Case ✅, noun ✅, semantic values ✅ | ✅ Pass |
| **Tabs** | Variant | 2, 3, 4, 5, 6, 7, 8 | Title Case ✅, noun ✅, clear values ✅ | ✅ Pass |

### Tab (Subcomponent)

| Property | Type | Values | Rule Check | Status |
|----------|------|--------|------------|--------|
| **Interaction** | Variant | Resting (+ likely Hover, Pressed, Focus-Visible, Disabled) | Title Case ✅, uses "Interaction" not "State" ✅, semantic values ✅ | ✅ Pass |
| **Selected** | Boolean / Boolean-like variant | true / false | **Does not start with "Has"** per boolean naming rules. If implemented as a boolean property, should be "Has Selection" (Has + Noun). If implemented as a boolean-like variant, should use a noun: "Selection" not "Selected" (adjective). | **Issue** |
| **Label** | Text | "Label" | Title Case ✅, uses role of text ✅, not generic ✅ | ✅ Pass |

---

## Summary

| Category | Issues | Details |
|----------|--------|---------|
| **1. Token coverage** | 0 confirmed issues; 27 tokens unverifiable | All 20 resting-state tokens confirmed. 27 interaction-state tokens could not be verified from the parent component set — they should be checked on the Tab subcomponent directly. 2 additional variables (`size/tabs/tab/border_bottom/width/selected` and `…/unselected`) found in the component but not in the CSV. |
| **2. Raw values / base tokens** | 1 issue | `content_container` has a raw `10px` gap (no variable bound). No base tokens used. |
| **3. Typography** | 0 issues | Both styles are from `affirm.typography/component/` set. |
| **4. Component property naming** | 1 issue | "Selected" property on Tab does not follow boolean naming convention (should start with "Has" or use noun form "Selection"). |

**Total issues found: 2**

### Recommendations

1. **Verify interaction-state tokens:** Review the Tab subcomponent directly (using its own component set node ID) to confirm the 27 interaction-state and outline/focus tokens are applied on the Hover, Pressed, Focus-Visible, and Disabled variants.
2. **Bind a variable to the content_container gap:** Even though the 10px gap currently has no visual effect (the indicator is absolutely positioned), bind a spacing variable for consistency.
3. **Rename "Selected" property:** Rename to "Has Selection" (if boolean) or "Selection" (if boolean-like variant with True/False values) to align with naming conventions.
4. **Add missing CSV tokens:** Consider adding `size/tabs/tab/border_bottom/width/selected` and `size/tabs/tab/border_bottom/width/unselected` to the component tokens CSV if they are intended component tokens.
