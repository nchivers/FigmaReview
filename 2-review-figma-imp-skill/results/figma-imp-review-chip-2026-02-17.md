# Figma Component Implementation Review — chip

**Date:** 2026-02-17
**Component:** chip
**Component URL:** https://www.figma.com/design/pypC8nTqembCVoO66eSHRn/branch/UI8i9XPAQ1i7FMu0trkvKQ/...?node-id=3664-18079

---

## Inputs Used

| Input | Status |
|-------|--------|
| componentName | `chip` |
| componentUrl | Provided |
| Component data source | **Figma MCP** (`get_variable_defs` + `get_design_context`) |
| componentTokensCsv | Provided (54 tokens) |
| figmaVariablesJson | Not provided (MCP used instead) |
| namingRules | Provided (`knowledge/naming-rules.md`) |
| additionalRules | Provided (`knowledge/additional-rules.md`) |

### Subcomponent classification

| Instance Name | Starts with `.` or `_` | Treatment |
|---------------|------------------------|-----------|
| `icon_disclosure_down` | No | Override-only (not a subcomponent) |
| `icon_happy` | No | Override-only (not a subcomponent) |

---

## 1. Token Coverage

**All 54 CSV tokens are used in the component.** No missing tokens.

Every token from `inputs/component-tokens.csv` was found in the `get_variable_defs` response. No position tokens needed to be excluded (none were present in the CSV).

### Naming note

- CSV maps `affirm.color.chip.indicator.focus_visible` to Figma name `color/chip/indicator/focus-visible` (hyphen), but `get_variable_defs` returns the key as `color/chip/indicator/focus_visible` (underscore). All other `focus_visible` tokens in the component use underscores consistently. The Figma variable name for this token may be inconsistent with the rest of the set.

### Additional tokens used but not in CSV

The following chip tokens appear in the component (`get_variable_defs`) but are **not listed in the CSV**:

| Variable name | Resolved value | Notes |
|--------------|---------------|-------|
| `spacing/chip/small/tap_target/padding_y` | 12 | Outer wrapper vertical padding (Small) |
| `spacing/chip/medium/tap_target/padding_y` | 10 | Outer wrapper vertical padding (Medium) |
| `spacing/chip/large/tap_target/padding_y` | 8 | Outer wrapper vertical padding (Large) |

These are `spacing/chip/` tokens and appear to be component-owned. Consider adding them to the token specification CSV.

---

## 2. Raw Values and Direct Base Tokens

### Base tokens used directly — 3 issues

All three issues are on the **focus-ring** element's `border-radius` property. Each size variant uses a `base/size/*` token directly instead of a component-level token.

| Node | Node ID | Property | Variable used | Resolved value | Issue |
|------|---------|----------|--------------|---------------|-------|
| focus-ring (Medium) | `19281:1672` | border-radius | `base/size/200` | 16px | Base token used directly |
| focus-ring (Large) | `19281:1673` | border-radius | `base/size/225` | 18px | Base token used directly |
| focus-ring (Small) | `19281:1671` | border-radius | `base/size/175` | 14px | Base token used directly |

**Recommendation:** Create component-level radius tokens for the focus ring (e.g. `radius/chip/small/focus_ring/all`, `radius/chip/medium/focus_ring/all`, `radius/chip/large/focus_ring/all`) that alias the appropriate base values, and apply those instead of using `base/size/*` directly.

### Non-standard color styles — 2 issues (likely from non-subcomponent icon instances)

| Style name | Value | Issue |
|-----------|-------|-------|
| `Indigo/indigo-50` | #4a4af4 | Non-standard color style; not a component or semantic variable |
| `❌ Indigo/indigo50` | #4A4AF4 | Deprecated color style (marked with ❌); not a component or semantic variable |

These appear in the `get_variable_defs` output and the design context styles list. They share the same hex value as `color/chip/outline/focus_visible` (#4a4af4). They may originate from nested non-subcomponent icon instances (`icon_disclosure_down`, `icon_happy`), in which case they are out of scope for full review per the subcomponent rule. However, if they are applied as overrides or directly on the chip component, they should be replaced with the appropriate component variable.

### Raw values — informational

| Node | Node ID | Property | Value | Notes |
|------|---------|----------|-------|-------|
| focus-ring (all sizes) | various | inset (position) | -3px | Hardcoded offset; `spacing/chip/outline/offset/focus_visible` (value: 2) exists as a token but Figma cannot bind variables to position properties — excluded per additional rules |

---

## 3. Typography

**No issues.** All text nodes use library typography styles from the `typography/component/` set.

| Typography style | Properties |
|-----------------|------------|
| `typography/component/singleline/Small-MidImp` | Calibre Medium, 14/18, weight 500 |
| `typography/component/singleline/Medium-MidImp` | Calibre Medium, 16/20, weight 500 |
| `typography/component/singleline/Large-MidImp` | Calibre Medium, 18/24, weight 500 |

All three styles begin with `typography/component/` which satisfies the requirement that typography must come from the `affirm.typography/component/` set (the `affirm.` prefix is not included in Figma MCP-returned style names, which is expected).

---

## 4. Component Property Naming

### Component properties found

| Property | Type | Values |
|----------|------|--------|
| Interaction | Variant | Resting, Hover, Pressed, Focus-visible, Disabled |
| Size | Variant | Small, Medium, Large |
| Icon | Variant | None, Start |
| Label | Text | (editable, default: "Chip text") |
| Swap Icon | Content Swap | (instance swap slot) |

### Issues — 1 found

| Property | Value | Rule violated | Expected |
|----------|-------|--------------|----------|
| Interaction | **Focus-visible** | Title Case: all property values must use Title Case | **Focus-Visible** (capital V) |

### Passing checks

- **Interaction** — Correct noun name; uses "Interaction" instead of "State" per specific rules. Values "Resting", "Hover", "Pressed", "Disabled" are all Title Case. "Disabled" is correctly a value of Interaction rather than a separate boolean.
- **Size** — Correct noun name. Values "Small", "Medium", "Large" are all Title Case.
- **Icon** — Correct noun name for a variant that combines presence and position (values "None", "Start"). Not a pure boolean, so "Has" prefix is not required.
- **Label** — Text property uses a role-based name (from the approved examples list).
- **Swap Icon** — Content swap property correctly uses "Swap + Slot Name" format.

---

## Summary

| Check | Issues |
|-------|--------|
| 1. Token coverage | **0** (all 54 CSV tokens covered) |
| 2. Raw values / base tokens | **5** (3 base tokens on focus-ring radius, 2 non-standard color styles) |
| 3. Typography | **0** |
| 4. Property naming | **1** (Title Case violation on "Focus-visible") |
| **Total** | **6 issues** |

### Critical issues

- **Base tokens on focus-ring border-radius** (3 issues): The focus-ring element uses `base/size/200`, `base/size/225`, and `base/size/175` directly for border-radius across the three size variants. Component-level tokens should be created and applied instead.

### Non-critical / informational

- 3 tap_target spacing tokens are used in the component but missing from the CSV.
- `color/chip/indicator/focus-visible` uses a hyphen while all other `focus_visible` tokens use underscores — naming inconsistency.
- 2 non-standard Indigo color styles likely originate from non-subcomponent icon instances.
- Focus-ring offset uses a hardcoded position value (expected — Figma limitation per additional rules).
