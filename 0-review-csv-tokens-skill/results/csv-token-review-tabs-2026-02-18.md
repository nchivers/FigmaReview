# CSV Component Token Review — Tabs

## Inputs used

| Input | Value |
|-------|-------|
| **componentName** | `tabs` |
| **CSV** | `inputs/component-tokens.csv` (48 tokens, 14 segment columns) |
| **Naming rules** | `knowledge/token-naming-rules.md` |

---

## 1. Naming issues

| # | Token (reconstructed) | Segment | Issue | Expected |
|---|----------------------|---------|-------|----------|
| 1 | `affirm.size.tabs.border_bottom.width` (CSV row 41) | **subpart** (column 11) contains `border_bottom` | `border_bottom` is placed in the **subpart** column, but there is no parent **part**. Per the border naming pattern (`affirm.size.{component}[...].border[.{part-variant}][.{subpart}].width`), when a border element belongs directly to the component, it should occupy the **part** column (column 9). A subpart without a part is structurally incorrect. | Move `border_bottom` to the **part** column (column 9); leave subpart empty. |

**Total naming issues: 1**

---

## 2. Tokens missing assignments

None. All tokens have the required base-token assignments:

- **Color tokens (33 rows):** All have both Light Mode and Dark Mode values.
- **Radius tokens (6 rows):** All have an All Modes value.
- **Size tokens (4 rows):** All have an All Modes value.
- **Spacing tokens (5 rows):** All have an All Modes value.

**Total missing assignments: 0**

---

## 3. Logically missing tokens

The following are suggested additions **for consideration**, not hard failures.

### 3a. Icon tokens (if tabs support icons)

If tabs can display icons alongside text labels, the following token groups are expected based on the existing text-color pattern (selected/unselected x resting/hover/pressed/focus_visible/disabled):

| Suggested token | Foundation | Reason |
|----------------|------------|--------|
| `affirm.color.tabs.tab.icon.selected.{resting,hover,pressed,focus_visible,disabled}` | color | Icon color for selected tab, matching the text interaction set |
| `affirm.color.tabs.tab.icon.unselected.{resting,hover,pressed,focus_visible,disabled}` | color | Icon color for unselected tab, matching the text interaction set |
| `affirm.size.tabs.tab.icon.all` | size | Icon size (1:1 aspect ratio) |
| `affirm.spacing.tabs.tab.gap_x` | spacing | Horizontal gap between icon and label text within a tab |

**Count: up to 12 tokens (10 color + 1 size + 1 spacing), if icons are supported.**

### 3b. Border state consideration

| Existing token | Observation |
|---------------|-------------|
| `affirm.color.tabs.border` | This is the only color token with no state or interaction. If the entire tabs component can be disabled, consider whether the border color should change in that state (e.g. `affirm.color.tabs.border.disabled`). If the border is intentionally static across all states, no change is needed. |

**Count: up to 1 token, if a disabled border color is needed.**

---

## Summary

| Category | Count |
|----------|-------|
| **Naming issues** | 1 |
| **Missing assignments** | 0 |
| **Logically missing (for consideration)** | Up to 13 tokens (12 icon-related + 1 border state) |
