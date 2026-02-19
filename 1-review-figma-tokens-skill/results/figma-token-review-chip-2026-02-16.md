# Figma Token Review — chip

**Date:** 2026-02-16

---

## Task 1: CSV vs Figma

Token names were matched by stripping the `affirm.` prefix from CSV tokens and replacing `.` with `/` to align with Figma's slash-separated naming convention.

### Missing in Figma

None — all 54 CSV tokens have a corresponding Figma variable (exact match after normalization), except the one naming discrepancy listed below.

### Extra in Figma

The following Figma variables contain `chip` but are not listed in the CSV:

- `spacing/chip/icon_only/large/padding_x` (VariableID:16716:1388)
- `spacing/chip/icon_only/large/padding_y` (VariableID:16716:1389)
- `spacing/chip/icon_only/small/padding_x` (VariableID:16716:1391)
- `spacing/chip/icon_only/small/padding_y` (VariableID:16716:1392)

### Naming Discrepancies

| CSV Token | Expected Figma Name | Actual Figma Name | Difference |
|---|---|---|---|
| `affirm.color.chip.indicator.focus_visible` | `color/chip/indicator/focus_visible` | `color/chip/indicator/focus-visible` | Hyphen (`-`) instead of underscore (`_`) in `focus-visible` segment |

This is the only token where the Figma name uses a hyphen while the CSV (and all other chip tokens) use an underscore for the `focus_visible` state.

### Assignment Discrepancies

| CSV Token | Mode | CSV Expected | Figma Actual Alias | Notes |
|---|---|---|---|---|
| `affirm.color.chip.container.bg.resting` | Light Mode | `opacity.000` | `base/color/opacity/transparent` | CSV expects alias tail `opacity/000`; Figma resolves to `opacity/transparent` |
| `affirm.color.chip.container.bg.resting` | Dark Mode | `opacity.000` | `base/color/opacity/transparent` | Same as above |

All other token assignments match their expected values.

---

## Task 2: Scoping Rule Violations

### Violations Found

| Variable Name | Rule Applied | Expected Scopes | Actual Scopes | Expected hiddenFromPublishing | Actual hiddenFromPublishing |
|---|---|---|---|---|---|
| `color/chip/outline/focus_visible` | Component color — contains `/outline/` | `["STROKE_COLOR"]` | `["ALL_SCOPES"]` | `true` | `false` |
| `spacing/chip/outline/offset/focus_visible` | Spacing — name startsWith `spacing/` | `["GAP"]` | `["ALL_SCOPES"]` | `true` | `false` |

#### Details

1. **`color/chip/outline/focus_visible`** (VariableID:19236:1595)
   - **Rule:** `IF name matches "^color/{component}/" AND name contains "/outline/"` → scopes must equal `["STROKE_COLOR"]`, hiddenFromPublishing must equal `true`
   - **Actual scopes:** `["ALL_SCOPES"]` — should be `["STROKE_COLOR"]`
   - **Actual hiddenFromPublishing:** `false` — should be `true`

2. **`spacing/chip/outline/offset/focus_visible`** (VariableID:19251:1614)
   - **Rule:** `IF name startsWith "spacing/"` → scopes must equal `["GAP"]`; and `IF name contains component name AND represents spacing` → hiddenFromPublishing must equal `true`
   - **Actual scopes:** `["ALL_SCOPES"]` — should be `["GAP"]`
   - **Actual hiddenFromPublishing:** `false` — should be `true`

### Additional Observations (No Rule Match — Not Violations)

The following indicator tokens do not match any specific sub-pattern rule (no `/text/`, `/icon/`, `/bg/`, `/border/`, or `/outline/` segment), so no scoping rule applies. However, they have `hiddenFromPublishing: false` and `scopes: ["ALL_SCOPES"]`, which differs from all other chip component tokens:

- `color/chip/indicator/resting`
- `color/chip/indicator/hover`
- `color/chip/indicator/pressed`
- `color/chip/indicator/focus-visible`
- `color/chip/indicator/disabled`

---

## Token Mapping

The full CSV-to-Figma token mapping is in `results/figma-token-mapping-chip-2026-02-16.csv`.
