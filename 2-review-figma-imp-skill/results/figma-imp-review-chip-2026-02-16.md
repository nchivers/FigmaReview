# Figma Implementation Review — Chip

**Date:** 2026-02-16

---

## Inputs Used

| Input | Value / Status |
|-------|---------------|
| Component name | chip |
| Component URL | `https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/UI8i9XPAQ1i7FMu0trkvKQ/...?node-id=3664-18079` |
| Data source | **Figma MCP** (`get_variable_defs`, `get_design_context`, `get_metadata`, `get_screenshot`) |
| Component tokens CSV | Present (`inputs/component-tokens.csv` — 54 tokens) |
| Figma variables JSON | Listed in inputs but not needed (MCP provided variable data directly) |
| Naming rules | Present (`knowledge/naming-rules.md`) |
| Additional rules | Present (`knowledge/additional-rules.md`) — position tokens excluded; subcomponent rules applied; `affirm.typography/component/` requirement applied |

### Subcomponent classification (per additional rules)

- **`container`**, **`focus-ring`**, text nodes — part of the reviewed component (full review applied)
- **`icon_disclosure_down`**, **`icon_happy`** — names do not start with `.` or `_`; treated as external component instances (overrides only)

---

## 1. Token Coverage

**CSV tokens checked:** 54
**Tokens matched in component:** 53
**Tokens not used:** 1

### Issues

| CSV Token | Figma Name | Figma Variable ID | Finding |
|-----------|------------|-------------------|---------|
| `affirm.spacing.chip.small.gap_x` | `spacing/chip/small/gap_x` | `VariableID:16716:1384` | **Not used.** All Small-size variants bind gap to `spacing/chip/large/gap_x` instead of `spacing/chip/small/gap_x`. This appears to be a binding error — the Small container's horizontal gap references the Large gap token. |

### Notes

- No position tokens exist in the CSV, so no exclusions were needed per the position-token additional rule.
- All other 53 tokens (color, spacing, radius, size) were confirmed present in the `get_variable_defs` response.
- The `base/size/*` variables (`base/size/100`, `base/size/125`, `base/size/150`, `base/size/175`, `base/size/225`) are used on the outer wrapper div for vertical padding. These are valid variables (not chip-specific tokens) and are not in the CSV; they are not flagged as missing.

---

## 2. Raw Values (No Hex / Non-Variable)

### Issues

None.

### Details

All reviewed properties use variable references:

- **Color** (fills, strokes, text color, focus outline): All use `var(--color/chip/...)` references.
- **Spacing** (padding, gap): All use `var(--spacing/chip/...)` references.
- **Border radius**: All use `var(--radius/chip/...)` references.
- **Border width**: Uses `var(--size/chip/border/width)`.
- **Focus outline width**: Uses `var(--size/chip/outline/width/focus_visible)`.
- **Focus outline color**: Uses `var(--color/chip/outline/focus_visible)`.

### Exempt / excluded items

- **Focus-ring `inset` values** (`-3px`): Raw positional value on the absolutely-positioned focus-ring layer. Exempt per additional rules — Figma cannot bind variables to position/constraint properties (x, y, inset). The computed offset (-3px) is consistent with `size/chip/border/width` (1px) + `spacing/chip/outline/offset/focus_visible` (2px).
- **Icon instance frame sizes** (`24px` on `icon_disclosure_down` and `icon_happy`): These are external component instances (names do not start with `.` or `_`); per additional rules, only overrides are evaluated, not the instance's own frame size.

### Observation

The `get_variable_defs` response includes a deprecated-looking variable: **`❌ Indigo/indigo50`** (`#4A4AF4`). This appears in the variable resolution chain for `color/chip/outline/focus_visible` and is not directly bound to any layer. The ❌ prefix suggests it may be a deprecated alias. The component itself correctly binds `color/chip/outline/focus_visible` — no raw hex is used. However, the presence of a ❌-prefixed variable in the alias chain may warrant cleanup at the variables level.

