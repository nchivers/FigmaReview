# CSV Token Review — text_input

## Inputs used

| Input | Path |
|-------|------|
| componentName | `text_input` (from `inputs/inputs.json`) |
| Component tokens CSV | `inputs/component-tokens.csv` (14 segment columns) |
| Token naming rules | `knowledge/token-naming-rules.md` |

---

## 1. Naming issues

None. All 131 token rows were validated against the naming rules:

- **Namespace:** All rows use `affirm` — valid.
- **Foundation:** Values used — `color`, `radius`, `size`, `spacing` — all in the allowed set.
- **Component:** `input_text` — uses underscores per rules.
- **Variant, Size-Variant, Context, Polarity, Persistence:** All empty (optional segments) — valid.
- **Part:** Values used — `input`, `message`, `error_message`, (empty) — all reasonable element names.
- **Part-Variant:** Empty in all rows — valid.
- **Subpart:** Values used — `cursor`, `label`, `value`, `icon`, `border`, `outline`, `label_value`, (empty) — all reasonable element names.
- **Property by foundation:**
  - Color: `bg`, `border`, `outline`, `fill`, `icon`, `text` — all in the allowed color property set.
  - Radius: `all` — valid.
  - Size: `all`, `min_height`, `width` — all in the allowed size property set.
  - Spacing: `gap_y`, `gap_x`, `padding_x`, `padding_y`, `offset` — all in the allowed spacing property set.
- **State:** Values used — `empty`, `filled`, `error_empty`, `error_filled` — all in the allowed state/composite-state set.
- **Interaction:** Values used — `resting`, `hover`, `focus`, `focus_visible`, `pressed`, `disabled` — all in the allowed interaction set.
- **Token-building patterns:** Icon color tokens use `icon` as property; icon size tokens use `all` as property with `icon` as subpart. Border size tokens use `width` as property with `border` as subpart. Outline color tokens correctly use `outline` as property with `focus_visible` interaction. Cursor tokens use `fill` as property with `cursor` as subpart. All patterns align with the documented token-building rules.

---

## 2. Tokens missing assignments

None. All tokens have the required base-token assignments:

- **Color tokens (119 rows):** All have both **Light Mode** and **Dark Mode** values populated.
- **Radius tokens (1 row):** `affirm.radius.input_text.input.all` has **All Modes** = `size.100`.
- **Size tokens (4 rows):** All have **All Modes** values (`size.300`, `size.700`, `size.013`, `size.025`).
- **Spacing tokens (7 rows):** All have **All Modes** values (`size.100`, `size.150`, `size.025`, `size.200`, `size.200`, `size.100`, `size.025`).

---

## 3. Logically missing tokens

All existing state/interaction groups have complete interaction coverage. No missing interactions were found within any group:

| Part / Subpart | Property | States present | Interactions per non-error state | Interactions per error state |
|---|---|---|---|---|
| input | bg | empty, filled, error_empty, error_filled | resting, hover, pressed, focus_visible, focus, disabled (6) | resting, hover, pressed, focus_visible, focus (5 — no disabled per error rule) |
| input | border | empty, filled, error_empty, error_filled | 6 | 5 |
| input | outline | empty, filled, error_empty, error_filled | focus_visible only (1) | focus_visible only (1) |
| input > cursor | fill | empty, filled, error_empty, error_filled | focus only (1) | focus only (1) |
| input | icon | empty, filled, error_empty, error_filled | 6 | 5 |
| input > label | text | empty, filled, error_empty, error_filled | 6 | 5 |
| input > value | text | filled, error_filled | 6 | 5 |
| message | text | (no state) | 6 | — |
| error_message | text | (no state) | 5 (no disabled) | — |

**Notes for consideration:**

- **`error_message.text` has no `disabled` interaction.** The error handling rule exempts error *states* (e.g. `error_empty`, `error_filled`) from needing `disabled`. `error_message` is technically a *part* name, not a state. However, in practice an error message would not display on a disabled component, so omitting `disabled` is reasonable. Flag for team discussion if strict consistency is preferred.
- **No placeholder text tokens.** If the component uses a floating-label pattern (label moves into the input when empty), the existing `input.label.text.empty.*` tokens cover placeholder appearance. If the design has a *separate* placeholder element distinct from the label, tokens such as `affirm.color.input_text.input.placeholder.text.empty.{interaction}` would be needed.
- **No shadow tokens.** If the design uses box-shadows on the input (e.g. for depth or focus indication), `shadow` foundation tokens would be needed. Omission is fine if the design relies on borders/outlines only.

---

## Summary

| Category | Count |
|----------|-------|
| Naming issues | 0 |
| Missing assignments | 0 |
| Logically missing tokens (for consideration) | 0 hard issues; 3 advisory notes |

**Total token rows reviewed:** 131
