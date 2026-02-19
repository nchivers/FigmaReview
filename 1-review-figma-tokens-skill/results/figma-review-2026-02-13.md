# Figma Variables Review — 2026-02-13

---

## Task 1: CSV vs Figma

**Token name mapping:** CSV tokens use `affirm.{type}.{path}` with dot separators (e.g. `affirm.color.merchant_tile.container.bg.hover`). Figma variables use `{type}/{path}` with slash separators (e.g. `color/merchant_tile/container/bg/hover`). The `affirm.` prefix is stripped and dots are converted to slashes for matching.

### Missing in Figma

None — all 36 CSV tokens have a corresponding Figma variable.

### Extra in Figma

None — the 36 Figma `merchant_tile` variables map 1-to-1 with the 36 CSV tokens.

### Naming discrepancies

2 tokens use a **space** in Figma where the CSV uses an **underscore** in the final path segment:

| CSV token | Expected Figma name | Actual Figma name |
|---|---|---|
| `affirm.size.merchant_tile.container.outline.width.focus_visible` | `size/merchant_tile/container/outline/width/focus_visible` | `size/merchant_tile/container/outline/width/focus visible` |
| `affirm.spacing.merchant_tile.container.outline.offset.focus_visible` | `spacing/merchant_tile/container/outline/offset/focus_visible` | `spacing/merchant_tile/container/outline/offset/focus visible` |

**Note:** All other `focus_visible` tokens in Figma use the underscore correctly (e.g. `color/merchant_tile/container/bg/focus_visible`). Only these two size/spacing tokens use a space.

### Assignment discrepancies

None — all alias targets in Figma match the expected values from the CSV across all modes.

**Color tokens (Light/Dark modes):** All 21 color variables resolve to the correct `base/g-color/{color}/{shade}` aliases matching the CSV's `{color}.{shade}` values. For example:
- `color/merchant_tile/container/bg/hover` → Light: `base/g-color/indigo/050` (CSV: `indigo.050`) ✓, Dark: `base/g-color/gray/850` (CSV: `gray.850`) ✓

**Spacing, size, radius, and position tokens (single mode):** All 15 non-color variables resolve to the correct `base/size/{value}` aliases matching the CSV's `size.{value}` entries. For example:
- `spacing/merchant_tile/merchant_info/padding_x` → `base/size/100` (CSV: `size.100`) ✓

---

## Task 2: Scoping rule violations

Only the 36 Figma variables corresponding to CSV tokens were evaluated against the rules in `knowledge/scoping-rules.md`.

### Violations

**No scoping rule violations found.** All variables that match an applicable rule have the correct `scopes` and `hiddenFromPublishing` values.

### Detailed evaluation by rule

| Rule | Tokens checked | Expected scopes | Expected hidden | Result |
|------|---------------|-----------------|-----------------|--------|
| Component color `/bg/` → `["FRAME_FILL","SHAPE_FILL"]`, hidden=true | 4 | `["FRAME_FILL","SHAPE_FILL"]` | `true` | Pass |
| Component color `/text/` → `["TEXT_FILL"]`, hidden=true | 8 | `["TEXT_FILL"]` | `true` | Pass |
| Component color `/icon/` → includes `["SHAPE_FILL"]`, hidden=true | 4 | includes `SHAPE_FILL` | `true` | Pass |
| Component color `/border/` → `["STROKE_COLOR"]`, hidden=true | 4 | `["STROKE_COLOR"]` | `true` | Pass |
| Spacing → `["GAP"]`, component hidden=true | 6 | `["GAP"]` | `true` | Pass |
| Radius → `["CORNER_RADIUS"]` | 2 | `["CORNER_RADIUS"]` | — | Pass |
| Size component `/outline/` → `["STROKE_FLOAT"]`, hidden=true | 1 | `["STROKE_FLOAT"]` | `true` | Pass |
| Size component dimension → `["WIDTH_HEIGHT"]`, hidden=true | 2 | `["WIDTH_HEIGHT"]` | `true` | Pass |

### Tokens with no matching rule (not evaluated)

- `color/merchant_tile/container/outline/focus_visible` — no component color rule covers `/outline/` pattern (actual: scopes `["STROKE_COLOR"]`, hidden `false`)
- `position/merchant_tile/merchant_img/merchant_logo/left` — no position rules defined
- `position/merchant_tile/merchant_img/merchant_logo/bottom` — no position rules defined
- `position/merchant_tile/badge/left` — no position rules defined
- `position/merchant_tile/badge/top` — no position rules defined

---

## Summary

| Category | Count |
|----------|-------|
| CSV tokens | 36 |
| Figma variables (merchant_tile) | 36 |
| Missing in Figma | 0 |
| Extra in Figma | 0 |
| Naming discrepancies | 2 |
| Assignment discrepancies | 0 |
| Scoping violations | 0 |
