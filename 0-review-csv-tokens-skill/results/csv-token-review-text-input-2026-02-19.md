# CSV Token Review — text_input

**Date:** 2026-02-19

---

## Inputs used

| Input | Value / Path |
|-------|-------------|
| **componentName** | `text_input` |
| **CSV** | `inputs/component-tokens.csv` (14 segment columns, 3 assignment columns) |
| **Token naming rules** | `knowledge/token-naming-rules.md` |

---

## 1. Naming issues

### 1.1 Cursor tokens missing required Property segment

The four cursor tokens have an empty **Property** column. `cursor` is placed in Part-Variant, but no Property value follows. Per the naming rules, Property is a required (non-optional) segment, and `cursor` is not a valid Property value for the `color` foundation (valid values: `text`, `icon`, `fill`, `bg`, `border`, `outline`, `shadow`, `gradient_start`, `gradient_end`, `opacity`).

| Token (reconstructed) | Issue | Expected |
|------------------------|-------|----------|
| `affirm.color.input_text.input.cursor.empty.focus` | Property segment is empty | Add a property such as `fill` or `bg` (e.g., `affirm.color.input_text.input.cursor.fill.empty.focus`) |
| `affirm.color.input_text.input.cursor.filled.focus` | Property segment is empty | Same as above |
| `affirm.color.input_text.input.cursor.error_empty.focus` | Property segment is empty | Same as above |
| `affirm.color.input_text.input.cursor.error_filled.focus` | Property segment is empty | Same as above |

### 1.2 Outline offset token uses wrong Foundation

The outline **offset** token uses `size` as its Foundation, but per the naming rules `offset` is a **Spacing** property (not a Size property). The focus-visible pattern also specifies: `affirm.spacing.{component}[...].outline.offset[.{state}].focus_visible`.

| Token (reconstructed) | Issue | Expected |
|------------------------|-------|----------|
| `affirm.size.input_text.input.outline.offset` | Foundation is `size`; `offset` is a Spacing property | Change foundation to `spacing` → `affirm.spacing.input_text.input.outline.offset` |

**Total naming issues: 5 tokens**

---

## 2. Tokens missing assignments

All **color** tokens (dual-mode) have both **Light Mode** and **Dark Mode** values populated.

Both **size** tokens (single-mode) have **All Modes** values populated.

**None.**

---

## 3. Logically missing tokens

### 3.1 Error-state groups missing `disabled` interaction

Every non-error state group includes 6 interactions: `resting`, `hover`, `pressed`, `focus_visible`, `focus`, `disabled`. Every error-state group includes only 5 interactions — `disabled` is absent in all of them. If the component can be disabled while in an error state, these tokens should be added for parity.

| Suggested token | Part | Property | State | Missing interaction | Reason |
|-----------------|------|----------|-------|---------------------|--------|
| `affirm.color.input_text.input.bg.error_empty.disabled` | input | bg | error_empty | disabled | Non-error counterpart (`empty`) has disabled |
| `affirm.color.input_text.input.bg.error_filled.disabled` | input | bg | error_filled | disabled | Non-error counterpart (`filled`) has disabled |
| `affirm.color.input_text.input.border.error_empty.disabled` | input | border | error_empty | disabled | Non-error counterpart (`empty`) has disabled |
| `affirm.color.input_text.input.border.error_filled.disabled` | input | border | error_filled | disabled | Non-error counterpart (`filled`) has disabled |
| `affirm.color.input_text.input.icon.error_empty.disabled` | input | icon | error_empty | disabled | Non-error counterpart (`empty`) has disabled |
| `affirm.color.input_text.input.icon.error_filled.disabled` | input | icon | error_filled | disabled | Non-error counterpart (`filled`) has disabled |
| `affirm.color.input_text.input.label.text.error_empty.disabled` | input (subpart: label) | text | error_empty | disabled | Non-error counterpart (`empty`) has disabled |
| `affirm.color.input_text.input.label.text.error_filled.disabled` | input (subpart: label) | text | error_filled | disabled | Non-error counterpart (`filled`) has disabled |
| `affirm.color.input_text.input.value.text.error_filled.disabled` | input (subpart: value) | text | error_filled | disabled | Non-error counterpart (`filled`) has disabled |
| `affirm.color.input_text.error_message.text.disabled` | error_message | text | (none) | disabled | Non-error counterpart (`message`) has disabled |

**Total suggested tokens: 10** (for consideration, not hard failures)

---

## Summary

| Category | Count |
|----------|-------|
| **Naming issues** | 5 (4 cursor tokens missing property; 1 outline offset wrong foundation) |
| **Missing assignments** | 0 |
| **Logically missing tokens** | 10 suggested (all error-state groups missing `disabled` interaction) |
