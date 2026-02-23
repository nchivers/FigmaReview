# Figma Implementation Review: Tabs

## Inputs Used

| Input | Value |
|-------|-------|
| **Component name** | tabs |
| **Component URL** | `https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/aYQLf7iigh7grR2ECpkJlf/...?node-id=3672-742` |
| **Data source** | Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| **Component tokens CSV** | Present (`inputs/component-tokens.csv`, 47 tokens) |
| **Figma variables JSON** | Present (`inputs/figma-variables.json`) — not required for this review; MCP provided variable resolution |
| **Naming rules** | Present (`knowledge/naming-rules.md`) |
| **Additional rules** | Present (`knowledge/additional-rules.md`) — position token exclusion, subcomponent rules, typography selection rules applied |

### Owned Subcomponents

| Subcomponent | Node ID | Classification | Context Fetched |
|---|---|---|---|
| **.Tab** | `3672:733` | **Owned** (local, not published — name prefixed with `.`) | Yes — `get_variable_defs`, `get_design_context`, `get_metadata` all called on `3672:733` |

The **.Tab** component set contains 10 variants: Selected (True/False) x Interaction (Resting, Hover, Pressed, Focus Visible, Disabled). Its full variable context was merged into the review scope.

No remote or published subcomponent instances were identified.

---

## 1. Token Coverage

**All 47 CSV tokens are applied.** No missing tokens.

Every token from the CSV was matched to a variable in the combined root + .Tab subcomponent `get_variable_defs` responses. Matching was done by Figma variable name (the `figma_name` column in the CSV) against the variable keys returned by MCP.

- **Root component** variables cover: `color/tabs/border`, `size/tabs/border_bottom/width`, `spacing/tabs/left_aligned/gap_x`, `spacing/tabs/centered/gap_x`, plus shared Tab variables for the default (Resting) state.
- **Subcomponent .Tab** variables cover all interaction-state tokens (hover, pressed, focus_visible, disabled) for text color, indicator fill, and content_container background — across both selected and unselected states — as well as outline/focus tokens (`color/tabs/tab/outline/focus_visible`, `size/tabs/tab/outline/width/focus_visible`, `spacing/tabs/tab/outline/offset/focus_visible`).

**Position token exclusion:** No position tokens were present in the CSV, so the position-token exception from additional rules was not needed.

**Additional variables found in the component (not in CSV):**
- `size/tabs/tab/border_bottom/width/selected` (value: `2`)
- `size/tabs/tab/border_bottom/width/unselected` (value: `0`)

These two variables are applied in the component but are not listed in the component tokens CSV. Consider adding them to the token set if they are intended component tokens.

---

## 2. Raw Values and Direct Base Tokens

### Issues

1. **Subcomponent .Tab — focus_ring element: border-radius uses raw values instead of variables**
   - **Nodes:** `19719:6478` (selected, focus visible), `19719:6471` (unselected, focus visible)
   - **Property:** `border-radius`
   - **Raw values:** `rounded-tl: 12px`, `rounded-tr: 12px`, `rounded-bl: 4px`, `rounded-br: 4px`
   - **Expected:** These should reference `radius/tabs/tab/container/top` (12px) and `radius/tabs/tab/container/bottom` (4px) variables, which are already bound on the parent container element. The focus ring's border-radius must match the container and should use the same variable bindings.

2. **Subcomponent .Tab — content_container: gap uses raw value**
   - **Nodes:** All content_container instances (e.g. `19667:5941`, `19667:6057`, and equivalents across interaction states)
   - **Property:** `itemSpacing` (auto-layout gap)
   - **Raw value:** `10px`
   - **Note:** This gap has no visual effect in the current layout because the only sibling of the text node (the indicator) is absolutely positioned. However, it is still a raw numeric value for a spacing property without a variable binding.

### No Direct Base Tokens

No variables with names starting with `base/` were found in the component. All applied variables use component-level token paths (`color/tabs/...`, `spacing/tabs/...`, `radius/tabs/...`, `size/tabs/...`).

---

## 3. Typography

**No issues.**

Both typography styles used in the component are from the `affirm.typography/component/` set (the `affirm.` prefix is consistently omitted by the Figma MCP for all variable names):

| Style | Used On | Weight | Size | Line Height |
|-------|---------|--------|------|-------------|
| `typography/component/singleline/Medium-HighImp` | Selected tab label | 600 (Semibold) | 16px | 20px |
| `typography/component/singleline/Medium-MidImp` | Unselected tab label | 500 (Medium) | 16px | 20px |

Both are named library styles (not ad-hoc font/size/lineHeight definitions). The underlying typography variables (`component/fontFamily`, `component/size/Medium`, `component/lineHeight/Medium`, `component/letterSpacing/Medium`, `component/weight/highImp`, `component/weight/midImp`) are all variable references.

---

## 4. Component Property Naming

**No issues.**

### Root component: Tabs

| Property | Type | Values | Compliance |
|----------|------|--------|------------|
| **Alignment** | Variant | Left, Center | Title Case, noun, semantic, clear values |
| **Tabs** | Variant | 2, 3, 4, 5, 6, 7, 8 | Title Case, noun, clear numeric values |

### Subcomponent: .Tab

| Property | Type | Values | Compliance |
|----------|------|--------|------------|
| **Selected** | Variant (boolean-like) | True, False | Title Case, True/False values per boolean-like variant rule |
| **Interaction** | Variant | Resting, Hover, Pressed, Focus Visible, Disabled | Title Case, uses "Interaction" (not "State"), "Disabled" is a value of Interaction — all per rules |
| **Label** | Text | (editable) | Title Case, role-based name, not generic |

All property names and values follow the naming rules. No emoji, no slashes/pipes, no implementation language, no vague terms.

---

## Summary

| Category | Issues |
|----------|--------|
| **1. Token coverage** | 0 |
| **2. Raw values / base tokens** | 2 |
| **3. Typography** | 0 |
| **4. Component property naming** | 0 |
| **Total** | **2 issues** |

### Issue Details

| # | Severity | Component | Description |
|---|----------|-----------|-------------|
| 1 | Issue | Subcomponent .Tab | Focus ring border-radius uses raw values (4px, 12px) instead of `radius/tabs/tab/container/bottom` and `radius/tabs/tab/container/top` variables |
| 2 | Issue (low impact) | Subcomponent .Tab | Content container auto-layout gap is a raw 10px value without a variable binding (no visual effect currently) |
