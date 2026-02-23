# Figma Token Review: text_input

**Date:** 2026-02-21
**Component:** text_input
**CSV tokens:** 130
**Figma variables (input_text):** 123

---

## Task 1: CSV vs Figma Comparison

### Missing in Figma (20 tokens not matched by exact name)

Of these 20, **12 have naming near-matches** in Figma (the variable exists but the name differs), and **8 are truly absent** (no equivalent Figma variable found).

#### Category A: Naming near-matches (12 tokens)

**A1. Underscore vs hyphen — `focus_visible` vs `focus-visible` (3 tokens)**

| CSV Token | Expected Figma Name | Actual Figma Name |
|---|---|---|
| `affirm.color.input_text.input.bg.empty.focus_visible` | `color/input_text/input/bg/empty/focus_visible` | `color/input_text/input/bg/empty/focus-visible` |
| `affirm.color.input_text.input.border.empty.focus_visible` | `color/input_text/input/border/empty/focus_visible` | `color/input_text/input/border/empty/focus-visible` |
| `affirm.color.input_text.input.bg.error_empty.focus_visible` | `color/input_text/input/bg/error_empty/focus_visible` | `color/input_text/input/bg/empty/error_empty/focus-visible` |

> The CSV uses `focus_visible` (underscore) while Figma uses `focus-visible` (hyphen). This should be reconciled to a single convention.

**A2. Path structure — `bg/error_empty/` vs `bg/empty/error_empty/` (5 tokens)**

| CSV Token | Expected Figma Name | Actual Figma Name |
|---|---|---|
| `affirm.color.input_text.input.bg.error_empty.resting` | `color/input_text/input/bg/error_empty/resting` | `color/input_text/input/bg/empty/error_empty/resting` |
| `affirm.color.input_text.input.bg.error_empty.hover` | `color/input_text/input/bg/error_empty/hover` | `color/input_text/input/bg/empty/error_empty/hover` |
| `affirm.color.input_text.input.bg.error_empty.pressed` | `color/input_text/input/bg/error_empty/pressed` | `color/input_text/input/bg/empty/error_empty/pressed` |
| `affirm.color.input_text.input.bg.error_empty.focus_visible` | `color/input_text/input/bg/error_empty/focus_visible` | `color/input_text/input/bg/empty/error_empty/focus-visible` |
| `affirm.color.input_text.input.bg.error_empty.focus` | `color/input_text/input/bg/error_empty/focus` | `color/input_text/input/bg/empty/error_empty/focus` |

> The CSV groups `error_empty` as a sibling of `empty` under `bg/`, but Figma nests `error_empty` inside `empty/` (`bg/empty/error_empty/`). The hierarchy should be aligned.

**A3. Missing `/text` segment — `error_message/text/` vs `error_message/` (5 tokens)**

| CSV Token | Expected Figma Name | Actual Figma Name |
|---|---|---|
| `affirm.color.input_text.error_message.text.resting` | `color/input_text/error_message/text/resting` | `color/input_text/error_message/resting` |
| `affirm.color.input_text.error_message.text.hover` | `color/input_text/error_message/text/hover` | `color/input_text/error_message/hover` |
| `affirm.color.input_text.error_message.text.focus` | `color/input_text/error_message/text/focus` | `color/input_text/error_message/focus` |
| `affirm.color.input_text.error_message.text.focus_visible` | `color/input_text/error_message/text/focus_visible` | `color/input_text/error_message/focus_visible` |
| `affirm.color.input_text.error_message.text.pressed` | `color/input_text/error_message/text/pressed` | `color/input_text/error_message/pressed` |

> Note: `color/input_text/error_message/resting` exists in Figma but is listed under "Extra in Figma" below because it only matches if we strip the `/text` segment. The CSV includes a `text` segment in the path (`error_message/text/`) while Figma omits it (`error_message/`). This difference should be resolved — either the CSV should drop the `text` segment or Figma should add it.

#### Category B: Truly missing — no Figma equivalent (8 tokens)

