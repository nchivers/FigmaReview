# Component Implementation Review — Merchant Tile

**Date:** 2026-02-16

---

## Inputs Used

| Input | Status |
|-------|--------|
| **componentUrl** | `https://www.figma.com/design/yvoTWRBHHMvvVdTphS2UpN/branch/RcZDLMyyyW75BOu0qaoRv3/…?node-id=5-3602` |
| **Component data source** | Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| **componentTokensCsv** | Present — 37 tokens |
| **figmaVariablesJson** | Not present (file does not exist) |
| **namingRules** | Present (`knowledge/naming-rules.md`) |
| **additionalRules** | Present (`knowledge/additional-rules.md`) — position-token exclusion and subcomponent rules applied |
| **componentExportJson** | Not present (not needed — Figma MCP used) |

**Component structure:** Component set "🎨 [r] Merchant Tile" with four variants — `State=resting`, `State=hover`, `State=focus visible`, `State=pressed`. Each variant contains a merchant image area with a logo overlay, an optional badge, a merchant name, and optional terms text with icon.

**Subcomponent classification (per additional rules):**
- Layers starting with `.` → subcomponents (full review). None found.
- Instance "Merchant Logos" → does NOT start with `.` → override-only evaluation.
- Instance "🎨 [R] Badge" → does NOT start with `.` → override-only evaluation.
- Instance "Color=grayscale" (icon) → does NOT start with `.` → override-only evaluation.

---

## 1. Token Coverage

**CSV tokens:** 37 | **Matched:** 29 | **Position tokens excluded:** 4 | **Not applied (issues):** 4

### Issues — tokens from CSV not found in component variables

| CSV Token | Figma Variable | Variable ID |
|-----------|---------------|-------------|
| `affirm.color.merchant_tile.container.border.resting` | `color/merchant_tile/container/border/resting` | `VariableID:7130:101` |
| `affirm.color.merchant_tile.container.border.hover` | `color/merchant_tile/container/border/hover` | `VariableID:7130:102` |
| `affirm.color.merchant_tile.container.border.pressed` | `color/merchant_tile/container/border/pressed` | `VariableID:7130:103` |
| `affirm.color.merchant_tile.container.border.focus_visible` | `color/merchant_tile/container/border/focus_visible` | `VariableID:7130:104` |

> The component uses `size/merchant_tile/border/width/resting` (value `0`) for border width but does not bind the four border **color** tokens. The focus-visible state uses an **outline** token (`color/merchant_tile/container/outline/focus_visible`) rather than a border. These border-color tokens should still be applied to ensure the design responds correctly if border width changes.

### Position tokens excluded (per additional rules)

The following 4 position tokens are excluded from the unused-token count because Figma does not allow binding variables to x/y position properties:

- `position/merchant_tile/badge/left` (`VariableID:7721:987`)
- `position/merchant_tile/badge/top` (`VariableID:7721:988`)
- `position/merchant_tile/merchant_img/merchant_logo/bottom` (`VariableID:7721:986`)
- `position/merchant_tile/merchant_img/merchant_logo/left` (`VariableID:7721:985`)

### Extra variable in component (not in CSV)

- `size/merchant_tile/border/width/resting` (value `0`) — bound in the component but not listed in the CSV.

---

## 2. Raw Values (No Hex / Non-Variable)

Checked: color, spacing, border radius, stroke color, stroke width.

### In-scope layers (main component frames)

**No issues.** All checked properties on in-scope layers use variable references:

- Container backgrounds (`color/merchant_tile/container/bg/*`) — variable-bound across all 4 states
- Border radii (`radius/merchant_tile/container/all`, `radius/merchant_tile/merchant_img/all`) — variable-bound
- Spacing / padding / gap (`spacing/merchant_tile/merchant_info/*`, `spacing/merchant_tile/term_text/gap_x`) — variable-bound
- Text colors (`color/merchant_tile/merchant_info/name/text/*`, `color/merchant_tile/term_text/text/*`, `color/merchant_tile/term_text/icon/*`) — variable-bound
- Focus-visible outline (`color/merchant_tile/container/outline/focus_visible`, `size/merchant_tile/container/outline/width/focus_visible`, `spacing/merchant_tile/container/outline/offset/focus_visible`) — variable-bound

