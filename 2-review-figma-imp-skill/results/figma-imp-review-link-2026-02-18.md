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

**Variants reviewed:** 3 sizes (Large, Medium, Small) x 5 interactions (Resting, Hover, Pressed, Focus Visible, Disabled) = 15 variants.

**Nested instances:**
- `icon_new_window` — does NOT start with `.` or `_`; treated as **external component** (override-only review per additional rules).

---

## 1. Token Coverage

**7 of 32 tokens not applied.** 0 excluded by additional rules (no position tokens in this component's token set).

### Icon color — 1 not applied

| CSV Token | Figma Variable | Status |
|-----------|---------------|--------|
| affirm.color.link.icon.focus_visible | `color/link/icon/focus visible` | **Not applied** — missing from variable defs |

The remaining 4 icon color tokens (`resting`, `hover`, `pressed`, `disabled`) are correctly applied.

### Radius state tokens — 6 not applied

Hover, Pressed, and Disabled variants reuse `radius/link/container top/resting` and `radius/link/container bottom/resting` instead of their state-specific radius tokens.

| CSV Token | Figma Variable | Status |
|-----------|---------------|--------|
| affirm.radius.link.container.top.hover | `radius/link/container top/hover` | **Not applied** — uses `container top/resting` |
| affirm.radius.link.container.top.pressed | `radius/link/container top/pressed` | **Not applied** — uses `container top/resting` |
| affirm.radius.link.container.top.disabled | `radius/link/container top/disabled` | **Not applied** — uses `container top/resting` |
| affirm.radius.link.container.bottom.hover | `radius/link/container bottom/hover` | **Not applied** |
| affirm.radius.link.container.bottom.pressed | `radius/link/container bottom/pressed` | **Not applied** |
| affirm.radius.link.container.bottom.disabled | `radius/link/container bottom/disabled` | **Not applied** |

> **Note:** All radius tokens resolve to the same values (`size/100` = 8 for top, `size/000` = 0 for bottom), so visually there is no difference. However, each state should bind its own token for maintainability.

---

## 2. Raw Values and Direct Base Tokens

### Raw values — 1 issue

| Node / Layer | Property | Raw Value | Expected |
|-------------|----------|-----------|----------|
| `icon_new_window` (all 15 variants) | Width & Height | `24px` (hardcoded in design context code) | Variable defs confirm `size/link/{size}/icon/all` tokens ARE bound (values: Large=20, Medium=16, Small=14), yet the design context code renders `24px` on the icon wrapper across all size variants. The token binding may not be applied to the instance's width/height, or the wrapper has an additional fixed constraint. Verify in Figma that the icon instance dimensions are controlled by the size tokens. |

### Wrong tokens (non-link variables used in link component) — 2 issues

| Node / Layer | Property | Actual Variable | Expected Variable |
|-------------|----------|----------------|-------------------|
| Size=Medium, Interaction=Focus visible (`19056:6266`) | Horizontal padding (`paddingLeft` / `paddingRight`) | `size/checkbox/outline/offset/focus` | `spacing/link/outline_offset/focus visible` or a link-specific token |
| Size=Small, Interaction=Focus visible (`19056:6270`) | Border width (`strokeWeight`) | `size/checkbox/indicator/border/width/unselected/focus` | `size/link/outline_width/focus visible` |

> These are **checkbox** tokens incorrectly applied in the **link** component. While they resolve to the same value (`2px`), the link component should use its own tokens. The Large Focus Visible variant correctly uses `size/link/outline_width/focus visible` for border width and `spacing/link/outline_offset/focus visible` for padding — Medium and Small should match.

### Direct base tokens

None — no variables starting with `base/` were found in the component.

---

## 3. Typography

### Styles used

| Style Name | Sizes Applied |
|-----------|---------------|
| `typography/body/support/Large • Link` | Large variants |
| `typography/body/support/Medium • Link` | Medium variants |
| `typography/body/support/Small • Link` | Small variants |

All text nodes use defined library typography styles (not ad-hoc font/size/lineHeight).

### Typography set — 1 issue

Per additional rules, all typography must come from the `affirm.typography/component/` set. The styles follow the path `typography/body/support/*`, which does not begin with `affirm.typography/component/`.

| Style | Issue |
|-------|-------|
| `typography/body/support/Large • Link` | Not from `affirm.typography/component/` set |
| `typography/body/support/Medium • Link` | Not from `affirm.typography/component/` set |
| `typography/body/support/Small • Link` | Not from `affirm.typography/component/` set |

> **Note:** The Figma MCP may strip the library prefix from style names. If the full Figma path is actually `affirm.typography/component/body/support/...`, then these styles would be compliant. Verify the full style path in Figma to confirm.

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

None present. No issues.

---

## Summary

| Category | Issues |
|----------|--------|
| **1. Token coverage** | **7** tokens not applied (1 icon color focus visible, 6 radius state tokens) |
| **2. Raw values / wrong tokens** | **3** issues (1 icon wrapper size concern, 2 checkbox tokens used in link) |
| **3. Typography** | **1** issue (styles not from `affirm.typography/component/` set — needs verification) |
| **4. Component property naming** | **2** issues ("Focus visible" casing, "External Link" missing "Has" prefix) |
| **Total** | **13 issues** |

### Critical issues

- **Checkbox tokens in link component** (Check 2): Two Focus Visible variants (Medium, Small) use `size/checkbox/*` tokens instead of `size/link/*` / `spacing/link/*` tokens. The Large variant is correct — Medium and Small should be updated to match.
- **6 radius state tokens not bound** (Check 1): Hover, Pressed, and Disabled variants reuse the Resting radius token rather than their own state-specific tokens.
