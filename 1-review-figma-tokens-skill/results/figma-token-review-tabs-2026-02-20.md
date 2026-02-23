# Figma Token Review — Tabs

**Component:** tabs
**Date:** 2026-02-20
**CSV tokens:** 47
**Figma variables matched:** 47

---

## Task 1: CSV vs Figma

### Missing in Figma

None. All 47 CSV tokens have a corresponding Figma variable.

### Extra in Figma

None. Every Figma variable containing `tabs` in its name maps to a CSV token.

### Naming Discrepancies

None. The CSV uses `affirm.{category}.tabs.{path}` (dot-separated) and Figma uses `{category}/tabs/{path}` (slash-separated). After removing the `affirm.` prefix and converting dots to slashes, all names match exactly (case-sensitive). Underscored segments (e.g. `content_container`, `border_bottom`, `focus_visible`) are consistent between both sources.

### Assignment Discrepancies

None. All alias assignments in Figma match the expected values from the CSV:

- **Color tokens (Light/Dark modes):** Each CSV value (e.g. `gray.950`) matches the corresponding Figma alias (e.g. `base/g-color/gray/950`). All 32 color tokens verified across both modes.
- **Radius tokens (All Modes):** Each CSV value (e.g. `size.150`) matches the corresponding Figma alias (e.g. `base/size/150`). All 6 radius tokens verified.
- **Size tokens (All Modes):** Each CSV value matches the Figma alias. All 4 size tokens verified.
- **Spacing tokens (All Modes):** Each CSV value matches the Figma alias. All 5 spacing tokens verified.

---

## Task 2: Scoping Rule Violations

### 1. `color/tabs/border` — incorrect scopes

| Field | Expected | Actual |
|-------|----------|--------|
| **Rule applied** | `^color/{component}/` AND name contains `/border` → scopes must equal `["STROKE_COLOR"]`, hiddenFromPublishing must equal `true` | |
| **scopes** | `["STROKE_COLOR"]` | `["ALL_SCOPES"]` |
| **hiddenFromPublishing** | `true` | `true` (correct) |

**Issue:** The variable's scopes are set to `ALL_SCOPES` instead of the required `STROKE_COLOR`. This allows the variable to be used in any scope context (fill, text, stroke, etc.) rather than being restricted to stroke usage only.

### 2. `size/tabs/border_bottom/width` — rule ambiguity / possible violation

| Field | Expected | Actual |
|-------|----------|--------|
| **Matching rule** | Generic dimension rule: `name contains component name AND represents dimension` → scopes must equal `["WIDTH_HEIGHT"]`, hiddenFromPublishing must equal `true` | |
| **scopes** | `["WIDTH_HEIGHT"]` (per generic rule) | `["STROKE_FLOAT"]` |
| **hiddenFromPublishing** | `true` | `true` (correct) |

**Note:** The specific size-border rule (`name contains "/border/"` — with trailing slash) does not match because the Figma name uses `/border_bottom/` as a single path segment rather than `/border/`. The generic dimension rule therefore applies, expecting `["WIDTH_HEIGHT"]`. However, `STROKE_FLOAT` is semantically correct for a border width. Consider either:
- Renaming the variable to `size/tabs/border/bottom/width` so the specific border rule matches, or
- Accepting `STROKE_FLOAT` as intentional and documenting the exception.

### Compliant tokens by rule

| Rule | Tokens | Count | Result |
|------|--------|-------|--------|
| Component color — `/text` → `["TEXT_FILL"]`, hidden=true | `color/tabs/tab/text/...` | 10 | All compliant |
| Component color — `/bg` → `["FRAME_FILL","SHAPE_FILL"]`, hidden=true | `color/tabs/tab/content_container/bg/...` | 10 | All compliant |
| Component color — `/fill` → `["FRAME_FILL","SHAPE_FILL"]`, hidden=true | `color/tabs/tab/indicator/fill/...` | 10 | All compliant |
| Component color — `/outline` → `["STROKE_COLOR"]`, hidden=true | `color/tabs/tab/outline/focus_visible` | 1 | Compliant |
| Spacing → `["GAP"]`, hidden=true | `spacing/tabs/...` | 5 | All compliant |
| Size — dimension → `["WIDTH_HEIGHT"]`, hidden=true | `size/tabs/tab/indicator/height/...` | 2 | All compliant |
| Size — `/outline/` → `["STROKE_FLOAT"]`, hidden=true | `size/tabs/tab/outline/width/focus_visible` | 1 | Compliant |
| Radius → `["CORNER_RADIUS"]` | `radius/tabs/...` | 6 | All compliant |

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/figma-token-mapping-tabs-2026-02-20.csv`.