### Non-subcomponent instances (override-only evaluation per additional rules)

| Instance | Property | Value | Assessment |
|----------|----------|-------|------------|
| **Merchant Logos** | border color | `#edf1f5` | `#edf1f5` does not appear in `get_variable_defs`. If this is an override applied by the Merchant Tile (not the instance default), it should use a variable. **Requires manual verification.** |
| **Merchant Logos** | background | `white` | `Primary/White` style appears in `get_variable_defs` — likely using the library style. No issue. |
| **Merchant Logos** | border radius | `999px` | Likely the component's own pill-radius default, not an override. No issue. |
| **Merchant Logos** | size | `80px` | `size/merchant_tile/merchant_img/merchant_logo/all` exists with value `40` — the 40px may apply to the inner logo, while 80px is the container. May need verification. |
| **🎨 [R] Badge** | — | — | All overrides (bg, padding, radius, typography) use variables/styles. No issues. |
| **Color=grayscale** (icon) | — | — | No override issues detected. |

> Position values on Merchant Logos (`bottom: 8px`, `left: 8px`) and Badge (`left: 8px`, `top: 8px`) are raw, but position properties cannot be variable-bound in Figma per additional rules.

---

## 3. Typography

**No issues.** All text uses defined library typography styles:

| Text Element | Typography Style | Properties |
|-------------|-----------------|------------|
| Badge text | `affirm.typography/component/singleline/Small-MidImp` | Calibre Medium 14/18, letterSpacing 0 |
| Merchant name | `affirm.typography/component/singleline/Large-HighImp` | Calibre Semibold 18/24, letterSpacing 0 |
| Terms text | `typography/body-Medium` | Calibre Regular 16/24, letterSpacing 0 |

All three are library-defined composite styles with variable-backed individual properties (fontFamily, weight, size, lineHeight, letterSpacing).

---

## 4. Component Property Naming

Rules applied from `knowledge/naming-rules.md`.

### Component properties detected

| Property | Type | Values |
|----------|------|--------|
| State | Variant | resting, hover, focus visible, pressed |
| Has Badge | Boolean | true, false |
| Has Terms Text | Boolean | true, false |
| Merchant Name | Text | (editable, default "StubHub") |

### Issues

| Property | Actual | Rule Violated | Expected |
|----------|--------|---------------|----------|
| **State** (name) | `State` | "Use 'Interaction' instead of 'State' for variants that differ based on interaction." | `Interaction` |
| **State** (values) | `resting`, `hover`, `focus visible`, `pressed` | "Use Title Case for all property names and values." | `Resting`, `Hover`, `Focus Visible`, `Pressed` |

### Passed

- **Has Badge** — "Has + Noun" format. Title Case. Boolean values true/false. ✓
- **Has Terms Text** — "Has + Noun" format. Title Case. Boolean values true/false. ✓
- **Merchant Name** — Role-based text property name. Title Case. Not generic. ✓
- No emojis in property names or values. ✓

---

## Summary

| Category | Issues | Details |
|----------|--------|---------|
| **1. Token coverage** | **4** | 4 container border color tokens not applied (resting, hover, pressed, focus-visible). 4 position tokens excluded per additional rules. |
| **2. Raw values** | **0 confirmed** | No raw values on in-scope layers. 1 potential issue on Merchant Logos instance (`border #edf1f5`) requires manual verification. |
| **3. Typography** | **0** | All text uses library typography styles. |
| **4. Property naming** | **2** | Variant property "State" should be "Interaction"; variant values should use Title Case. |

**Total: 6 confirmed issues + 1 requiring manual verification.**

The most impactful findings are the 4 missing border-color token bindings and the 2 naming violations. Typography is fully compliant. The Merchant Logos border color (`#edf1f5`) should be manually checked to determine whether it is an override or a component default.
