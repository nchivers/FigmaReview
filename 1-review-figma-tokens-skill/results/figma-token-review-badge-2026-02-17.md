# Figma Token Review — badge

**Date:** 2026-02-17
**Component:** badge
**CSV tokens:** 166
**Figma badge variables:** 166

---

## Task 1: CSV vs Figma Comparison

### 1. Missing in Figma

None — all 166 CSV token names have a corresponding Figma variable.

### 2. Extra in Figma

None — the Figma badge variable set contains exactly the 166 tokens listed in the CSV.

### 3. Naming Discrepancies

None — all token names match exactly after converting CSV dot-notation (`affirm.color.badge.…`) to Figma slash-notation (`color/badge/…`).

### 4. Assignment Discrepancies

| CSV Token | Mode | CSV Expected | Figma Actual | Notes |
|-----------|------|-------------|-------------|-------|
| `affirm.color.badge.brand_tertiary.border` | Light | `opacity.000` | `base/color/opacity/transparent` | All other border tokens use `opacity.transparent` in the CSV; this one uses `opacity.000` |
| `affirm.color.badge.brand_tertiary.border` | Dark | `opacity.000` | `base/color/opacity/transparent` | Same as above |
| `affirm.color.badge.success.static.bg` | Dark | `green.100` → `base/color/green/100` | `color/green/100` (semantic alias) | Light Mode correctly points to `base/color/green/100`; Dark Mode aliases to a semantic-level token instead of the base token |
| `affirm.size.badge.medium.icon.all` | All Modes | `size.175` | `base/size/200` | Appears swapped with small |
| `affirm.size.badge.small.icon.all` | All Modes | `size.200` | `base/size/175` | Appears swapped with medium |

**Note on icon size swap:** The CSV specifies medium icon = `size.175` and small icon = `size.200`, but Figma has medium icon = `base/size/200` and small icon = `base/size/175`. The Figma values are logically correct (medium > small), suggesting the CSV values may be transposed.

**Note on brand_tertiary.border:** The CSV uses `opacity.000` while all other 35 border tokens in the CSV use `opacity.transparent`. Figma consistently uses `base/color/opacity/transparent` for all border tokens. This is likely a CSV typo — `opacity.000` and `opacity.transparent` are distinct variables.

**Note on success.static.bg Dark Mode:** The Figma variable's Dark Mode value aliases to `color/green/100` (a semantic variable) rather than `base/color/green/100` (a base primitive). The Light Mode correctly points to the base token. This inconsistency in alias level should be investigated.

---

## Task 2: Scoping Rule Violations

No violations found.

All Figma badge variables that match scoping rules have correct `scopes` and `hiddenFromPublishing` values:

| Rule Pattern | Tokens Checked | Expected Scopes | Expected Hidden | Result |
|-------------|----------------|-----------------|-----------------|--------|
| `color/{component}/` + `/bg/` | 36 tokens | `["FRAME_FILL","SHAPE_FILL"]` | `true` | All pass |
| `color/{component}/` + `/border/` | 36 tokens | `["STROKE_COLOR"]` | `true` | All pass |
| `color/{component}/` + `/icon/` | 36 tokens | must include `["SHAPE_FILL"]` | `true` | All pass (actual: `["FRAME_FILL","SHAPE_FILL"]`) |
| `color/{component}/` + `/text/` | 36 tokens | `["TEXT_FILL"]` | `true` | All pass |
| `size/{component}/` + `/border/` | 1 token | `["STROKE_FLOAT"]` | `true` | Pass |
| `size/{component}/` (dimension) | 3 tokens | `["WIDTH_HEIGHT"]` | `true` | All pass |
| `spacing/` (badge spacing) | 15 tokens | `["GAP"]` | `true` | All pass |
| `radius/` | 3 tokens | `["CORNER_RADIUS"]` | `true` | All pass |

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/figma-token-mapping-badge-2026-02-17.csv`.
