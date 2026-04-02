# Token Update Plan — top nav bar

**Generated:** 2026-04-02 12:58
**Source of truth:** inputs/component-tokens.csv
**Figma variables file:** inputs/figma-variables.json

---

## Summary

| Action | Count |
|--------|-------|
| Value updates (normalized exact match) | 1 |
| Renames + updates (potential match) | 12 |
| Deletes | 29 |
| Additions | 21 |
| In sync (no changes needed) | 2 |

---

## Task 1 — Normalized exact matches (value updates only)

| CSV name | Figma name | Figma ID | Mode | Current value | Required value | Required value ID |
|----------|------------|----------|------|---------------|----------------|-------------------|
| affirm.color.top_nav_bar.notification_indicator.fill | color/top_nav_bar/notification_indicator/fill | VariableID:7328:2724 | Light Mode | base/g-color/red/550 | base/color/red/500 | VariableID:4360:1126027 |
| affirm.color.top_nav_bar.notification_indicator.fill | color/top_nav_bar/notification_indicator/fill | VariableID:7328:2724 | Dark Mode | base/g-color/red/500 | base/color/red/500 | VariableID:4360:1126027 |

---

## Task 2 — Potential matches (rename and/or value update)

**CSV token:** `affirm.color.top_nav_bar.main.container.bg`
**Figma variable:** `color/top_nav_bar/tier_1/bg` (`VariableID:7328:2715`)
**Confidence:** High — tier_1 → main variant rename; `container` segment added; same structural role (primary variant background)
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_1/bg` → `color/top_nav_bar/main/container/bg`
- UPDATE Light Mode: `base/g-color/gray/050` → `base/color/gray/white` (`VariableID:4360:1125971`)
- UPDATE Dark Mode: `base/g-color/gray/920` → `base/color/gray/950` (`VariableID:4360:1126019`)

---

**CSV token:** `affirm.color.top_nav_bar.main.inverse.static.container.bg`
**Figma variable:** `color/top_nav_bar/tier_1/inverse/static/bg` (`VariableID:7328:2717`)
**Confidence:** High — tier_1 → main; `container` segment added; inverse/static modifier preserved
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_1/inverse/static/bg` → `color/top_nav_bar/main/inverse/static/container/bg`
- UPDATE Light Mode: `base/g-color/opacity/000` → `base/color/gray/950` (`VariableID:4360:1126019`)
- UPDATE Dark Mode: `base/g-color/opacity/000` → `base/color/gray/950` (`VariableID:4360:1126019`)

---

**CSV token:** `affirm.color.top_nav_bar.main.page_title.text`
**Figma variable:** `color/top_nav_bar/tier_1/page_title/text` (`VariableID:7328:2721`)
**Confidence:** High — tier_1 → main; page_title/text path preserved
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_1/page_title/text` → `color/top_nav_bar/main/page_title/text`
- UPDATE Light Mode: `base/g-color/gray/970` → `base/color/gray/950` (`VariableID:4360:1126019`)
- UPDATE Dark Mode: `base/g-color/gray/030` → `base/color/gray/white` (`VariableID:4360:1125971`)

---

**CSV token:** `affirm.color.top_nav_bar.main.inverse.static.page_title.text`
**Figma variable:** `color/top_nav_bar/tier_1/inverse/static/page_title/text` (`VariableID:7328:2723`)
**Confidence:** High — tier_1 → main; inverse/static and page_title/text paths preserved
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_1/inverse/static/page_title/text` → `color/top_nav_bar/main/inverse/static/page_title/text`
- UPDATE Light Mode: `base/g-color/gray/030` → `base/color/gray/white` (`VariableID:4360:1125971`)
- UPDATE Dark Mode: `base/g-color/gray/030` → `base/color/gray/white` (`VariableID:4360:1125971`)

---

