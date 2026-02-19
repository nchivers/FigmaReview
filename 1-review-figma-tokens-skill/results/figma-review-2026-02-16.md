# Figma Token Review: merchant_tile
**Date:** 2026-02-16

## Summary

| Metric | Count |
|---|---|
| CSV Tokens | 36 |
| Figma Variables (total in JSON) | 134 |
| Matched Tokens | 36 |
| Missing in Figma | 0 |
| Extra in Figma (not in CSV) | 98 |
| Naming Discrepancies | 0 |
| Assignment Discrepancies | 0 |
| Scoping Violations | 0 |

---

## Task 1: CSV vs Figma Comparison

### Missing in Figma

None. All 36 CSV tokens have matching Figma variables.

**Name conversion:** CSV uses dot notation with `affirm.` prefix (e.g. `affirm.color.merchant_tile.container.bg.resting`), Figma uses slash notation without prefix (e.g. `color/merchant_tile/container/bg/resting`). All 36 tokens resolve to exact matches after this normalization.

### Extra in Figma (not in CSV)

98 Figma variables are present in the JSON but not listed in the CSV. These belong to other components: `bottom_nav_bar`, `date_icon`, `numeric_keyboard`, and `top_nav_bar`.

<details>
<summary>Full list of 98 extra Figma variables</summary>

