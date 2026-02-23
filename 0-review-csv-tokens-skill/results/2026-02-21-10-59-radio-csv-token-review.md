# CSV Token Review — Radio

## Inputs used

- **componentName:** radio (from `inputs/inputs.json`)
- **CSV:** `inputs/component-tokens.csv` — 14 segment columns, 3 assignment columns (All Modes, Light Mode, Dark Mode)
- **Naming rules:** `knowledge/token-naming-rules.md`

---

## 1. Naming issues

**1 issue found.**

| Row | Token | Segment | Issue |
|-----|-------|---------|-------|
| 134 | `affirm.size.radio.container.offset.focus_visible` | **foundation** / **property** | `offset` is a **spacing** property, not a **size** property. Per the controlled vocabulary, size properties are: `height`, `width`, `min_width`, `max_width`, `min_height`, `max_height`, `all`. The `offset` property belongs to the **spacing** foundation. Additionally, the focus-visible offset pattern specifies `affirm.spacing.{component}[...].outline.offset[.{state}].focus_visible`, suggesting the part should be `outline` rather than `container`. Expected: `affirm.spacing.radio.container.offset.focus_visible` (or `affirm.spacing.radio.outline.offset.focus_visible` per the focus-visible pattern). |

All other segments across all 134 data rows are valid:
- **Namespace:** `affirm` throughout — valid.
- **Foundation:** `color`, `position`, `radius`, `size`, `spacing` — all in the allowed list.
- **Component:** `radio` — valid (lowercase, no spaces).
- **Part:** `dot`, `indicator`, `container`, (empty) — all valid part names.
- **Property by foundation:** All valid except `offset` under `size` (flagged above).
- **State:** `selected`, `unselected`, `error_selected`, `error_unselected`, (empty) — all valid per controlled vocabulary.
- **Interaction:** `resting`, `hover`, `pressed`, `focus_visible`, `disabled`, (empty) — all valid.

---

## 2. Tokens missing assignments

**None.**

All tokens have the required base-token assignments:
- **Color tokens (rows 2–84):** Light Mode and Dark Mode values present for all rows.
- **Position tokens (rows 85–86):** All Modes value present.
- **Radius tokens (rows 87–92):** All Modes value present.
- **Size tokens (rows 93–134):** All Modes value present.
- **Spacing token (row 135):** All Modes value present.

---

## 3. Logically missing tokens

**13 suggestions for consideration.**

The standard interaction set observed in this component is: `resting`, `hover`, `pressed`, `focus_visible`, `disabled`. Several groups have all five interactions for normal states (`selected`, `unselected`) but only four for error states — missing `disabled`. The container outline group is also missing `disabled`.

### 3a. Color tokens missing `disabled` interaction for error states

| Part | Property | State | Present interactions | Missing |
|------|----------|-------|---------------------|---------|
| dot | border | error_selected | resting, hover, pressed, focus_visible | **disabled** |
| dot | border | error_unselected | resting, hover, pressed, focus_visible | **disabled** |
| indicator | border | error_selected | resting, hover, pressed, focus_visible | **disabled** |
| indicator | border | error_unselected | resting, hover, pressed, focus_visible | **disabled** |
| indicator | bg | error_selected | resting, hover, pressed, focus_visible | **disabled** |
| indicator | bg | error_unselected | resting, hover, pressed, focus_visible | **disabled** |

**Note:** `dot.bg` error states (error_selected, error_unselected) already include `disabled` — the gap is only on `dot.border`, `indicator.border`, and `indicator.bg`.

Suggested tokens:
- `affirm.color.radio.dot.border.error_selected.disabled`
- `affirm.color.radio.dot.border.error_unselected.disabled`
- `affirm.color.radio.indicator.border.error_selected.disabled`
- `affirm.color.radio.indicator.border.error_unselected.disabled`
- `affirm.color.radio.indicator.bg.error_selected.disabled`
- `affirm.color.radio.indicator.bg.error_unselected.disabled`

### 3b. Container outline missing `disabled` interaction

| Part | Property | State | Present interactions | Missing |
|------|----------|-------|---------------------|---------|
| container | outline | (none) | resting, hover, pressed, focus_visible | **disabled** |

Suggested token:
- `affirm.color.radio.container.outline.disabled`

### 3c. Size border-width tokens missing `disabled` for error states

| Part | Subpart | Property | State | Present interactions | Missing |
|------|---------|----------|-------|---------------------|---------|
| dot | border | width | error_selected | resting, hover, pressed, focus_visible | **disabled** |
| dot | border | width | error_unselected | resting, hover, pressed, focus_visible | **disabled** |
| indicator | border | width | error_selected | resting, hover, pressed, focus_visible | **disabled** |
| indicator | border | width | error_unselected | resting, hover, pressed, focus_visible | **disabled** |

Suggested tokens:
- `affirm.size.radio.dot.border.width.error_selected.disabled`
- `affirm.size.radio.dot.border.width.error_unselected.disabled`
- `affirm.size.radio.indicator.border.width.error_selected.disabled`
- `affirm.size.radio.indicator.border.width.error_unselected.disabled`

### 3d. Radius container missing `disabled` interaction

| Part | Property | State | Present interactions | Missing |
|------|----------|-------|---------------------|---------|
| container | all | (none) | resting, hover, pressed, focus_visible | **disabled** |

Suggested token:
- `affirm.radius.radio.container.all.disabled`

### 3e. Text tokens — consider error state

Other parts (dot, indicator) differentiate between normal and error states (e.g., `selected` vs `error_selected`). The text tokens have no state segment. If the label text color should change when the radio is in an error state, consider adding error-state text tokens (e.g., `affirm.color.radio.text.error.resting`, etc.).

---

## Summary

| Category | Count |
|----------|-------|
| Naming issues | 1 |
| Missing assignments | 0 |
| Logically missing tokens (for consideration) | 13 |
| **Total findings** | **14** |
