# CSV Component Token Review — Checkbox

**Date:** 2026-02-18

---

## Inputs used

| Input | Value / Path |
|-------|-------------|
| **componentName** | `checkbox` (from `inputs/inputs.json`) |
| **CSV** | `inputs/component-tokens.csv` — 97 token rows, 14 segment columns + 3 assignment columns |
| **Token naming rules** | `knowledge/token-naming-rules.md` |

---

## 1. Naming issues

**4 tokens** have a foundation–property mismatch.

| Token (reconstructed) | Segment | Issue | Expected |
|------------------------|---------|-------|----------|
| `affirm.size.checkbox.container.outline.offset.resting` | **foundation** | `offset` is not a valid property for the `size` foundation. Allowed size properties: `height`, `width`, `min_width`, `max_width`, `min_height`, `max_height`, `all`. | Foundation should be **`spacing`** (which includes `offset`). The focus-visible rules explicitly use `affirm.spacing.{component}[...].outline.offset[.{state}].focus_visible`. |
| `affirm.size.checkbox.container.outline.offset.hover` | **foundation** | Same as above. | **`spacing`** |
| `affirm.size.checkbox.container.outline.offset.pressed` | **foundation** | Same as above. | **`spacing`** |
| `affirm.size.checkbox.container.outline.offset.focus_visible` | **foundation** | Same as above. | **`spacing`** |

All other segment values (namespace, component, variant, part, subpart, property, state, interaction) conform to the naming rules across all 97 rows.

---

## 2. Tokens missing assignments

None. All dual-mode (color) tokens have both Light Mode and Dark Mode values, and all single-mode (size, spacing, radius) tokens have All Modes values.

---

## 3. Logically missing tokens

The following gaps were inferred by comparing interaction and state coverage across groups. These are **for consideration**, not hard failures.

### 3a. Error states missing `disabled` interaction

The `selected` and `unselected` states each have 5 interactions: `resting`, `hover`, `pressed`, `focus_visible`, `disabled`. The error composite states (`error_selected`, `error_unselected`) only have 4 — `disabled` is absent.

| Part | Property | State | Missing interaction | Reason |
|------|----------|-------|---------------------|--------|
| indicator | bg | error_selected | `disabled` | selected has disabled; error_selected does not |
| indicator | bg | error_unselected | `disabled` | unselected has disabled; error_unselected does not |
| indicator | border | error_selected | `disabled` | selected has disabled; error_selected does not |
| indicator | border | error_unselected | `disabled` | unselected has disabled; error_unselected does not |
| indicator | icon | error_selected | `disabled` | selected has disabled; error_selected does not |
| indicator | icon | error_unselected | `disabled` | unselected has disabled; error_unselected does not |

> **6 potentially missing color tokens.** If the design intentionally uses the non-error disabled tokens when in an error+disabled state, these may not be needed — but the pattern is inconsistent.

### 3b. Border-width (size) tokens missing error states

`indicator.border.width` has tokens for `selected` (5 interactions) and `unselected` (5 interactions) but none for `error_selected` or `error_unselected`. Since the color layer _does_ define visible borders for `error_unselected` (`red.850` / `red.300`), corresponding width tokens may be expected.

| Part | Subpart | Property | Missing states | Reason |
|------|---------|----------|----------------|--------|
| indicator | border | width | error_selected (resting, hover, pressed, focus_visible) | border color tokens exist for this state |
| indicator | border | width | error_unselected (resting, hover, pressed, focus_visible) | border color tokens exist with visible (non-transparent) values |

> **Up to 8 potentially missing size tokens.** If error-state border widths are the same as the non-error equivalents, these might be handled by fallback — but explicit tokens would match the color layer's coverage.

### 3c. Indeterminate state not represented

Checkbox commonly supports an `indeterminate` state (partial selection). The naming rules list `indeterminate` as a valid State value, but no tokens in the CSV use it. If the design includes an indeterminate appearance, tokens for `indicator.bg`, `indicator.border`, `indicator.icon`, and `label.text` with `indeterminate` state would be expected (mirroring the `selected`/`unselected` sets).

> **For consideration** — depends on whether the design system includes an indeterminate checkbox variant.

---

## Summary

| Category | Count |
|----------|-------|
| **Naming issues** | 4 (foundation–property mismatch on outline offset tokens) |
| **Missing assignments** | 0 |
| **Logically missing tokens (for consideration)** | 6 error-state disabled color tokens + up to 8 error-state border-width size tokens + indeterminate state set |