- color/bottom_nav_bar/bg
- color/bottom_nav_bar/item/bg/selected
- color/bottom_nav_bar/item/bg/unselected
- color/bottom_nav_bar/item/icon/selected
- color/bottom_nav_bar/item/icon/unselected
- color/bottom_nav_bar/item/text/selected
- color/bottom_nav_bar/item/text/unselected
- color/date_icon/bg
- color/date_icon/border
- color/date_icon/day/text
- color/date_icon/month/text
- color/numeric_keyboard/button/bg/disabled
- color/numeric_keyboard/button/bg/focus
- color/numeric_keyboard/button/bg/hover
- color/numeric_keyboard/button/bg/pressed
- color/numeric_keyboard/button/bg/resting
- color/numeric_keyboard/button/icon/disabled
- color/numeric_keyboard/button/icon/focus
- color/numeric_keyboard/button/icon/hover
- color/numeric_keyboard/button/icon/pressed
- color/numeric_keyboard/button/icon/resting
- color/numeric_keyboard/button/text/disabled
- color/numeric_keyboard/button/text/focus
- color/numeric_keyboard/button/text/hover
- color/numeric_keyboard/button/text/pressed
- color/numeric_keyboard/button/text/resting
- color/top_nav_bar/notification_indicator/fill
- color/top_nav_bar/tier_1/bg
- color/top_nav_bar/tier_1/inverse/static/bg
- color/top_nav_bar/tier_1/inverse/static/notification_indicator/border
- color/top_nav_bar/tier_1/inverse/static/page_title/text
- color/top_nav_bar/tier_1/notification_indicator/border
- color/top_nav_bar/tier_1/page_title/text
- color/top_nav_bar/tier_1/secondary/bg
- color/top_nav_bar/tier_1/secondary/notification_indicator/border
- color/top_nav_bar/tier_1/secondary/page_title/text
- color/top_nav_bar/tier_2/bg
- color/top_nav_bar/tier_2/inverse/static/bg
- color/top_nav_bar/tier_2/inverse/static/notification_indicator/border
- color/top_nav_bar/tier_2/inverse/static/page_title/text
- color/top_nav_bar/tier_2/notification_indicator/border
- color/top_nav_bar/tier_2/page_title/text
- color/top_nav_bar/tier_2/secondary/bg
- color/top_nav_bar/tier_2/secondary/notification_indicator/border
- color/top_nav_bar/tier_2/secondary/page_title/text
- radius/bottom_nav_bar/bottom
- radius/bottom_nav_bar/item/all
- radius/bottom_nav_bar/top
- radius/date_icon/all
- radius/numeric_keyboard/button/all
- radius/numeric_keyboard/container/bottom
- radius/numeric_keyboard/container/top
- radius/top_nav_bar/notification_indicator/all
- size/date_icon/border/width
- size/numeric_keyboard/button/height
- size/numeric_keyboard/button/min_width
- size/top_nav_bar/affirm_logo/width
- size/top_nav_bar/notification_indicator/all
- size/top_nav_bar/tier_1/inverse/static/notification_indicator/border/width
- size/top_nav_bar/tier_1/notification_indicator/border/width
- size/top_nav_bar/tier_1/secondary/notification_indicator/border/width
- size/top_nav_bar/tier_2/inverse/static/notification_indicator/border/width
- size/top_nav_bar/tier_2/notification_indicator/border/width
- size/top_nav_bar/tier_2/secondary/notification_indicator/border/width
- spacing/bottom_nav_bar/gap_x
- spacing/bottom_nav_bar/item/gap_y
- spacing/bottom_nav_bar/item/padding_y
- spacing/bottom_nav_bar/padding_bottom
- spacing/bottom_nav_bar/padding_top
- spacing/bottom_nav_bar/padding_x
- spacing/date_icon/content/gap_y
- spacing/date_icon/padding_x
- spacing/date_icon/padding_y
- spacing/numeric_keyboard/contained/container/padding_bottom
- spacing/numeric_keyboard/contained/container/padding_top
- spacing/numeric_keyboard/contained/container/padding_x
- spacing/numeric_keyboard/container/gap_y
- spacing/numeric_keyboard/container/padding_bottom
- spacing/numeric_keyboard/container/padding_top
- spacing/numeric_keyboard/container/padding_x
- spacing/numeric_keyboard/number_pad/gap_x
- spacing/numeric_keyboard/number_pad/gap_y
- spacing/top_nav_bar/tier_1/container/padding_bottom
- spacing/top_nav_bar/tier_1/container/padding_left
- spacing/top_nav_bar/tier_1/container/padding_right
- spacing/top_nav_bar/tier_1/container/padding_top
- spacing/top_nav_bar/tier_1/right_buttons/button_group/gap_x
- spacing/top_nav_bar/tier_1/right_buttons/button_group/padding_right
- spacing/top_nav_bar/tier_1/right_buttons/single_button/gap_x
- spacing/top_nav_bar/tier_1/right_buttons/single_button/padding_right
- spacing/top_nav_bar/tier_2/container/padding_bottom
- spacing/top_nav_bar/tier_2/container/padding_left
- spacing/top_nav_bar/tier_2/container/padding_right
- spacing/top_nav_bar/tier_2/container/padding_top
- spacing/top_nav_bar/tier_2/right_buttons/button_group/gap_x
- spacing/top_nav_bar/tier_2/right_buttons/button_group/padding_right
- spacing/top_nav_bar/tier_2/right_buttons/single_button/gap_x
- spacing/top_nav_bar/tier_2/right_buttons/single_button/padding_right

</details>

### Naming Discrepancies

None. All token names align exactly after accounting for the naming convention difference (dot notation with `affirm.` prefix in CSV vs slash notation in Figma).

### Assignment Discrepancies

None. All alias assignments in Figma match the expected values from the CSV across all modes.

<details>
<summary>Full assignment verification (56 mode checks)</summary>