| CSV Token | Expected Figma Name | Category |
|---|---|---|
| `affirm.radius.input_text.input.all` | `radius/input_text/input/all` | Radius |
| `affirm.spacing.input_text.gap_y` | `spacing/input_text/gap_y` | Spacing |
| `affirm.spacing.input_text.input.gap_x` | `spacing/input_text/input/gap_x` | Spacing |
| `affirm.spacing.input_text.input.label_value.gap_y` | `spacing/input_text/input/label_value/gap_y` | Spacing |
| `affirm.spacing.input_text.input.padding_x` | `spacing/input_text/input/padding_x` | Spacing |
| `affirm.spacing.input_text.input.padding_y.empty` | `spacing/input_text/input/padding_y/empty` | Spacing |
| `affirm.spacing.input_text.input.padding_y.filled` | `spacing/input_text/input/padding_y/filled` | Spacing |
| `affirm.spacing.input_text.input.outline.offset` | `spacing/input_text/input/outline/offset` | Spacing |

> All radius and spacing tokens defined in the CSV are completely absent from Figma. No `radius/input_text/` or `spacing/input_text/` variables exist in the Figma variable set.

---

### Extra in Figma (1 variable)

These Figma variables contain `input_text` in their name but do not correspond to any CSV token (after accounting for near-matches above):

| Figma Name | Figma ID |
|---|---|
| `color/input_text/input/value/text/empty/resting` | `VariableID:15372:5926` |

> The CSV defines `value/text` tokens only for `filled` and `error_filled` states, not for `empty`. Figma has an additional `empty/resting` variable that is not in the CSV.

---

### Naming Discrepancies

See **Category A** under "Missing in Figma" above. Summary of patterns:

1. **`focus_visible` vs `focus-visible`** — 3 tokens use underscore in CSV but hyphen in Figma
2. **`bg/error_empty/` vs `bg/empty/error_empty/`** — 5 tokens have different nesting hierarchy
3. **`error_message/text/` vs `error_message/`** — 5 tokens differ by a `/text` path segment

---

### Assignment Discrepancies

| CSV Token | Mode | CSV Expected | Figma Alias |
|---|---|---|---|
| `affirm.color.input_text.input.label.text.filled.focus` | Light Mode | `indigo.970` | `base/g-color/indigo/950` |

> The CSV specifies `indigo.970` for the light mode value, but the Figma variable aliases to `indigo/950`. This is a value mismatch that should be investigated.

---

## Task 2: Scoping Rule Violations

### Background (`/bg`) tokens — missing `SHAPE_FILL` scope (16 violations)

All 16 background color tokens have `scopes: ["FRAME_FILL"]` but the rule requires `scopes: ["FRAME_FILL", "SHAPE_FILL"]`.

**Rule:** Component color with `/bg` → scopes must equal `["FRAME_FILL", "SHAPE_FILL"]`, hiddenFromPublishing = true

| Variable | Expected Scopes | Actual Scopes |
|---|---|---|
| `color/input_text/input/bg/empty/resting` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/empty/hover` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/empty/pressed` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/empty/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/empty/disabled` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/filled/resting` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/filled/hover` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/filled/pressed` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/filled/focus_visible` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/filled/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/filled/disabled` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/error_filled/resting` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/error_filled/hover` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/error_filled/pressed` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/error_filled/focus_visible` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |
| `color/input_text/input/bg/error_filled/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["FRAME_FILL"]` |

> All background tokens are missing the `SHAPE_FILL` scope. They currently have only `FRAME_FILL`.

### Cursor fill tokens — incorrect scope (4 violations)

**Rule:** Component color with `/fill` → scopes must equal `["FRAME_FILL", "SHAPE_FILL"]`, hiddenFromPublishing = true

| Variable | Expected Scopes | Actual Scopes |
|---|---|---|
| `color/input_text/input/cursor/fill/empty/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["STROKE_COLOR"]` |
| `color/input_text/input/cursor/fill/filled/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["STROKE_COLOR"]` |
| `color/input_text/input/cursor/fill/error_empty/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["STROKE_COLOR"]` |
| `color/input_text/input/cursor/fill/error_filled/focus` | `["FRAME_FILL", "SHAPE_FILL"]` | `["STROKE_COLOR"]` |

> All cursor fill tokens have `STROKE_COLOR` but the `/fill` rule requires `["FRAME_FILL", "SHAPE_FILL"]`. Note: if cursor colors are intentionally applied as strokes in the design, the scoping rules may need a cursor-specific exception.

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/2026-02-21-12-04-text_input-figma-token-mapping.csv`.
