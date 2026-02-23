# Figma Token Review — Tabs

**Component:** tabs
**Date:** 2026-02-20-14-26
**CSV tokens:** 47
**Figma variables matched:** 47

---

## Task 1: CSV vs Figma

### Missing in Figma

None. All 47 CSV tokens have a corresponding Figma variable.

### Extra in Figma

None. Every Figma variable containing `tabs` in its name maps to a CSV token.

### Naming Discrepancies

None. The CSV uses `affirm.{category}.tabs.{path}` (dot-separated) and Figma uses `{category}/tabs/{path}` (slash-separated). After removing the `affirm.` prefix and converting dots to slashes, all names match exactly (case-sensitive). Underscored segments (e.g. `content_container`, `border_bottom`, `focus_visible`, `left_aligned`, `gap_x`, `padding_x`, `padding_y`) are consistent between both sources.

### Assignment Discrepancies

None. All alias assignments in Figma match the expected values from the CSV:

- **Color tokens (Light/Dark modes):** Each CSV value (e.g. `gray.950`) matches the corresponding Figma alias (e.g. `base/g-color/gray/950`). All 32 color tokens verified across both modes.
- **Radius tokens (All Modes):** Each CSV value (e.g. `size.150`) matches the corresponding Figma alias (e.g. `base/size/150`). All 6 radius tokens verified.
- **Size tokens (All Modes):** Each CSV value matches the Figma alias. All 4 size tokens verified.
- **Spacing tokens (All Modes):** Each CSV value matches the Figma alias. All 5 spacing tokens verified.

---

## Task 2: Scoping Rule Violations

No violations found. All 47 tokens comply with the applicable scoping rules.

### Compliant tokens by rule

| Rule | Tokens | Count | Result |
|------|--------|-------|--------|
| Component color — `/text` → `["TEXT_FILL"]`, hidden=true | `color/tabs/tab/text/...` | 10 | All compliant |
| Component color — `/bg` → `["FRAME_FILL","SHAPE_FILL"]`, hidden=true | `color/tabs/tab/content_container/bg/...` | 10 | All compliant |
| Component color — `/fill` → `["FRAME_FILL","SHAPE_FILL"]`, hidden=true | `color/tabs/tab/indicator/fill/...` | 10 | All compliant |
| Component color — `/border` → `["STROKE_COLOR"]`, hidden=true | `color/tabs/border` | 1 | Compliant |
| Component color — `/outline` → `["STROKE_COLOR"]`, hidden=true | `color/tabs/tab/outline/focus_visible` | 1 | Compliant |
| Spacing → `["GAP"]`, hidden=true | `spacing/tabs/...` | 5 | All compliant |
| Size — `/border` → `["STROKE_FLOAT"]`, hidden=true | `size/tabs/border_bottom/width` | 1 | Compliant |
| Size — dimension → `["WIDTH_HEIGHT"]`, hidden=true | `size/tabs/tab/indicator/height/...` | 2 | All compliant |
| Size — `/outline/` → `["STROKE_FLOAT"]`, hidden=true | `size/tabs/tab/outline/width/focus_visible` | 1 | Compliant |
| Radius → `["CORNER_RADIUS"]` | `radius/tabs/...` | 6 | All compliant |

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/2026-02-20-14-26-tabs-figma-token-mapping.csv`.