| CSV Token | Mode | CSV Expected | Figma Alias | Match |
|---|---|---|---|---|
| affirm.color.merchant_tile.container.bg.focus_visible | Dark | gray.850 | base/g-color/gray/850 | Yes |
| affirm.color.merchant_tile.container.bg.focus_visible | Light | indigo.050 | base/g-color/indigo/050 | Yes |
| affirm.color.merchant_tile.container.bg.hover | Dark | gray.850 | base/g-color/gray/850 | Yes |
| affirm.color.merchant_tile.container.bg.hover | Light | indigo.050 | base/g-color/indigo/050 | Yes |
| affirm.color.merchant_tile.container.bg.pressed | Dark | gray.800 | base/g-color/gray/800 | Yes |
| affirm.color.merchant_tile.container.bg.pressed | Light | indigo.100 | base/g-color/indigo/100 | Yes |
| affirm.color.merchant_tile.container.bg.resting | Dark | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.bg.resting | Light | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.focus_visible | Dark | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.focus_visible | Light | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.hover | Dark | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.hover | Light | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.pressed | Dark | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.pressed | Light | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.resting | Dark | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.border.resting | Light | opacity.000 | base/g-color/opacity/000 | Yes |
| affirm.color.merchant_tile.container.outline.focus_visible | Dark | indigo.650 | base/g-color/indigo/650 | Yes |
| affirm.color.merchant_tile.container.outline.focus_visible | Light | indigo.650 | base/g-color/indigo/650 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.focus_visible | Dark | gray.030 | base/g-color/gray/030 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.focus_visible | Light | gray.950 | base/g-color/gray/950 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.hover | Dark | gray.030 | base/g-color/gray/030 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.hover | Light | gray.950 | base/g-color/gray/950 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.pressed | Dark | gray.030 | base/g-color/gray/030 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.pressed | Light | gray.950 | base/g-color/gray/950 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.resting | Dark | gray.030 | base/g-color/gray/030 | Yes |
| affirm.color.merchant_tile.merchant_info.name.text.resting | Light | gray.950 | base/g-color/gray/950 | Yes |
| affirm.color.merchant_tile.term_text.icon.focus_visible | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.icon.focus_visible | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.icon.hover | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.icon.hover | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.icon.pressed | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.icon.pressed | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.icon.resting | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.icon.resting | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.text.focus_visible | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.text.focus_visible | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.text.hover | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.text.hover | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.text.pressed | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.text.pressed | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.color.merchant_tile.term_text.text.resting | Dark | gray.300 | base/g-color/gray/300 | Yes |
| affirm.color.merchant_tile.term_text.text.resting | Light | gray.700 | base/g-color/gray/700 | Yes |
| affirm.position.merchant_tile.badge.left | All Modes | size.100 | base/size/100 | Yes |
| affirm.position.merchant_tile.badge.top | All Modes | size.100 | base/size/100 | Yes |
| affirm.position.merchant_tile.merchant_img.merchant_logo.bottom | All Modes | size.100 | base/size/100 | Yes |
| affirm.position.merchant_tile.merchant_img.merchant_logo.left | All Modes | size.100 | base/size/100 | Yes |
| affirm.radius.merchant_tile.container.all | All Modes | size.200 | base/size/200 | Yes |
| affirm.radius.merchant_tile.merchant_img.all | All Modes | size.200 | base/size/200 | Yes |
| affirm.size.merchant_tile.container.outline.width.focus_visible | All Modes | size.025 | base/size/025 | Yes |
| affirm.size.merchant_tile.merchant_img.merchant_logo.all | All Modes | size.500 | base/size/500 | Yes |
| affirm.size.merchant_tile.term_text.icon.all | All Modes | size.200 | base/size/200 | Yes |
| affirm.spacing.merchant_tile.container.outline.offset.focus_visible | All Modes | size.025 | base/size/025 | Yes |
| affirm.spacing.merchant_tile.merchant_info.gap_y | All Modes | size.000 | base/size/000 | Yes |
| affirm.spacing.merchant_tile.merchant_info.padding_bottom | All Modes | size.050 | base/size/050 | Yes |
| affirm.spacing.merchant_tile.merchant_info.padding_top | All Modes | size.025 | base/size/025 | Yes |
| affirm.spacing.merchant_tile.merchant_info.padding_x | All Modes | size.100 | base/size/100 | Yes |
| affirm.spacing.merchant_tile.term_text.gap_x | All Modes | size.025 | base/size/025 | Yes |

</details>

---

## Task 2: Scoping Rules Evaluation

**No violations found.** All 36 tokens comply with applicable scoping rules. 4 position tokens (`position/...`) have no matching rule in the scoping rules and are excluded from evaluation per the instructions.

