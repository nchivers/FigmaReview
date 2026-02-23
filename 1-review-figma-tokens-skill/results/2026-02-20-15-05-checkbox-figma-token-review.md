# Figma Token Review: Checkbox

**Date:** 2026-02-20
**Component:** checkbox
**CSV tokens:** 102
**Figma variables:** 99

---

## Task 1: CSV vs Figma Comparison

> **Naming convention note:** CSV tokens use dot-separated paths with an `affirm.` prefix (e.g. `affirm.color.checkbox.indicator.bg.selected.resting`), while Figma variables use slash-separated paths without the prefix (e.g. `color/checkbox/indicator/bg/selected/resting`). Comparison was performed by stripping the `affirm.` prefix and treating dots and slashes as equivalent path separators.

### Missing in Figma

3 tokens from the CSV have no corresponding Figma variable:

| CSV Token | Expected Figma Name |
|-----------|-------------------|
| `affirm.size.checkbox.outline.width.hover` | `size/checkbox/outline/width/hover` |
| `affirm.size.checkbox.outline.width.pressed` | `size/checkbox/outline/width/pressed` |
| `affirm.size.checkbox.outline.width.resting` | `size/checkbox/outline/width/resting` |

All three are outline width tokens for non-focus states. Note that the `focus_visible` variant **does** exist in Figma (`size/checkbox/outline/width/focus_visible`), so only the `hover`, `pressed`, and `resting` states are missing.

### Extra in Figma

None. Every Figma checkbox variable has a corresponding entry in the CSV.

### Naming Discrepancies

None. After normalizing the path separator convention (dots vs slashes) and the `affirm.` prefix, all matched token names are identical with no case, spacing, or segment differences.

### Assignment Discrepancies

None. All matched tokens were compared by mode:

- **Color tokens** (72): Light Mode and Dark Mode alias targets in Figma match the CSV values (e.g. CSV `indigo.970` corresponds to Figma alias `base/g-color/indigo/970`).
- **Size tokens** (19 matched): All Modes alias targets match (e.g. CSV `size.250` corresponds to Figma alias `base/size/250`).
- **Radius tokens** (2): All Modes alias targets match.
- **Spacing tokens** (3): All Modes alias targets match.

---

## Task 2: Scoping Rule Violations

No violations found. All 99 matched Figma checkbox variables comply with the applicable scoping rules.

### Rules evaluated:

| Rule | Tokens Checked | Expected Scopes | Expected hiddenFromPublishing | Result |
|------|---------------|-----------------|-------------------------------|--------|
| Component color + `/text` | 17 label/text tokens | `["TEXT_FILL"]` | true | Pass |
| Component color + `/icon` | 18 indicator/icon tokens | must include `["SHAPE_FILL"]` | true | Pass (actual: `["FRAME_FILL","SHAPE_FILL"]`) |
| Component color + `/bg` | 18 indicator/bg tokens | `["FRAME_FILL","SHAPE_FILL"]` | true | Pass |
| Component color + `/border` | 18 indicator/border tokens | `["STROKE_COLOR"]` | true | Pass |
| Component color + `/outline` | 1 container/outline token | `["STROKE_COLOR"]` | true | Pass |
| Spacing | 3 spacing tokens | `["GAP"]` | true | Pass |
| Component size (dimension) | 3 tokens (indicator/all, icon/all, container/min_height) | `["WIDTH_HEIGHT"]` | true | Pass |
| Size + `/border` | 18 indicator/border/width tokens | `["STROKE_FLOAT"]` | true | Pass |
| Size + `/outline/` | 1 outline/width token | `["STROKE_FLOAT"]` | true | Pass |
| Radius | 2 radius tokens | `["CORNER_RADIUS"]` | true | Pass |

---

## Token Mapping

The full CSV-to-Figma token mapping is in `results/2026-02-20-15-05-checkbox-figma-token-mapping.csv`.
