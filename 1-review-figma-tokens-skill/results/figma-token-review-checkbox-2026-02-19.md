# Figma Token Review: Checkbox

**Date:** 2026-02-19
**Component:** checkbox
**CSV tokens:** 102
**Figma checkbox variables:** 102

---

## Task 1: CSV vs Figma

### Missing in Figma (exact name match)

2 tokens from the CSV do not have an exact name match in Figma. Both appear to be **naming discrepancies** rather than truly absent variables (see Naming Discrepancies below).

| CSV Token | Expected Figma Name |
|---|---|
| `affirm.color.checkbox.container.outline.focus_visible` | `color/checkbox/container/outline/focus_visible` |
| `affirm.size.checkbox.outline.width.focus_visible` | `size/checkbox/outline/width/focus_visible` |

### Extra in Figma

2 Figma variables have no corresponding CSV token. These likely correspond to the 2 "missing" tokens above.

| Figma Variable Name | Probable CSV Counterpart | Discrepancy |
|---|---|---|
| `color/checkbox/outline/focus_visible` | `affirm.color.checkbox.container.outline.focus_visible` | CSV has extra `container` path segment |
| `size/checkbox/outline/width/focus_outline` | `affirm.size.checkbox.outline.width.focus_visible` | Figma uses `focus_outline` instead of `focus_visible` |

### Naming Discrepancies

2 naming discrepancies detected between the CSV and Figma:

1. **`affirm.color.checkbox.container.outline.focus_visible`**
   - Expected Figma name: `color/checkbox/container/outline/focus_visible`
   - Actual Figma name: `color/checkbox/outline/focus_visible`
   - Issue: The CSV includes a `container` path segment that is absent in Figma.

2. **`affirm.size.checkbox.outline.width.focus_visible`**
   - Expected Figma name: `size/checkbox/outline/width/focus_visible`
   - Actual Figma name: `size/checkbox/outline/width/focus_outline`
   - Issue: The last segment differs — CSV uses `focus_visible`, Figma uses `focus_outline`.

### Assignment Discrepancies

1 token with discrepancies across 2 modes:

- **`affirm.color.checkbox.indicator.border.unselected.disabled`** (`color/checkbox/indicator/border/unselected/disabled`)
  - **Light Mode:** CSV expects alias `gray.300`, Figma aliases to `color/gray/300` (a semantic-level variable rather than the base primitive `base/g-color/gray/300`).
  - **Dark Mode:** CSV expects alias `gray.700`, Figma aliases to `color/gray/700` (same pattern — semantic variable instead of base primitive).
  - Note: All other color tokens in this component alias directly to `base/g-color/*` primitives. This token is the only one aliasing to a mid-level `color/*` semantic variable, which may indicate an unintended aliasing level.

---

## Task 2: Scoping Rule Violations

No issues. All 100 matched Figma checkbox variables pass the applicable scoping rules:

- **`color/checkbox/.../text/...`** tokens: scopes = `["TEXT_FILL"]`, hiddenFromPublishing = `true`
- **`color/checkbox/.../icon/...`** tokens: scopes = `["FRAME_FILL","SHAPE_FILL"]` (includes `SHAPE_FILL`), hiddenFromPublishing = `true`
- **`color/checkbox/.../bg/...`** tokens: scopes = `["FRAME_FILL","SHAPE_FILL"]`, hiddenFromPublishing = `true`
- **`color/checkbox/.../border/...`** tokens: scopes = `["STROKE_COLOR"]`, hiddenFromPublishing = `true`
- **`color/checkbox/.../outline/...`** tokens: scopes = `["STROKE_COLOR"]`, hiddenFromPublishing = `true`
- **`spacing/checkbox/...`** tokens: scopes = `["GAP"]`, hiddenFromPublishing = `true`
- **`radius/checkbox/...`** tokens: scopes = `["CORNER_RADIUS"]`
- **`size/checkbox/.../border/...`** tokens: scopes = `["STROKE_FLOAT"]`, hiddenFromPublishing = `true`
- **`size/checkbox/.../outline/...`** tokens: scopes = `["STROKE_FLOAT"]`, hiddenFromPublishing = `true`
- **`size/checkbox/...`** (dimensions): scopes = `["WIDTH_HEIGHT"]`, hiddenFromPublishing = `true`

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/figma-token-mapping-checkbox-2026-02-19.csv`.