---

## 3. Typography

### Issues

None.

### Details

Three typography styles are used across all variants, all from the `affirm.typography/component/` set:

| Style | Used in Size | Properties |
|-------|-------------|------------|
| `typography/component/singleline/Small-MidImp` | Small | Calibre Medium, 14px / 18px line-height |
| `typography/component/singleline/Medium-MidImp` | Medium | Calibre Medium, 16px / 20px line-height |
| `typography/component/singleline/Large-MidImp` | Large | Calibre Medium, 18px / 24px line-height |

All text nodes reference these styles (confirmed via `get_variable_defs` styles output and `get_design_context` CSS variable usage for font family, size, weight, line-height, and letter-spacing). No ad-hoc or unbound typography was found.

---

## 4. Component Property Naming

**Variant properties found** (from metadata variant names):

| Property | Values | Type |
|----------|--------|------|
| State | Resting, Hover, Pressed, Focus-visible, Disabled | Variant |
| Size | Small, Medium, Large | Variant |
| Icon | None, Start | Variant |

**Other properties** (from design context code):

| Property | Type (inferred) |
|----------|----------------|
| text (default: "Chip text") | Text |
| iconSwap | Content swap (instance swap) |

### Issues

| Property / Value | Rule Violated | Expected | Actual |
|-----------------|---------------|----------|--------|
| **State** (property name) | "Use 'Interaction' instead of 'State' for variants that differ based on interaction." | **Interaction** | **State** |
| **Focus-visible** (value of State) | "Use Title Case … Use spaces, not slashes, pipes, or punctuation." | **Focus Visible** | **Focus-visible** (hyphen) |
| Property panel order | "Core Variants order: Size, Emphasis, State, Interaction." Size should precede Interaction. | **Size → Interaction → Icon** | **State → Size → Icon** |

### Notes

- **Size** — Named correctly as a noun; values (Small, Medium, Large) are Title Case and semantic.
- **Icon** — Named as a noun; values (None, Start) use Title Case. "Start" follows the directionally safe language guideline (Start/End instead of Left/Right). While this controls icon presence/position, the two non-boolean values (None vs Start) make a variant more appropriate than a boolean "Has Icon".
- **text** — Property name "text" is generic. The naming rules recommend role-based names (e.g. "Label", "Value"). For a chip, "Label" would be more descriptive of the text's purpose. This is a recommendation, not a hard rule violation, since "Text" alone is not in the explicit avoid list (Text 1, Top Text, String).
- **iconSwap** — Inferred as a content swap property from the design context (instance swap slot for the start icon). Per naming rules, content swap properties must start with "Swap" in the format "Swap + Slot Name" (e.g. **Swap Icon**). The code generator rendered this as `iconSwap`, suggesting the Figma property name may not follow the "Swap Icon" convention. If the Figma property is indeed named something other than "Swap Icon", this would be an issue.
- **Disabled** is correctly a value within the State/Interaction property (not a separate boolean), which aligns with the rule: "For interactive elements that can be disabled, 'Disabled' should be a value in the 'Interaction' property."

---

## Summary

| Category | Issues | Status |
|----------|--------|--------|
| 1. Token coverage | 1 | `spacing/chip/small/gap_x` not used — Small variants bind to `spacing/chip/large/gap_x` instead |
| 2. Raw values | 0 | All color, spacing, radius, stroke, and typography values use variable references |
| 3. Typography | 0 | All text uses `affirm.typography/component/singleline/*` library styles |
| 4. Property naming | 3 | "State" → should be "Interaction"; "Focus-visible" → should be "Focus Visible"; property order should be Size → Interaction → Icon |

**Total issues: 4**

### Recommendations (non-blocking)

- Rename text property from "Text" to "Label" for better semantic clarity.
- Confirm the content swap property follows "Swap Icon" naming convention.
- Investigate the `❌ Indigo/indigo50` variable in the alias chain — may need cleanup at the variables collection level.
