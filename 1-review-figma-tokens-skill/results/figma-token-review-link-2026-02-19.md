# Figma Token Review: link

**Date:** 2026-02-19
**Component:** link
**CSV tokens:** 32
**Figma matches:** 32

---

## Task 1: CSV vs Figma

### Missing in Figma

None — all 32 CSV tokens have a matching Figma variable.

### Extra in Figma

None — every Figma variable scoped to the link component (`color/link/*`, `radius/link/*`, `size/link/*`, `spacing/link/*`) has a corresponding row in the CSV.

### Naming Discrepancies

None — CSV token names map to Figma names with a consistent transform (strip `affirm.` prefix, replace `.` with `/`), and all matches are exact.

### Assignment Discrepancies

None — all alias targets in Figma match the expected values from the CSV:

| Category | Tokens checked | Result |
|---|---|---|
| color/link/text/* (5 tokens) | Light & Dark mode aliases | All match (indigo.950/indigo.300 for active states; gray.400/gray.600 for disabled) |
| color/link/container/bg/* (5 tokens) | Light & Dark mode aliases | All match (opacity.000 for resting/disabled; indigo/gray shades for interactive states) |
| color/link/icon/* (5 tokens) | Light & Dark mode aliases | All match (same pattern as text tokens) |
| color/link/outline/focus_visible (1 token) | Light & Dark mode aliases | Match (indigo.650/indigo.650) |
| radius/link/* (10 tokens) | All Modes alias | All match (size.100 for top, size.000 for bottom) |
| size/link/* (4 tokens) | All Modes alias | All match (size.250/200/175 for icon sizes, size.025 for outline width) |
| spacing/link/* (2 tokens) | All Modes alias | All match (size.025) |

---

## Task 2: Scoping Rule Violations

No violations found. All 32 tokens pass their applicable scoping rules:

| Token group | Rule applied | Expected scopes | Actual scopes | hiddenFromPublishing |
|---|---|---|---|---|
| color/link/text/* (5) | Component color + `/text/` | `["TEXT_FILL"]` | `["TEXT_FILL"]` | true (expected true) |
| color/link/container/bg/* (5) | Component color + `/bg/` | `["FRAME_FILL","SHAPE_FILL"]` | `["FRAME_FILL","SHAPE_FILL"]` | true (expected true) |
| color/link/icon/* (5) | Component color + `/icon/` | must include `["SHAPE_FILL"]` | `["FRAME_FILL","SHAPE_FILL"]` | true (expected true) |
| color/link/outline/focus_visible (1) | Component color + `/outline/` | `["STROKE_COLOR"]` | `["STROKE_COLOR"]` | true (expected true) |
| radius/link/* (10) | startsWith `radius/` | `["CORNER_RADIUS"]` | `["CORNER_RADIUS"]` | true |
| size/link/large/icon/all (1) | Component dimension | `["WIDTH_HEIGHT"]` | `["WIDTH_HEIGHT"]` | true (expected true) |
| size/link/medium/icon/all (1) | Component dimension | `["WIDTH_HEIGHT"]` | `["WIDTH_HEIGHT"]` | true (expected true) |
| size/link/small/icon/all (1) | Component dimension | `["WIDTH_HEIGHT"]` | `["WIDTH_HEIGHT"]` | true (expected true) |
| size/link/outline/width/focus_visible (1) | `^size/{component}/` + `/outline/` | `["STROKE_FLOAT"]` | `["STROKE_FLOAT"]` | true (expected true) |
| spacing/link/gap_x (1) | spacing collection | `["GAP"]` | `["GAP"]` | true (expected true) |
| spacing/link/outline/offset/focus_visible (1) | spacing collection | `["GAP"]` | `["GAP"]` | true (expected true) |

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/figma-token-mapping-link-2026-02-19.csv`.
