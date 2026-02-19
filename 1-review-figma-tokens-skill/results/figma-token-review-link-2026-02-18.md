# Figma Token Review — Link

**Component:** link
**Date:** 2026-02-18

---

## Task 1: CSV vs Figma Comparison

### Missing in Figma

None — all 32 CSV tokens have a corresponding Figma variable (after accounting for the systematic naming convention differences between dot-notation in the CSV and slash-notation in Figma).

### Extra in Figma

None — all Figma variables in the `color/link/`, `radius/link/`, `size/link/`, and `spacing/link/` namespaces have a corresponding CSV token.

> **Note:** Semantic-level tokens `color/text/❌ link`, `color/text/❌ link • inverse`, `color/icon/link`, and `color/icon/link • inverse` exist in Figma but are not part of the link component token set — they belong to the semantic `color/text/` and `color/icon/` namespaces and are not expected in the component CSV.

### Naming Discrepancies

Two systematic naming convention differences exist between the CSV (source of truth) and Figma:

**1. Underscore vs space in state names**

The CSV uses `focus_visible` (underscore) while Figma uses `focus visible` (space). This affects 8 tokens:

| CSV Token | Figma Name |
|-----------|-----------|
| affirm.color.link.text.focus_visible | color/link/text/focus visible |
| affirm.color.link.container.bg.focus_visible | color/link/container_bg/focus visible |
| affirm.color.link.icon.focus_visible | color/link/icon/focus visible |
| affirm.color.link.outline.focus_visible | color/link/outline/focus visible |
| affirm.radius.link.container.top.focus_visible | radius/link/container top/focus visible |
| affirm.radius.link.container.bottom.focus_visible | radius/link/container bottom/focus visible |
| affirm.size.link.outline.width.focus_visible | size/link/outline_width/focus visible |
| affirm.spacing.link.outline.offset.focus_visible | spacing/link/outline_offset/focus visible |

**2. Segment merging (dot-separated segments in CSV → single segment in Figma)**

The CSV uses separate dot-separated segments for compound names, while Figma merges them into a single path segment (with underscore or space). This affects 22 tokens:

| CSV Pattern | Figma Pattern | Difference |
|-------------|---------------|------------|
| `container.bg` (5 color tokens) | `container_bg` | Dot → underscore merge |
| `container.top` (5 radius tokens) | `container top` | Dot → space merge |
| `container.bottom` (5 radius tokens) | `container bottom` | Dot → space merge |
| `outline.width` (1 size token) | `outline_width` | Dot → underscore merge |
| `outline.offset` (1 spacing token) | `outline_offset` | Dot → underscore merge |

### Assignment Discrepancies

**1 discrepancy found:**

| CSV Token | Mode | CSV Expected | Figma Actual |
|-----------|------|-------------|-------------|
| affirm.radius.link.container.top.focus_visible | All Modes | `size.100` | `base/size/125` |

The CSV specifies the alias target as `size.100` but the Figma variable `radius/link/container top/focus visible` (`VariableID:19026:5974`) resolves to `base/size/125`.

---

## Task 2: Scoping Rule Violations

**1 violation found:**

### radius/link/container top/pressed

- **Figma variable:** `radius/link/container top/pressed` (`VariableID:19026:5973`)
- **Rule applied:** `IF name startsWith "radius/"` → scopes must equal `["CORNER_RADIUS"]`
- **Expected scopes:** `["CORNER_RADIUS"]`
- **Actual scopes:** `["ALL_SCOPES"]`
- **Expected hiddenFromPublishing:** _(no rule)_
- **Actual hiddenFromPublishing:** `false` (all other radius/link tokens are `true`)

> **Note:** While no scoping rule explicitly governs `hiddenFromPublishing` for radius tokens, this is the only `radius/link/` variable with `hiddenFromPublishing: false` and `ALL_SCOPES` — it appears to be misconfigured compared to its siblings.

---

## Token Mapping

The full CSV-to-Figma mapping is in `results/figma-token-mapping-link-2026-02-18.csv`.
