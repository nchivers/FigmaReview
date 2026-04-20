# Additional Rules

## Shadow composite tokens → Figma styles, not variables

Shadow composite tokens in the CSV represent Figma **styles**, not variables. They must be **excluded entirely** from all tasks (matching, updates, renames, deletes, and additions).

### How to identify them

A CSV token is a shadow composite when its normalized name starts with `shadow/` and contains the segment `composite`. These tokens typically have:
- No mode values (All Modes, Light Mode, Dark Mode are all empty)
- An optional annotation of "Composite style" in the CSV

**Examples:**
- `affirm.shadow.button.primary.composite.resting`
- `affirm.shadow.button.secondary.composite.hover`
- `affirm.shadow.button.tertiary.composite.disabled`

### Why they are excluded

Shadows in Figma are applied as **effect styles**, which are a separate system from variables. The component-tokens CSV lists them for completeness, but they cannot be represented as Figma variables and must not appear in the plan.

### Rule

Before running any tasks, filter out all CSV tokens whose normalized name matches the pattern `shadow/{component}/**/composite/**`. These tokens must not participate in Task 1 (exact matches), Task 2 (potential matches), Task 3 (deletes), or Task 4 (additions), and must not appear in the plan output at all.

---

## Opacity base value lookup

CSV token values that reference opacity use short-form notation like `opacity.00`, `opacity.100`, etc. These are part of the color foundation in Figma and live under the `base/color/opacity/` path in `tools/knowledge/figma-base-variables.csv`.

### How to resolve them

When a CSV token value matches the pattern `opacity.##` (e.g. `opacity.00`, `opacity.50`, `opacity.100`):

1. Normalize the value by replacing `.` with `/` → `opacity/00`
2. Prepend `base/color/` → `base/color/opacity/00`
3. Look up `base/color/opacity/00` in `tools/knowledge/figma-base-variables.csv` to get the variable ID

**Examples:**

| CSV value | Normalized | Lookup key | Variable ID |
|-----------|-----------|------------|-------------|
| `opacity.00` | `opacity/00` | `base/color/opacity/00` | `VariableID:4360:1126063` |
| `opacity.100` | `opacity/100` | `base/color/opacity/100` | `VariableID:4360:1126073` |
| `opacity.transparent` | `opacity/transparent` | `base/color/opacity/transparent` | `VariableID:4360:1126062` |

### Why this is needed

The standard base token value lookup rule (normalize `.` → `/` and look up directly) does not find these values because the CSV omits the `base.color.` prefix. This rule ensures opacity references resolve correctly instead of being marked as "no alias found".
