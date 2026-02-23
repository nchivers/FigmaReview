# Figma Implementation Review — Tabs

**Date:** 2026-02-20 08:55
**Component:** Tabs
**Component URL:** https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/aYQLf7iigh7grR2ECpkJlf/%F0%9F%8E%A8--R--DS-Core-Library?m=auto&node-id=3672-742

## Inputs Used

| Input | Status |
|-------|--------|
| componentName | `tabs` |
| componentUrl | Provided (see above) |
| Component data source | **Figma MCP** (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| componentTokensCsv | Present (`inputs/component-tokens.csv` — 47 tokens) |
| figmaVariablesJson | Not present (file does not exist at inputs path) |
| namingRules | Present (`knowledge/naming-rules.md`) |
| additionalRules | Present (`knowledge/additional-rules.md`) |

---

## 1. Token Coverage

**20 of 47 tokens found** in the Figma MCP data. **27 tokens not found.**

### Tokens found (20)

| Token (figma_name) | Resolved Value |
|---------------------|---------------|
| `color/tabs/border` | #d8d8df |
| `color/tabs/tab/content_container/bg/selected/resting` | #00000000 |
| `color/tabs/tab/content_container/bg/unselected/resting` | #00000000 |
| `color/tabs/tab/indicator/fill/selected/resting` | #000049 |
| `color/tabs/tab/indicator/fill/unselected/resting` | #00000000 |
| `color/tabs/tab/text/selected/resting` | #0c0c14 |
| `color/tabs/tab/text/unselected/resting` | #4b4b5c |
| `radius/tabs/tab/container/bottom` | 4 |
| `radius/tabs/tab/container/top` | 12 |
| `radius/tabs/tab/content_container/bottom` | 0 |
| `radius/tabs/tab/content_container/top` | 12 |
| `radius/tabs/tab/indicator/all/selected` | 2 |
| `radius/tabs/tab/indicator/all/unselected` | 1 |
| `size/tabs/border_bottom/width` | 2 |
| `size/tabs/tab/indicator/height/selected` | 2 |
| `size/tabs/tab/indicator/height/unselected` | 1 |
| `spacing/tabs/centered/gap_x` | 0 |
| `spacing/tabs/left_aligned/gap_x` | 48 |
| `spacing/tabs/tab/padding_x` | 8 |
| `spacing/tabs/tab/padding_y` | 14 |

### Tokens NOT found — issue (27)

All 27 missing tokens are for **non-resting interaction states** (hover, pressed, focus_visible, disabled). These are applied within the Tab subcomponent's interaction variants, which were not captured by the MCP query on the parent Tabs component set.

**Content container background (8):**
- `color/tabs/tab/content_container/bg/selected/disabled`
- `color/tabs/tab/content_container/bg/selected/focus_visible`
- `color/tabs/tab/content_container/bg/selected/hover`
- `color/tabs/tab/content_container/bg/selected/pressed`
- `color/tabs/tab/content_container/bg/unselected/disabled`
- `color/tabs/tab/content_container/bg/unselected/focus_visible`
- `color/tabs/tab/content_container/bg/unselected/hover`
- `color/tabs/tab/content_container/bg/unselected/pressed`

**Indicator fill (8):**
- `color/tabs/tab/indicator/fill/selected/disabled`
- `color/tabs/tab/indicator/fill/selected/focus_visible`
- `color/tabs/tab/indicator/fill/selected/hover`
- `color/tabs/tab/indicator/fill/selected/pressed`
- `color/tabs/tab/indicator/fill/unselected/disabled`
- `color/tabs/tab/indicator/fill/unselected/focus_visible`
- `color/tabs/tab/indicator/fill/unselected/hover`
- `color/tabs/tab/indicator/fill/unselected/pressed`

**Text color (8):**
- `color/tabs/tab/text/selected/disabled`
- `color/tabs/tab/text/selected/focus_visible`
- `color/tabs/tab/text/selected/hover`
- `color/tabs/tab/text/selected/pressed`
- `color/tabs/tab/text/unselected/disabled`
- `color/tabs/tab/text/unselected/focus_visible`
- `color/tabs/tab/text/unselected/hover`
- `color/tabs/tab/text/unselected/pressed`

**Outline / focus-visible (3):**
- `color/tabs/tab/outline/focus_visible`
- `size/tabs/tab/outline/width/focus_visible`
- `spacing/tabs/tab/outline/offset/focus_visible`

### Subcomponent scope note

Per **additional rules (Subcomponents):** The Tab instances inside the Tabs component set do not have names starting with '.' or '_', so they are **not** treated as true subcomponents. Their internal structure is evaluated for overrides only; missing tokens inside Tab are out of scope for this review.

The 27 missing tokens are all expected to live within the Tab subcomponent's non-resting interaction variants (Hover, Pressed, Focus-Visible, Disabled). **To confirm these tokens are applied, the Tab subcomponent should be reviewed independently** by querying its own component node directly.

No position tokens were present in the CSV, so no exclusions per the position token rule were needed.

---

## 2. Raw Values and Direct Base Tokens

### Raw values — issue (1)

| Layer | Property | Raw Value | Notes |
|-------|----------|-----------|-------|
| `content_container` (inside Tab) | gap (auto-layout) | `10px` | Spacing gap between text and indicator is a raw numeric value, not bound to a variable. *(Inside Tab subcomponent — noted for completeness but Tab internals are out of scope per subcomponent rules.)* |

### Base tokens

No variables with names starting with `base/` were detected. All variable names use component-level or semantic paths (e.g. `color/tabs/...`, `spacing/tabs/...`, `radius/tabs/...`).

### Raw hex / non-variable colors

None. All color properties visible in the MCP data are bound to variables.

### Additional variables in MCP not in CSV

The MCP returned two variables not listed in the CSV:
- `size/tabs/tab/border_bottom/width/selected` (value: 2)
- `size/tabs/tab/border_bottom/width/unselected` (value: 0)

These appear to be per-state border width variables used internally in the Tab subcomponent. Their absence from the CSV is informational only — the CSV may not include all internal subcomponent variables.

---

## 3. Typography

Two typography styles are used in the component:

| Style | Applied To | Properties |
|-------|-----------|------------|
| `typography/component/singleline/Medium-HighImp` | Selected tab text | Calibre Semibold, 16/20, 600 weight |
| `typography/component/singleline/Medium-MidImp` | Unselected tab text | Calibre Medium, 16/20, 500 weight |

Both styles are from the `affirm.typography/component/` set (the `typography/component/` prefix in Figma corresponds to the `affirm.typography/component/` namespace). Both are named library styles, not ad-hoc font configurations.

**No issues.**

---

## 4. Component Property Naming

### RTabs properties (in scope)

| Property | Type | Values | Rule Check | Status |
|----------|------|--------|------------|--------|
| Alignment | Variant | Left, Center | Title Case noun ✅; semantic values ✅ | No issues |
| Tabs | Variant | 2, 3, 4, 5, 6, 7, 8 | Title Case noun ✅; numeric values for tab count are acceptable | No issues |

### Tab properties (out of scope — noted for reference)

Per additional rules, Tab instances do not start with '.' or '_' and are therefore not true subcomponents. Tab's internal properties are out of scope for this review. Listed below for reference only:

| Property | Type | Values | Observation |
|----------|------|--------|-------------|
| Interaction | Variant | Resting (+ likely Hover, Pressed, Focus-Visible, Disabled) | ✅ Uses "Interaction" not "State" per rules |
| Selected | Boolean | true, false | ⚠️ Does not start with "Has" per boolean naming rules (should be "Has Selected" or restructured as a variant with True/False values) |
| Label | Text | (editable) | ✅ Role-based name per rules |

**No in-scope issues.**

---

## Summary

| Check | Issues |
|-------|--------|
| 1. Token coverage | 27 tokens not found in MCP data (all non-resting interaction state tokens inside Tab subcomponent — out of scope per subcomponent rules; recommend independent Tab review) |
| 2. Raw values / base tokens | 1 raw value (`content_container` gap: 10px — inside Tab subcomponent, out of scope per rules) |
| 3. Typography | 0 issues |
| 4. Component property naming | 0 in-scope issues (1 out-of-scope observation on Tab's "Selected" boolean naming) |

### Critical vs Non-Critical

- **No critical in-scope issues identified** for the RTabs component set itself.
- **Recommendation:** The Tab subcomponent should be reviewed independently to verify the 27 non-resting interaction state tokens are correctly applied, the `content_container` gap uses a variable, and the "Selected" boolean property follows naming conventions. If Tab is intended to be a private subcomponent of Tabs, consider renaming it with a '.' or '_' prefix (e.g. `.Tab`) so future reviews include it in scope automatically.
