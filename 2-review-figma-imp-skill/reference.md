# Component Export Schema (Reference)

**Preferred:** Use the **Figma MCP server** with **componentUrl** so the skill can fetch component data via `get_variable_defs` (and optionally `get_design_context`). No export file is needed.

**Fallback:** When MCP is not available, the **component export** must expose node properties and variable bindings. The skill expects data in this shape (or equivalent).

---

## Source of export

- **Figma plugin:** Export the selected component (or current selection) to JSON. Include the node tree and, for each node, bound variable IDs where applicable.
- **Figma REST API:** Use endpoints that return node tree with bound variables (e.g. `GET /v1/files/:key/nodes?ids=...` with appropriate depth). Map variable bindings from the response.

---

## Expected node properties

For each node in the export, the reviewer needs:

| Property | Used for | Variable binding |
|----------|----------|-------------------|
| `id`, `name` | Identification | — |
| `fills` | Color check (no hex) | Each fill may have `boundVariableId` or `variableId`; raw `{r,g,b,a}` or hex = issue |
| `strokes` | Stroke color (no hex) | Same as fills |
| `strokeWeight`, `strokeAlign` | Stroke width (must be variable) | Bound variable for stroke weight if your system tokens it |
| `cornerRadius`, `rectangleCornerRadii` | Border radius (must be variable) | Bound variable |
| `paddingLeft`, `paddingRight`, `paddingTop`, `paddingBottom` | Spacing | Bound variable |
| `itemSpacing` (auto layout) | Gap | Bound variable |
| `textStyleId` | Typography style | Must reference a library style |
| `fontName`, `fontSize`, `lineHeight`, `letterSpacing` | Fallback if no style | If present without bound style, typography check flags it |

---

## Variable binding format

- **Figma API:** Fills/strokes can show `boundVariables.fills` / `boundVariables.strokes` with `id` → variable ID. Layout may have `boundVariables.paddingLeft` etc.
- **Plugin:** Use `node.boundVariables` (Figma plugin API) and serialize variable IDs for fills, strokes, corner radius, layout padding, and stroke weight.

The reviewer resolves these IDs using **figma-variables.json** (id → name, valuesByMode) when that file is provided.

---

## Minimal example (conceptual)

```json
{
  "id": "node-id",
  "name": "Container",
  "type": "FRAME",
  "fills": [{ "type": "VARIABLE_ALIAS", "id": "VariableID:..." }],
  "boundVariables": {
    "fills": [{ "id": "VariableID:..." }],
    "layoutPaddingLeft": [{ "id": "VariableID:..." }]
  },
  "cornerRadius": 8,
  "children": [...]
}
```

If `cornerRadius` is a raw number and no bound variable is present for it, the reviewer reports: "cornerRadius uses raw value 8 instead of variable." If a bound variable is present, the reviewer does not flag it (variable is used).

Adapt this to the actual export format your plugin or API produces; the skill matches on the presence of variable IDs vs raw values for the listed properties.
