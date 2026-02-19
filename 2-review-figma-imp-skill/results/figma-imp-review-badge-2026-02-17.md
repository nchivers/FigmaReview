# Figma Implementation Review — Badge

**Date:** 2026-02-17

---

## Inputs Used

| Input | Value |
|-------|-------|
| componentName | badge |
| componentUrl | https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/41Br4IoI6VkD47pgGSaXdi/%F0%9F%8E%A8--R--DS-Core-Library?m=auto&node-id=13011-27348 |
| Data source | **Figma MCP** (get_variable_defs + get_design_context) |
| componentTokensCsv | inputs/component-tokens.csv (166 tokens) |
| figmaVariablesJson | Not provided |
| namingRules | knowledge/naming-rules.md |
| additionalRules | knowledge/additional-rules.md |

---

## 1. Token Coverage

**All 166 tokens from the CSV are applied.** No missing tokens.

Every token listed in `component-tokens.csv` appears as a variable in the component's `get_variable_defs` response. This includes:

- **144 color tokens** across 9 categories (Default, Brand Primary, Brand Featured, Brand Secondary, Brand Tertiary, Success, Error, Warning, Info) × 4 contexts (Default, Static, Inverse, Inverse Static) × 4 properties (bg, border, icon, text)
- **3 radius tokens** (small, medium, large)
- **4 size tokens** (border/width, small/icon/all, medium/icon/all, large/icon/all)
- **15 spacing tokens** (gap_x, padding_top, padding_bottom, padding_left, padding_right × 3 sizes)

No position tokens were present in the CSV, so no exclusions were needed per the position-token additional rule.

**Issues:** None

---

## 2. Raw Values and Direct Base Tokens

### Raw values

Spot-checked three representative variants via `get_design_context`:
- `13011:27405` — Category=Default, Context=Default, Size=Medium, Icon=None
- `18998:1689` — Category=Default, Context=Default, Size=Medium, Icon=Start
- `18998:1738` — Category=Brand Primary, Context=Default, Size=Large, Icon=None

All **badge-owned** properties use CSS variable references for:
- Background color (`--color/badge/*/bg`)
- Border color (`--color/badge/*/border`)
- Border width (`--size/badge/border/width`)
- Text color (`--color/badge/*/text`)
- Padding top/bottom/left/right (`--spacing/badge/*/padding_*`)
- Gap (`--spacing/badge/*/gap_x`)
- Border radius (`--radius/badge/*/all`)
- Font family, weight, size, line height, letter spacing (all via `--component/*` variables)

No raw hex, RGB, or numeric values were found on badge-owned layers.

### Direct base tokens

No variables with names starting with `base/` were found in the `get_variable_defs` response. All variables use component-level token paths (e.g. `color/badge/...`, `spacing/badge/...`).

### External component instances

The icon instance (`icon_happy`) does not start with `.` or `_` and is treated as an external component per additional rules. Its internal structure is not fully reviewed. The icon wrapper appears as a fixed `24px` container in the code output, though the `size/badge/medium/icon/all` token (value: 16) is confirmed as bound in `get_variable_defs`. This discrepancy may reflect how the MCP code generator represents nested instance sizing — **manual verification recommended** to confirm the icon size is properly variable-bound in Figma.

**Issues:** None confirmed. One item flagged for manual verification (icon instance sizing).

---

## 3. Typography

All typography uses **defined library styles** from the `affirm.typography/component/` set:

| Size variant | Typography style |
|-------------|-----------------|
| Small | `typography/component/singleline/Small-MidImp` |
| Medium | `typography/component/singleline/Medium-MidImp` |
| Large | `typography/component/singleline/Large-MidImp` |

Each style is composed from component-level typography variables:
- `component/fontFamily` → Calibre
- `component/weight/midImp` → Medium (500)
- `component/size/{Small,Medium,Large}` → 14, 16, 18
- `component/lineHeight/{Small,Medium,Large} • tight` → 18, 20, 24
- `component/letterSpacing/{Small,Medium,Large}` → 0

All typography styles begin with `typography/component/` (maps to `affirm.typography/component/`), satisfying the additional rules requirement.

**Issues:** None

---

## 4. Component Property Naming

### Variant properties

| Property | Values | Compliant? |
|----------|--------|-----------|
| **Category** | Default, Brand Primary, Brand Featured, Brand Secondary, Brand Tertiary, Success, Error, Warning, Info | Yes |
| **Context** | Default, Default Static, Inverse, Inverse Static | Yes |
| **Size** | Small, Medium, Large | Yes |
| **Icon** | None, Start, End | Yes |

All variant properties:
- Use **nouns** for property names ✓
- Use **Title Case** for names and values ✓
- Use **spaces** (not slashes/pipes) ✓
- Values are clear and semantic ✓
- "Start" / "End" used instead of "Left" / "Right" (directionally safe) ✓
- No emoji in names ✓
- No interaction states present (badge is non-interactive, so no Interaction/State property needed) ✓

### Text properties

The badge exposes a text property (rendered as `text` in MCP code output, default value "Badge text"). Per the naming rules, text properties should describe the **role** of the text. "Label" would be more descriptive than "Text" for a badge's content.

- **Property:** Text (inferred from code output)
- **Rule:** "Use the role of the text, not its position" / "Avoid generic names"
- **Expected:** "Label"
- **Severity:** Minor — "Text" is not on the explicitly prohibited list (Text 1, Top Text, String), but "Label" would better describe the badge text's role.

### Content swap properties

The Icon=Start and Icon=End variants expose a content swap for the icon (rendered as `iconSwap` in MCP code output). Per the naming rules, content swap properties must start with **"Swap"** (e.g. "Swap Icon").

- **Property:** Unknown exact Figma name (MCP code shows `iconSwap`)
- **Rule:** "Must start with 'Swap'" / "Format: Swap + Slot Name"
- **Expected:** "Swap Icon"
- **Note:** The exact Figma property name could not be confirmed from the MCP code output alone. If the property is named "Icon Swap" or similar (not starting with "Swap"), it would be a violation. **Manual verification recommended.**

### Boolean properties

No boolean properties were observed in the component. The Icon variant (None/Start/End) controls icon presence via variant values rather than a boolean, which is an acceptable pattern.

**Issues:** 1 minor (text property name), 1 requiring manual verification (content swap name)

---

## Summary

| Check | Issues |
|-------|--------|
| 1. Token coverage | **0** — All 166 tokens applied |
| 2. Raw values / base tokens | **0 confirmed** — 1 item flagged for manual verification (icon instance sizing) |
| 3. Typography | **0** — All styles from `affirm.typography/component/` set |
| 4. Component property naming | **1 minor** (text property name could be "Label"); 1 manual-verification item (content swap property name) |
| **Total** | **1 minor issue, 2 items for manual verification** |

### Overall assessment

The badge component has excellent token coverage and proper variable binding across all categories, contexts, and sizes. Typography correctly uses the `affirm.typography/component/` library styles. Variant property naming follows all rules. Two minor items require manual verification in Figma to confirm exact property names (text and content swap) and icon instance sizing.
