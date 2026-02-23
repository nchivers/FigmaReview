# CSV Token Review — Accordion

## Inputs used

- **componentName:** accordion
- **CSV:** `inputs/component-tokens.csv` (14 segment columns + assignment columns)
- **Naming rules:** `knowledge/token-naming-rules.md`

---

## 1. Naming issues

None. All 40 tokens have valid segment values:

- **Namespace:** `affirm` — valid.
- **Foundation:** `color`, `size`, `spacing`, `radius` — all in the allowed set.
- **Component:** `accordion` — valid (no spaces, lowercase).
- **Variant / Size-Variant / Context / Polarity / Persistence:** all empty — valid (optional segments, not applicable).
- **Part:** `container`, `header`, `outline`, or empty — valid part names.
- **Part-Variant:** always empty — valid.
- **Subpart:** `icon` (on spacing/size tokens for the icon within header) or empty — valid.
- **Property values** align with their foundation:
  - Color: `bg`, `text`, `icon`, `outline` — all allowed.
  - Size: `width`, `all` — allowed.
  - Spacing: `margin_bottom`, `margin_top`, `offset`, `gap_x`, `padding_x`, `padding_y` — allowed.
  - Radius: `all` — allowed.
- **State:** `closed`, `open`, or empty — both are in the allowed state list.
- **Interaction:** `resting`, `hover`, `pressed`, `focus_visible`, `disabled`, or empty — all allowed.
- Focus-visible tokens follow the documented patterns: `color…outline.focus_visible`, `size…outline.width.focus_visible`, `spacing…outline.offset.focus_visible`.
- Transparent backgrounds use `opacity.000` as the base token, per the rule.

---

## 2. Tokens missing assignments

None. All assignments are present:

- **Dual-mode tokens (color):** All 31 color tokens have both Light Mode and Dark Mode values populated.
- **Single-mode tokens (size, spacing, radius):** All 9 tokens have an All Modes value populated.

---

## 3. Logically missing tokens

All existing token groups have complete interaction sets. The six color groups (container.bg, header.text, header.icon × closed/open) each have all five standard interactions: `resting`, `hover`, `pressed`, `focus_visible`, `disabled`.

The following are flagged **for consideration** based on the component's structure (open/closed accordion implies expandable content):

- **Content/body area tokens:** The accordion has `open` and `closed` states, implying a content area that expands. No tokens exist for a content/body/panel part (e.g., `color.accordion.content.bg`, `color.accordion.content.text`, `spacing.accordion.content.padding_x`, `spacing.accordion.content.padding_y`). If the content area requires component-level styling (background, text color, padding), consider adding tokens for it. If the content area inherits global tokens and needs no component-specific overrides, this can be disregarded.

- **Container border color:** The container has `bg` and `radius` tokens but no `border` color tokens. If the accordion design includes a visible border around the container (or between items), consider adding `affirm.color.accordion.container.border[.{state}][.{interaction}]` tokens. If the design is borderless, this can be disregarded.

- **Divider tokens:** Some accordion implementations include a visual divider between the header and body or between stacked accordion items. No divider tokens are present. Consider whether a divider element is needed (e.g., `affirm.color.accordion.divider.bg`, `affirm.size.accordion.divider.height`).

---

## Summary

| Category | Count |
|----------|-------|
| Naming issues | 0 |
| Missing assignments | 0 |
| Logically missing (for consideration) | 3 suggestions |

**Total tokens reviewed:** 40
