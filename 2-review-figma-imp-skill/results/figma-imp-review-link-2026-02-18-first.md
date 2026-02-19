# Figma Implementation Review — Link

**Component:** link
**Date:** 2026-02-18

---

## Inputs Used

| Input | Status |
|-------|--------|
| componentName | `link` |
| componentUrl | `https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/2qvJPV2B0c8o8TJqFAdVqv/...?node-id=3672-620` |
| Data source | **Figma MCP** (`get_variable_defs`, `get_design_context`, `get_metadata`) |
| componentTokensCsv | Present (`inputs/component-tokens.csv` — 32 tokens) |
| figmaVariablesJson | Present (not needed; MCP provided variable data) |
| namingRules | Present (`knowledge/naming-rules.md`) |
| additionalRules | Present (`knowledge/additional-rules.md`) |

**Variants reviewed:** 3 sizes (Large, Medium, Small) × 5 interactions (Resting, Hover, Pressed, Focus Visible, Disabled) = 15 variants.

---

## 1. Token Coverage

**14 of 32 tokens not applied** (0 excluded by additional rules — no position tokens in this component's token set).

### Icon color tokens — 5 not applied

The `icon_new_window` instance does not have `color/link/icon/*` tokens bound as fill overrides. The icon is rendered as an image (`<img>`), so no color variable is applied.

| CSV Token | Figma Variable | Status |
|-----------|---------------|--------|
| affirm.color.link.icon.resting | `color/link/icon/resting` | **Not applied** |
| affirm.color.link.icon.hover | `color/link/icon/hover` | **Not applied** |
| affirm.color.link.icon.pressed | `color/link/icon/pressed` | **Not applied** |
| affirm.color.link.icon.focus_visible | `color/link/icon/focus visible` | **Not applied** |
| affirm.color.link.icon.disabled | `color/link/icon/disabled` | **Not applied** |

### Radius state tokens — 6 not applied

Hover, Pressed, and Disabled variants reuse `radius/link/container top/resting` instead of their state-specific radius tokens. Bottom radius state tokens are also missing.

| CSV Token | Figma Variable | Status |
|-----------|---------------|--------|
| affirm.radius.link.container.top.hover | `radius/link/container top/hover` | **Not applied** — uses `container top/resting` |
| affirm.radius.link.container.top.pressed | `radius/link/container top/pressed` | **Not applied** — uses `container top/resting` |
| affirm.radius.link.container.top.disabled | `radius/link/container top/disabled` | **Not applied** — uses `container top/resting` |
| affirm.radius.link.container.bottom.hover | `radius/link/container bottom/hover` | **Not applied** |
| affirm.radius.link.container.bottom.pressed | `radius/link/container bottom/pressed` | **Not applied** |
| affirm.radius.link.container.bottom.disabled | `radius/link/container bottom/disabled` | **Not applied** |

### Icon size tokens — 3 not applied

All icon instances use a hardcoded `24px` size instead of the size-specific tokens.

| CSV Token | Figma Variable | Status |
|-----------|---------------|--------|
| affirm.size.link.large.icon.all | `size/link/large/icon/all` | **Not applied** — icon hardcoded to 24px |
| affirm.size.link.medium.icon.all | `size/link/medium/icon/all` | **Not applied** — icon hardcoded to 24px |
| affirm.size.link.small.icon.all | `size/link/small/icon/all` | **Not applied** — icon hardcoded to 24px |

> **Subcomponent note:** `icon_new_window` does not start with `.` or `_`, so it is treated as an external component instance. Only overrides are evaluated per additional rules. The missing tokens above are overrides that should be applied on the instance (fill color, size) but are not.

---

## 2. Raw Values and Direct Base Tokens

### Raw values — 1 issue

| Node / Layer | Property | Raw Value | Expected |
|-------------|----------|-----------|----------|
| `icon_new_window` (all 15 variants) | Width & Height | `24px` (hardcoded) | Should use `size/link/{size}/icon/all` variable per size variant |

### Wrong tokens (non-link variables used in link component) — 2 issues

| Node / Layer | Property | Actual Variable | Expected Variable |
|-------------|----------|----------------|-------------------|
| Size=Medium, Interaction=Focus visible (`19056:6266`) | Horizontal padding (`px`) | `size/checkbox/outline/offset/focus` | `spacing/link/outline_offset/focus visible` |
| Size=Small, Interaction=Focus visible (`19056:6270`) | Border width | `size/checkbox/indicator/border/width/unselected/focus` | `size/link/outline_width/focus visible` |

> These are **checkbox** tokens incorrectly applied in the **link** component. While they resolve to the same value (`2px`), the link component should use its own tokens for maintainability and correctness.

### Direct base tokens

None — no variables starting with `base/` were found in the component.

---

## 3. Typography

### Typography styles used

| Style Name | Sizes Applied |
|-----------|---------------|
| `typography/body/support/Large • Link` | Large variants |
| `typography/body/support/Medium • Link` | Medium variants |
| `typography/body/support/Small • Link` | Small variants |

All text nodes use defined library typography styles (not ad-hoc font/size/lineHeight). **However:**

### Typography set issue — 1 issue

Per additional rules, all typography must come from the `affirm.typography/component/` set. The styles used follow the pattern `typography/body/support/*` which does not begin with `affirm.typography/component/`.

| Style | Issue |
|-------|-------|
| `typography/body/support/Large • Link` | Not from `affirm.typography/component/` set |
| `typography/body/support/Medium • Link` | Not from `affirm.typography/component/` set |
| `typography/body/support/Small • Link` | Not from `affirm.typography/component/` set |

> **Note:** The Figma MCP may strip the library prefix from style names. If the full Figma path is `affirm.typography/component/body/support/...`, then these styles would actually be compliant. Verify the full style path in Figma to confirm.

---

## 4. Component Property Naming

### Variant properties

| Property | Values | Status |
|----------|--------|--------|
| Size | Large, Medium, Small | **No issues** — Title Case, noun name, clear semantic values |
| Interaction | Resting, Hover, Pressed, Focus visible, Disabled | **Issue** — see below |

**Issue:** The value `Focus visible` is not Title Case. Should be `Focus Visible` (capital "V").

### Boolean properties — 1 issue

| Property | Values | Issue |
|----------|--------|-------|
| External Link | true / false | Must start with **"Has"** — should be **"Has External Link"** |

### Text properties

| Property | Default Value | Status |
|----------|--------------|--------|
| Link Text | "Inline link text" | **No issues** — describes the role of the text |

### Content swap properties

None present.

---

## Summary

| Category | Issues |
|----------|--------|
| **1. Token coverage** | **14** tokens not applied (5 icon color, 6 radius state, 3 icon size) |
| **2. Raw values / wrong tokens** | **3** issues (1 hardcoded icon size, 2 checkbox tokens used in link) |
| **3. Typography** | **1** issue (styles not from `affirm.typography/component/` set — may need verification) |
| **4. Component property naming** | **2** issues ("Focus visible" casing, "External Link" missing "Has" prefix) |
| **Total** | **20 issues** |

### Critical issues

- **Checkbox tokens in link component** (Check 2): Two Focus Visible variants use `size/checkbox/*` tokens instead of `size/link/*` / `spacing/link/*` tokens. This creates an incorrect cross-component dependency.
- **14 tokens not applied** (Check 1): Nearly half of the component's token set is not bound in the Figma implementation, undermining token-driven theming.
