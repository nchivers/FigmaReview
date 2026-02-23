# Figma Implementation Review: Tabs

## Inputs Used

- **Component name:** Tabs
- **Component URL:** https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/aYQLf7iigh7grR2ECpkJlf/%F0%9F%8E%A8--R--DS-Core-Library?m=auto&node-id=3672-742
- **Data source:** Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`)
- **Component tokens CSV:** Present (47 tokens)
- **Figma variables JSON:** Not found (file does not exist at `inputs/figma-variables.json`)
- **Naming rules:** Present (`knowledge/naming-rules.md`)
- **Additional rules:** Present (`knowledge/additional-rules.md`) — position token exception, owned subcomponent rules, typography selection rules applied throughout

### Subcomponent Classification

The **Tab** subcomponent (instances used inside each Tabs variant) was identified from the design context output. Tab is rendered as a locally-defined component within the same code context as the root Tabs component set, which indicates it is **local** to the file. Published status could not be definitively determined from the MCP data alone.

**Treatment:** Tab was classified as an **owned subcomponent** (local, assumed not published) per the additional rules. Variable definitions were fetched for both the root Tabs component set (node `3672:742`) and individual Tab variant nodes (`3672:738` for unselected/resting, `3672:740` for selected/resting).

**Limitation:** The Tab component set's full node ID could not be located to fetch all interaction state variants (Hover, Focus-Visible, Pressed, Disabled). Only the **Resting** interaction state was available from the MCP data. This means tokens for non-resting interaction states could not be verified as applied. The 27 unverified tokens are all for non-resting states and are listed below.

---

## 1. Token Coverage

**CSV tokens:** 47 total
**Tokens confirmed as applied (from MCP variable_defs):** 20
**Tokens not found in MCP data:** 27 (all non-resting interaction states — see limitation above)
**Position tokens excluded:** None identified in the CSV

### Tokens confirmed as applied (20)

| CSV Token | Figma Variable Name | Status |
|-----------|-------------------|--------|
| affirm.color.tabs.border | color/tabs/border | Applied |
| affirm.color.tabs.tab.content_container.bg.selected.resting | color/tabs/tab/content_container/bg/selected/resting | Applied |
| affirm.color.tabs.tab.content_container.bg.unselected.resting | color/tabs/tab/content_container/bg/unselected/resting | Applied |
| affirm.color.tabs.tab.indicator.fill.selected.resting | color/tabs/tab/indicator/fill/selected/resting | Applied |
| affirm.color.tabs.tab.indicator.fill.unselected.resting | color/tabs/tab/indicator/fill/unselected/resting | Applied |
| affirm.color.tabs.tab.text.selected.resting | color/tabs/tab/text/selected/resting | Applied |
| affirm.color.tabs.tab.text.unselected.resting | color/tabs/tab/text/unselected/resting | Applied |
| affirm.radius.tabs.tab.container.bottom | radius/tabs/tab/container/bottom | Applied |
| affirm.radius.tabs.tab.container.top | radius/tabs/tab/container/top | Applied |
| affirm.radius.tabs.tab.content_container.bottom | radius/tabs/tab/content_container/bottom | Applied |
| affirm.radius.tabs.tab.content_container.top | radius/tabs/tab/content_container/top | Applied |
| affirm.radius.tabs.tab.indicator.all.selected | radius/tabs/tab/indicator/all/selected | Applied |
| affirm.radius.tabs.tab.indicator.all.unselected | radius/tabs/tab/indicator/all/unselected | Applied |
| affirm.size.tabs.border_bottom.width | size/tabs/border_bottom/width | Applied |
| affirm.size.tabs.tab.indicator.height.selected | size/tabs/tab/indicator/height/selected | Applied |
| affirm.size.tabs.tab.indicator.height.unselected | size/tabs/tab/indicator/height/unselected | Applied |
| affirm.spacing.tabs.centered.gap_x | spacing/tabs/centered/gap_x | Applied |
| affirm.spacing.tabs.left_aligned.gap_x | spacing/tabs/left_aligned/gap_x | Applied |
| affirm.spacing.tabs.tab.padding_x | spacing/tabs/tab/padding_x | Applied |
| affirm.spacing.tabs.tab.padding_y | spacing/tabs/tab/padding_y | Applied |

### Tokens not verified — non-resting interaction states (27)

These tokens could not be confirmed because only the Resting state of the Tab subcomponent was accessible via MCP. They correspond to Hover, Focus-Visible, Pressed, and Disabled interaction states defined in the Tab component set.

| CSV Token | Figma Variable Name | State |
|-----------|-------------------|-------|
| affirm.color.tabs.tab.content_container.bg.selected.disabled | color/tabs/tab/content_container/bg/selected/disabled | Disabled |
| affirm.color.tabs.tab.content_container.bg.selected.focus_visible | color/tabs/tab/content_container/bg/selected/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.content_container.bg.selected.hover | color/tabs/tab/content_container/bg/selected/hover | Hover |
| affirm.color.tabs.tab.content_container.bg.selected.pressed | color/tabs/tab/content_container/bg/selected/pressed | Pressed |
| affirm.color.tabs.tab.content_container.bg.unselected.disabled | color/tabs/tab/content_container/bg/unselected/disabled | Disabled |
| affirm.color.tabs.tab.content_container.bg.unselected.focus_visible | color/tabs/tab/content_container/bg/unselected/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.content_container.bg.unselected.hover | color/tabs/tab/content_container/bg/unselected/hover | Hover |
| affirm.color.tabs.tab.content_container.bg.unselected.pressed | color/tabs/tab/content_container/bg/unselected/pressed | Pressed |
| affirm.color.tabs.tab.indicator.fill.selected.disabled | color/tabs/tab/indicator/fill/selected/disabled | Disabled |
| affirm.color.tabs.tab.indicator.fill.selected.focus_visible | color/tabs/tab/indicator/fill/selected/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.indicator.fill.selected.hover | color/tabs/tab/indicator/fill/selected/hover | Hover |
| affirm.color.tabs.tab.indicator.fill.selected.pressed | color/tabs/tab/indicator/fill/selected/pressed | Pressed |
| affirm.color.tabs.tab.indicator.fill.unselected.disabled | color/tabs/tab/indicator/fill/unselected/disabled | Disabled |
| affirm.color.tabs.tab.indicator.fill.unselected.focus_visible | color/tabs/tab/indicator/fill/unselected/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.indicator.fill.unselected.hover | color/tabs/tab/indicator/fill/unselected/hover | Hover |
| affirm.color.tabs.tab.indicator.fill.unselected.pressed | color/tabs/tab/indicator/fill/unselected/pressed | Pressed |
| affirm.color.tabs.tab.outline.focus_visible | color/tabs/tab/outline/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.text.selected.disabled | color/tabs/tab/text/selected/disabled | Disabled |
| affirm.color.tabs.tab.text.selected.focus_visible | color/tabs/tab/text/selected/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.text.selected.hover | color/tabs/tab/text/selected/hover | Hover |
| affirm.color.tabs.tab.text.selected.pressed | color/tabs/tab/text/selected/pressed | Pressed |
| affirm.color.tabs.tab.text.unselected.disabled | color/tabs/tab/text/unselected/disabled | Disabled |
| affirm.color.tabs.tab.text.unselected.focus_visible | color/tabs/tab/text/unselected/focus_visible | Focus-Visible |
| affirm.color.tabs.tab.text.unselected.hover | color/tabs/tab/text/unselected/hover | Hover |
| affirm.color.tabs.tab.text.unselected.pressed | color/tabs/tab/text/unselected/pressed | Pressed |
| affirm.size.tabs.tab.outline.width.focus_visible | size/tabs/tab/outline/width/focus_visible | Focus-Visible |
| affirm.spacing.tabs.tab.outline.offset.focus_visible | spacing/tabs/tab/outline/offset/focus_visible | Focus-Visible |

### Additional variables observed (not in CSV)

The following variables were found in the component but are not listed in the CSV. These are not issues — they are additional tokens used by the implementation:

- `size/tabs/tab/border_bottom/width/selected` (value: 2)
- `size/tabs/tab/border_bottom/width/unselected` (value: 0)

---

## 2. Raw Values and Direct Base Tokens

### Raw values (non-variable)

- **Issue:** Subcomponent Tab — `content_container` layer, **gap** property: raw value `10px`. This auto-layout gap is not bound to a variable. All spacing properties should use variable references.

### Direct base tokens (variable names starting with `base/`)

- None. All observed variable names use component-level token paths (e.g. `color/tabs/...`, `spacing/tabs/...`, `radius/tabs/...`, `size/tabs/...`). No `base/` prefixed variables were found.

**Note:** The `figmaVariablesJson` file was not available, so alias chain resolution (checking whether any applied variable aliases a base token) could not be performed. The check was limited to the variable names returned by `get_variable_defs`.

---

## 3. Typography

### Styles observed

| Style Name | Applied To | Status |
|-----------|-----------|--------|
| typography/component/singleline/Medium-HighImp | Selected tab text (weight: 600/Semibold) | Pass |
| typography/component/singleline/Medium-MidImp | Unselected tab text (weight: 500/Medium) | Pass |

Both typography styles are defined library styles (returned as named entries from `get_variable_defs`). Both start with `typography/component/` which corresponds to the required `affirm.typography/component/` set (the `affirm.` prefix is not included in Figma variable names). No ad-hoc font specifications were found.

No issues.

---

## 4. Component Property Naming

### Root component: Tabs (`3672:742`)

| Property | Type | Values | Rule Check | Status |
|----------|------|--------|-----------|--------|
| Alignment | Variant | Left, Center | Title Case, noun, clear semantic values | Pass |
| Tabs | Variant | 2, 3, 4, 5, 6, 7, 8 | Title Case, noun | **Issue** |

- **Issue:** Root component — Variant property **"Tabs"** uses the component's own name as a property name. Per naming rules, property names should be specific and avoid vague terms. A name like **"Count"** or **"Tab Count"** would more clearly describe what the property controls (the number of tabs displayed). "Tabs" as a property name within the Tabs component is ambiguous — it could be confused with the component name itself rather than the number of tabs.

### Subcomponent: Tab

| Property | Type | Values (observed) | Rule Check | Status |
|----------|------|-------------------|-----------|--------|
| Interaction | Variant | Resting (others expected: Hover, Focus-Visible, Pressed, Disabled) | Title Case, noun, uses "Interaction" not "State" | Pass |
| Selected | Boolean-like | true / false | Should start with "Has" if boolean property | **Issue** |
| Label | Text | "Label" (default) | Uses role of text, not position | Pass |

- **Issue:** Subcomponent Tab — Property **"Selected"** does not follow the boolean naming convention. Per naming rules, boolean properties must start with **"Has"** (format: Has + Noun). The property should be renamed to **"Has Selected"** or restructured as a variant property with explicit **"True"/"False"** values if using the boolean-like variant pattern.

### Property panel order

Property panel order could not be verified from MCP data alone. The naming rules specify that Core Variants (Size, Emphasis, Interaction) should come first, followed by Layout Variants, then boolean/swap/text properties ordered by layout position.

---

## Summary

| Category | Issues | Not Verified |
|----------|--------|-------------|
| 1. Token coverage | 0 confirmed issues | 27 tokens (non-resting states) |
| 2. Raw values / base tokens | 1 issue | — |
| 3. Typography | 0 issues | — |
| 4. Property naming | 2 issues | Panel order |
| **Total** | **3 issues** | **27 tokens + panel order** |

### Issues

1. **Raw value (spacing):** Tab subcomponent `content_container` has a `10px` gap not bound to a variable.
2. **Property naming:** Root component variant property "Tabs" should use a more descriptive name (e.g. "Count").
3. **Property naming:** Tab subcomponent property "Selected" does not follow the "Has" prefix convention for boolean properties.

### Unverified items

- **27 tokens** for non-resting interaction states (Hover, Focus-Visible, Pressed, Disabled) could not be verified. The Tab component set with all interaction variants was not accessible from the MCP scope of the root Tabs component set. A manual check of the Tab component set in Figma is recommended to confirm these tokens are applied to the corresponding interaction state variants.
- **Property panel order** in Figma could not be verified from MCP data.
- **Figma variables JSON** was not available, so alias chain resolution for base token detection could not be performed.
