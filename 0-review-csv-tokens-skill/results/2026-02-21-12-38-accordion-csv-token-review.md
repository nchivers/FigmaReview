# CSV Token Review — Accordion

## Inputs used

| Input | Value |
|-------|-------|
| **componentName** | `accordion` (from `inputs/inputs.json`) |
| **CSV** | `inputs/component-tokens.csv` (14 segment columns, 31 token rows) |
| **Naming rules** | `knowledge/token-naming-rules.md` |

---

## 1. Naming issues

None. All 31 tokens conform to the naming rules:

- **Namespace:** All rows use `affirm` — valid.
- **Foundation:** Values used (`color`, `size`, `spacing`, `radius`) are all in the allowed set.
- **Component:** `accordion` — valid (no spaces, underscore convention followed).
- **Optional segments** (variant, size-variant, context, polarity, persistence): Correctly omitted (empty) where not applicable.
- **Part:** Values used (`container`, `header`, `outline`) are valid element names.
- **Subpart:** `icon` used once (row 29, spacing for header icon margin) — valid.
- **Property:** Each property is valid for its foundation:
  - Color: `bg`, `text`, `icon`, `outline` — all allowed.
  - Size: `width` — allowed.
  - Spacing: `margin_bottom`, `offset` — allowed.
  - Radius: `all` — allowed.
- **State:** `closed`, `open` — both in the allowed state list.
- **Interaction:** `resting`, `hover`, `pressed`, `focus_visible`, `disabled` — all in the allowed interaction list.
- **Token-building patterns:** Focus-visible outline tokens (color, size, spacing) follow the documented focus-visible patterns. Icon color tokens correctly use `icon` as the property. Transparent backgrounds use `opacity.000` as required.

---

## 2. Tokens missing assignments

None. All assignments are present:

- **Dual-mode tokens (color, rows 1–27):** All 27 color tokens have both Light Mode and Dark Mode values populated.
- **Single-mode tokens (size/spacing/radius, rows 28–31):** All 4 tokens have All Modes values populated.

---

## 3. Logically missing tokens

The following tokens appear logically missing based on interaction-state patterns across groups. Marked **for consideration** (not hard failures).

### Missing `resting` interaction for header text and header icon

The `container.bg` group has all five interactions (`resting`, `hover`, `pressed`, `focus_visible`, `disabled`) for both `closed` and `open` states. However, the `header.text` and `header.icon` groups have only four interactions — they are missing `resting`:

| Suggested token | Reason |
|-----------------|--------|
| `affirm.color.accordion.header.text.closed.resting` | header.text has hover, pressed, focus_visible, disabled for closed — missing resting |
| `affirm.color.accordion.header.text.open.resting` | header.text has hover, pressed, focus_visible, disabled for open — missing resting |
| `affirm.color.accordion.header.icon.closed.resting` | header.icon has hover, pressed, focus_visible, disabled for closed — missing resting |
| `affirm.color.accordion.header.icon.open.resting` | header.icon has hover, pressed, focus_visible, disabled for open — missing resting |

**Note:** It is possible the header text and icon intentionally inherit their resting color from a global or parent token and don't need component-specific resting tokens. If so, this can be disregarded.

---

## Summary

| Category | Count |
|----------|-------|
| Naming issues | 0 |
| Missing assignments | 0 |
| Logically missing tokens (for consideration) | 4 |
