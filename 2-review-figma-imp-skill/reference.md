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

---

## Resolving owned subcomponent node IDs (for MCP)

To fetch full context for an **owned subcomponent**, you need the **component set’s** `fileKey` and `nodeId` (the main component node), not the instance node. Use the following so the MCP can be called correctly.

### Node ID format

- Figma uses **colon** in API responses (e.g. `3672:742`). URLs use **hyphen** (e.g. `node-id=3672-742`).
- When calling MCP tools, use the **same format the MCP expects**. If the tool accepts `nodeId`, try the colon form first (e.g. `3672:742`); if that fails, try the hyphen form (e.g. `3672-742`). Be consistent once you know which works.

### How to get the component set node ID for a subcomponent

1. **Call get_metadata(fileKey, rootNodeId)** (and optionally **get_design_context**) for the **root** component so the response includes the full tree of descendants. Use a **depth** or scope that includes all nested instance nodes.

2. **Parse the response for instance nodes.** Look for nodes with type `INSTANCE` (or the MCP’s equivalent for “component instance”). For each instance that you later classify as an owned subcomponent, you need the **main component** (component set) that instance references.

3. **Main component reference in the response:** The MCP or underlying API may expose the main component in one of these ways:
   - **Direct on the instance:** A property on the instance node such as `mainComponent`, `componentId`, `componentKey`, or `componentSetId`. It may be an object with `file_key` and `node_id`, or a string key you can look up.
   - **Top-level map:** A top-level `components` or `componentSets` object mapping an id/key to `{ file_key, node_id }`. Use the instance’s `componentId` or `componentKey` to look up that object and read `node_id` (and `file_key` if the subcomponent is in another file).
   - If you find a **node_id** (and optional **file_key**) for the main component, use those to call **get_variable_defs(fileKey, nodeId)** and **get_design_context** / **get_metadata** for the subcomponent. That node_id is the **component set** node (or the default variant’s component node; both can work for variable defs).

4. **If you only have variant node IDs:** Sometimes the response only gives you **variant** node IDs (e.g. `3672:738`, `3672:740`) — these are usually **COMPONENT** nodes that are **children** of a **COMPONENT_SET**. In that case:
   - The **component set** is the **parent** of those variant nodes. Inspect the tree: the node whose `children` (or equivalent) list contains `3672:738` and `3672:740` has an `id` — that **id is the component set node ID**. Use that with **get_variable_defs(fileKey, componentSetNodeId)** to get variables for the **entire** set (all interaction states/variants).
   - If the metadata does not list parent ids, request the file/nodes with sufficient **depth** so you receive the parent of the variant nodes, or request multiple node ids including the suspected parent (e.g. a node id one level above the variants in the hierarchy).

5. **Call MCP for the component set:** Once you have **(fileKey, nodeId)** for the subcomponent’s **component set**, call **get_variable_defs(fileKey, nodeId)**, and optionally **get_design_context(fileKey, nodeId)** and **get_metadata(fileKey, nodeId)**. Use the same fileKey as the root if the subcomponent is in the same file. Merge the returned variables and context into the review scope and run all checks (token coverage, no raw/base tokens, typography, naming) for that subcomponent, labeling findings with the subcomponent name.