| Figma Variable | Rule Applied | Expected Scopes | Actual Scopes | Expected Hidden | Actual Hidden | Result |
|---|---|---|---|---|---|---|
| color/merchant_tile/container/bg/focus_visible | Component color /bg/ | [FRAME_FILL, SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/container/bg/hover | Component color /bg/ | [FRAME_FILL, SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/container/bg/pressed | Component color /bg/ | [FRAME_FILL, SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/container/bg/resting | Component color /bg/ | [FRAME_FILL, SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/container/border/focus_visible | Component color /border/ | [STROKE_COLOR] | [STROKE_COLOR] | true | true | Pass |
| color/merchant_tile/container/border/hover | Component color /border/ | [STROKE_COLOR] | [STROKE_COLOR] | true | true | Pass |
| color/merchant_tile/container/border/pressed | Component color /border/ | [STROKE_COLOR] | [STROKE_COLOR] | true | true | Pass |
| color/merchant_tile/container/border/resting | Component color /border/ | [STROKE_COLOR] | [STROKE_COLOR] | true | true | Pass |
| color/merchant_tile/container/outline/focus_visible | Component color /outline/ | [STROKE_COLOR] | [STROKE_COLOR] | true | true | Pass |
| color/merchant_tile/merchant_info/name/text/focus_visible | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/merchant_info/name/text/hover | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/merchant_info/name/text/pressed | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/merchant_info/name/text/resting | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/term_text/icon/focus_visible | Component color /icon/ | includes [SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/term_text/icon/hover | Component color /icon/ | includes [SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/term_text/icon/pressed | Component color /icon/ | includes [SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/term_text/icon/resting | Component color /icon/ | includes [SHAPE_FILL] | [FRAME_FILL, SHAPE_FILL] | true | true | Pass |
| color/merchant_tile/term_text/text/focus_visible | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/term_text/text/hover | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/term_text/text/pressed | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| color/merchant_tile/term_text/text/resting | Component color /text/ | [TEXT_FILL] | [TEXT_FILL] | true | true | Pass |
| position/merchant_tile/badge/left | No matching rule | — | — | — | — | N/A |
| position/merchant_tile/badge/top | No matching rule | — | — | — | — | N/A |
| position/merchant_tile/merchant_img/merchant_logo/bottom | No matching rule | — | — | — | — | N/A |
| position/merchant_tile/merchant_img/merchant_logo/left | No matching rule | — | — | — | — | N/A |
| radius/merchant_tile/container/all | Radius | [CORNER_RADIUS] | [CORNER_RADIUS] | — | true | Pass |
| radius/merchant_tile/merchant_img/all | Radius | [CORNER_RADIUS] | [CORNER_RADIUS] | — | true | Pass |
| size/merchant_tile/container/outline/width/focus_visible | Size component /outline/ | [STROKE_FLOAT] | [STROKE_FLOAT] | true | true | Pass |
| size/merchant_tile/merchant_img/merchant_logo/all | Size component dimension | [WIDTH_HEIGHT] | [WIDTH_HEIGHT] | true | true | Pass |
| size/merchant_tile/term_text/icon/all | Size component dimension | [WIDTH_HEIGHT] | [WIDTH_HEIGHT] | true | true | Pass |
| spacing/merchant_tile/container/outline/offset/focus_visible | Spacing | [GAP] | [GAP] | true | true | Pass |
| spacing/merchant_tile/merchant_info/gap_y | Spacing | [GAP] | [GAP] | true | true | Pass |
| spacing/merchant_tile/merchant_info/padding_bottom | Spacing | [GAP] | [GAP] | true | true | Pass |
| spacing/merchant_tile/merchant_info/padding_top | Spacing | [GAP] | [GAP] | true | true | Pass |
| spacing/merchant_tile/merchant_info/padding_x | Spacing | [GAP] | [GAP] | true | true | Pass |
| spacing/merchant_tile/term_text/gap_x | Spacing | [GAP] | [GAP] | true | true | Pass |

---

## Token Mapping

The full CSV-to-Figma token mapping is in `results/figma-token-mapping-2026-02-16.csv`.