**CSV token:** `affirm.color.top_nav_bar.secondary.container.bg`
**Figma variable:** `color/top_nav_bar/tier_2/bg` (`VariableID:7328:2731`)
**Confidence:** Medium — tier_2 → secondary variant rename; `container` segment added; assumes tier_2 maps to secondary (both represent the "second" variant)
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_2/bg` → `color/top_nav_bar/secondary/container/bg`
- UPDATE Light Mode: `base/g-color/gray/050` → `base/color/gray/white` (`VariableID:4360:1125971`)
- UPDATE Dark Mode: `base/g-color/gray/920` → `base/color/gray/950` (`VariableID:4360:1126019`)

---

**CSV token:** `affirm.color.top_nav_bar.secondary.inverse.static.container.bg`
**Figma variable:** `color/top_nav_bar/tier_2/inverse/static/bg` (`VariableID:7328:2733`)
**Confidence:** Medium — tier_2 → secondary; `container` segment added; inverse/static preserved
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_2/inverse/static/bg` → `color/top_nav_bar/secondary/inverse/static/container/bg`
- UPDATE Light Mode: `base/g-color/opacity/000` → `base/color/gray/950` (`VariableID:4360:1126019`)
- UPDATE Dark Mode: `base/g-color/opacity/000` → `base/color/gray/950` (`VariableID:4360:1126019`)

---

**CSV token:** `affirm.color.top_nav_bar.secondary.page_title.text`
**Figma variable:** `color/top_nav_bar/tier_2/page_title/text` (`VariableID:7328:2734`)
**Confidence:** Medium — tier_2 → secondary; page_title/text preserved
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_2/page_title/text` → `color/top_nav_bar/secondary/page_title/text`
- UPDATE Light Mode: `base/g-color/gray/970` → `base/color/gray/950` (`VariableID:4360:1126019`)
- UPDATE Dark Mode: `base/g-color/gray/030` → `base/color/gray/white` (`VariableID:4360:1125971`)

---

**CSV token:** `affirm.color.top_nav_bar.secondary.inverse.static.page_title.text`
**Figma variable:** `color/top_nav_bar/tier_2/inverse/static/page_title/text` (`VariableID:7328:2736`)
**Confidence:** Medium — tier_2 → secondary; inverse/static and page_title/text preserved
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_2/inverse/static/page_title/text` → `color/top_nav_bar/secondary/inverse/static/page_title/text`
- UPDATE Light Mode: `base/g-color/gray/030` → `base/color/gray/white` (`VariableID:4360:1125971`)
- UPDATE Dark Mode: `base/g-color/gray/030` → `base/color/gray/white` (`VariableID:4360:1125971`)

---

