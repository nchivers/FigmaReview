# CSV Token Review — Accordion

## Inputs used

- **componentName:** accordion (from `inputs/inputs.json`)
- **CSV:** `inputs/component-tokens.csv` (14 segment columns, 40 token rows)
- **Naming rules:** `0-review-csv-tokens-skill/knowledge/token-naming-rules.md`

---

## 1. Naming issues

None.

All 40 tokens pass segment validation against token-naming-rules.md:

- **Namespace:** `affirm` — valid for consumer-facing, logged-in experiences.
- **Foundation:** `color`, `size`, `spacing`, `radius` — all in the allowed set.
- **Component:** `accordion` — valid (lowercase, no spaces).
- **Optional segments** (variant, size_variant, context, polarity, persistence): all empty where not applicable — valid.
- **Part:** `container`, `header`, `outline`, or empty — all recognised element names.
- **Part-variant:** all empty — valid.
- **Subpart:** `icon` or empty — valid element within the subcomponent.
- **Property values** match their foundation's allowed set:
  - Color: `bg`, `text`, `icon`, `outline` — all valid.
  - Size: `width`, `all` — valid.
  - Spacing: `margin_bottom`, `margin_top`, `offset`, `gap_x`, `padding_x`, `padding_y` — all valid.
  - Radius: `all` — valid.
- **State:** `closed`, `open`, or empty — all in the allowed state vocabulary.
- **Interaction:** `resting`, `hover`, `pressed`, `focus_visible`, `disabled`, or empty — all valid.
- **Token-building patterns** correctly followed:
  - Icon color tokens use `icon` as the property (e.g. `affirm.color.accordion.header.icon.closed.hover`).
  - Icon size token uses part=`header`, subpart=`icon`, property=`all` (e.g. `affirm.size.accordion.header.icon.all`).
  - Focus-visible outline tokens follow the outline pattern: color (`affirm.color.accordion.outline.focus_visible`), size (`affirm.size.accordion.outline.width.focus_visible`), spacing (`affirm.spacing.accordion.outline.offset.focus_visible`).
  - Transparent backgrounds use `opacity.000` base token (e.g. container bg in resting and disabled states).

---

## 2. Tokens missing assignments

None.

- **Dual-mode (color) — 27 tokens:** All have both Light Mode and Dark Mode values.
- **Single-mode (size, spacing, radius) — 13 tokens:** All have an All Modes value.

---

## 3. Logically missing tokens

All existing part/property/state groups have complete interaction sets. The items below are **for consideration**, not hard failures.

### Complete interaction coverage confirmed

| Part | Property | States | Interactions present |
|------|----------|--------|---------------------|
| container | bg | closed, open | resting, hover, pressed, focus_visible, disabled |
| header | text | closed, open | resting, hover, pressed, focus_visible, disabled |
| header | icon | closed, open | resting, hover, pressed, focus_visible, disabled |

Each of the 6 groups (3 part/property combinations x 2 states) has the full set of 5 interaction values. No gaps within these groups.

### For consideration

1. **No `content` / `body` part tokens** — The accordion has `open` state tokens for the header and container, but no tokens for the expandable content area (e.g. `affirm.color.accordion.content.bg`, `affirm.spacing.accordion.content.padding_x`). If the content area uses inherited or global tokens this may be intentional, but worth confirming.

2. **No `divider` tokens** — If the accordion design includes visible dividers between accordion items, dedicated divider tokens (e.g. `affirm.color.accordion.divider.border`) may be needed.

3. **No `header.text` or `header.icon` size tokens beyond the single icon size** — There is `affirm.size.accordion.header.icon.all` for the icon, but no text size token (e.g. font-size, line-height). This is likely handled by typography tokens outside the component scope, but worth confirming.

---

## Summary

| Category | Count |
|----------|-------|
| Naming issues | 0 |
| Missing assignments | 0 |
| Logically missing (for consideration) | 3 |

The accordion token set is well-structured with complete naming and assignments. All interactive color token groups cover the full interaction set (resting, hover, pressed, focus_visible, disabled) across both `closed` and `open` states. The three items flagged for consideration relate to potential coverage of the content area, dividers, and text sizing — all of which may be intentionally handled outside the component token scope.