**CSV token:** `affirm.color.top_nav_bar.notification_indicator.border`
**Figma variable:** `color/top_nav_bar/tier_1/notification_indicator/border` (`VariableID:7328:2727`)
**Confidence:** Medium — notification_indicator/border tokens are becoming variant-independent (removing tier_1); tier_1 version chosen as source since it's the "primary"
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_1/notification_indicator/border` → `color/top_nav_bar/notification_indicator/border`
- UPDATE Light Mode: `base/g-color/gray/050` → `base/color/gray/white` (`VariableID:4360:1125971`)
- UPDATE Dark Mode: `base/g-color/gray/920` → `base/color/gray/950` (`VariableID:4360:1126019`)

---

**CSV token:** `affirm.color.top_nav_bar.inverse.static.notification_indicator.border`
**Figma variable:** `color/top_nav_bar/tier_1/inverse/static/notification_indicator/border` (`VariableID:7328:2730`)
**Confidence:** Medium — removing tier_1 prefix; inverse/static modifier preserved; notification tokens consolidated to variant-independent
**Planned actions:**
- RENAME: `color/top_nav_bar/tier_1/inverse/static/notification_indicator/border` → `color/top_nav_bar/inverse/static/notification_indicator/border`
- UPDATE Light Mode: `base/g-color/opacity/000` → `base/color/gray/950` (`VariableID:4360:1126019`)
- UPDATE Dark Mode: `base/g-color/opacity/000` → `base/color/gray/950` (`VariableID:4360:1126019`)

---

**CSV token:** `affirm.size.top_nav_bar.main.affirm_logo.width`
**Figma variable:** `size/top_nav_bar/affirm_logo/width` (`VariableID:7328:2749`)
**Confidence:** Medium — `main` variant segment being added; CSV splits this into main/secondary variants while Figma has a single shared token
**Planned actions:**
- RENAME: `size/top_nav_bar/affirm_logo/width` → `size/top_nav_bar/main/affirm_logo/width`
- No value update needed — All Modes: `base/size/900` matches required `size.900` (`VariableID:4253:912`)

---

**CSV token:** `affirm.size.top_nav_bar.notification_indicator.border.width`
**Figma variable:** `size/top_nav_bar/tier_1/notification_indicator/border/width` (`VariableID:7328:2740`)
**Confidence:** Medium — removing tier_1; notification_indicator/border/width path preserved; consolidating tier-specific variants into single token
**Planned actions:**
- RENAME: `size/top_nav_bar/tier_1/notification_indicator/border/width` → `size/top_nav_bar/notification_indicator/border/width`
- No value update needed — All Modes: `base/size/013` matches required `size.013` (`VariableID:57:2007`)

---

## Task 3 — Deletes

| Figma variable name | Figma ID | Action |
|---------------------|----------|--------|
| spacing/top_nav_bar/tier_1/container/padding_right | VariableID:2199:3114 | DELETE |
| spacing/top_nav_bar/tier_1/container/padding_left | VariableID:2199:3115 | DELETE |
| spacing/top_nav_bar/tier_1/container/padding_top | VariableID:7328:2700 | DELETE |
| spacing/top_nav_bar/tier_1/container/padding_bottom | VariableID:7328:2701 | DELETE |
| spacing/top_nav_bar/tier_1/right_buttons/button_group/gap_x | VariableID:7328:2702 | DELETE |
| spacing/top_nav_bar/tier_1/right_buttons/button_group/padding_right | VariableID:7328:2703 | DELETE |
| spacing/top_nav_bar/tier_1/right_buttons/single_button/padding_right | VariableID:7328:2705 | DELETE |
| spacing/top_nav_bar/tier_1/right_buttons/single_button/gap_x | VariableID:7328:2706 | DELETE |
| spacing/top_nav_bar/tier_2/container/padding_left | VariableID:7328:2707 | DELETE |
| spacing/top_nav_bar/tier_2/container/padding_right | VariableID:7328:2708 | DELETE |
| spacing/top_nav_bar/tier_2/container/padding_top | VariableID:7328:2709 | DELETE |
| spacing/top_nav_bar/tier_2/container/padding_bottom | VariableID:7328:2710 | DELETE |
| spacing/top_nav_bar/tier_2/right_buttons/single_button/padding_right | VariableID:7328:2711 | DELETE |
| spacing/top_nav_bar/tier_2/right_buttons/single_button/gap_x | VariableID:7328:2712 | DELETE |
| spacing/top_nav_bar/tier_2/right_buttons/button_group/gap_x | VariableID:7328:2713 | DELETE |
| spacing/top_nav_bar/tier_2/right_buttons/button_group/padding_right | VariableID:7328:2714 | DELETE |
| color/top_nav_bar/tier_1/secondary/bg | VariableID:7328:2716 | DELETE |
| color/top_nav_bar/tier_1/secondary/page_title/text | VariableID:7328:2722 | DELETE |
| color/top_nav_bar/tier_1/secondary/notification_indicator/border | VariableID:7328:2728 | DELETE |
| color/top_nav_bar/tier_2/secondary/bg | VariableID:7328:2732 | DELETE |
| color/top_nav_bar/tier_2/secondary/page_title/text | VariableID:7328:2735 | DELETE |
| color/top_nav_bar/tier_2/secondary/notification_indicator/border | VariableID:7328:2738 | DELETE |
| color/top_nav_bar/tier_2/notification_indicator/border | VariableID:7328:2737 | DELETE |
| color/top_nav_bar/tier_2/inverse/static/notification_indicator/border | VariableID:7328:2739 | DELETE |
| size/top_nav_bar/tier_1/secondary/notification_indicator/border/width | VariableID:7328:2742 | DELETE |
| size/top_nav_bar/tier_1/inverse/static/notification_indicator/border/width | VariableID:7328:2743 | DELETE |
| size/top_nav_bar/tier_2/secondary/notification_indicator/border/width | VariableID:7328:2744 | DELETE |
| size/top_nav_bar/tier_2/inverse/static/notification_indicator/border/width | VariableID:7328:2745 | DELETE |
| size/top_nav_bar/tier_2/notification_indicator/border/width | VariableID:7328:2746 | DELETE |

---

## Task 4 — Additions

| CSV token name | All Modes | All Modes ID | Light Mode | Light Mode ID | Dark Mode | Dark Mode ID | Action |
|----------------|-----------|--------------|------------|---------------|-----------|--------------|--------|
| affirm.color.top_nav_bar.main.static.container.bg | | | base.color.gray.white | VariableID:4360:1125971 | base.color.gray.white | VariableID:4360:1125971 | ADD |
| affirm.color.top_nav_bar.main.inverse.container.bg | | | base.color.gray.950 | VariableID:4360:1126019 | base.color.gray.white | VariableID:4360:1125971 | ADD |
| affirm.color.top_nav_bar.main.static.page_title.text | | | base.color.gray.950 | VariableID:4360:1126019 | base.color.gray.950 | VariableID:4360:1126019 | ADD |
| affirm.color.top_nav_bar.main.inverse.page_title.text | | | base.color.gray.white | VariableID:4360:1125971 | base.color.gray.950 | VariableID:4360:1126019 | ADD |
| affirm.color.top_nav_bar.secondary.static.container.bg | | | base.color.gray.white | VariableID:4360:1125971 | base.color.gray.white | VariableID:4360:1125971 | ADD |
| affirm.color.top_nav_bar.secondary.inverse.container.bg | | | base.color.gray.950 | VariableID:4360:1126019 | base.color.gray.white | VariableID:4360:1125971 | ADD |
| affirm.color.top_nav_bar.secondary.static.page_title.text | | | base.color.gray.950 | VariableID:4360:1126019 | base.color.gray.950 | VariableID:4360:1126019 | ADD |
| affirm.color.top_nav_bar.secondary.inverse.page_title.text | | | base.color.gray.white | VariableID:4360:1125971 | base.color.gray.950 | VariableID:4360:1126019 | ADD |
| affirm.color.top_nav_bar.static.notification_indicator.border | | | base.color.gray.white | VariableID:4360:1125971 | base.color.gray.white | VariableID:4360:1125971 | ADD |
| affirm.color.top_nav_bar.inverse.notification_indicator.border | | | base.color.gray.950 | VariableID:4360:1126019 | base.color.gray.white | VariableID:4360:1125971 | ADD |
| affirm.color.top_nav_bar.static.notification_indicator.fill | | | base.color.red.500 | VariableID:4360:1126027 | base.color.red.500 | VariableID:4360:1126027 | ADD |
| affirm.color.top_nav_bar.inverse.notification_indicator.fill | | | base.color.red.500 | VariableID:4360:1126027 | base.color.red.500 | VariableID:4360:1126027 | ADD |
| affirm.color.top_nav_bar.inverse.static.notification_indicator.fill | | | base.color.red.500 | VariableID:4360:1126027 | base.color.red.500 | VariableID:4360:1126027 | ADD |
| affirm.position.top_nav_bar.notification_indicator.right | size.125 | VariableID:16:1944 | | | | | ADD |
| affirm.position.top_nav_bar.notification_indicator.top | size.125 | VariableID:16:1944 | | | | | ADD |
| affirm.size.top_nav_bar.secondary.affirm_logo.width | size.900 | VariableID:4253:912 | | | | | ADD |
| affirm.size.top_nav_bar.container.min_height | size.700 | VariableID:14:1954 | | | | | ADD |
| affirm.spacing.top_nav_bar.main.container.padding_x | size.200 | VariableID:14:1946 | | | | | ADD |
| affirm.spacing.top_nav_bar.secondary.container.padding_x | size.000 | VariableID:1:2328 | | | | | ADD |
| affirm.spacing.top_nav_bar.container.gap_x | size.100 | VariableID:1:2332 | | | | | ADD |
| affirm.spacing.top_nav_bar.container.padding_y | size.050 | VariableID:1:2330 | | | | | ADD |

---

## Task 5 — In sync (exact match, no changes needed)

| Token name |
|------------|
| size/top_nav_bar/notification_indicator/all |
| radius/top_nav_bar/notification_indicator/all |
