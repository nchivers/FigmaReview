---
name: review-figma-imp
description: Reviews a Figma library component to ensure tokens are applied correctly, no hex or raw values are used for spacing/color/radius/stroke, typography uses library styles, and names/values follow defined rules. Use when reviewing a Figma component implementation, checking token usage, or auditing a component for design-system compliance.
---

# Figma Component Implementation Review

Review a given component from a Figma library against token usage, variable-only values, typography styles, and naming rules. Write findings to a single results file.

---

## Inputs

Read paths from **inputs/inputs.json** (paths are relative to the skill root):

| Key | Purpose |
|-----|--------|
| `componentUrl` | **Required.** Figma link to the component (e.g. `https://www.figma.com/design/FILE_KEY/...?node-id=NODE_ID`). Used by Figma MCP to fetch component data, or for reference when using JSON export. |
| `componentName` | Optional. Short name for the component (e.g. `merchant-tile`, `Button`). Used in the results filename so reviews of different components on different days stay separate. If missing, use `component`. |
| `componentTokensCsv` | Optional. CSV of tokens associated with this component. Used to verify "all tokens applied" and to map token → variable ID. |
| `componentExportJson` | Optional. **Fallback only.** Exported component tree from Figma (plugin or API). Use when Figma MCP is not configured. |
| `figmaVariablesJson` | Optional. Figma variables export (id, name, valuesByMode, etc.) to resolve variable IDs and validate no raw values. |
| `namingRules` | Path to rules for property/value naming (e.g. knowledge/naming-rules.md). |
| `additionalRules` | Optional. Path to interpretive rules and exceptions (e.g. knowledge/additional-rules.md). Claude applies these when running any check (e.g. exclude position tokens from "unused token" reporting). |

- **Additional rules:** If `additionalRules` is present, read that file and apply every rule when performing the review. Rules may define exceptions (e.g. do not flag position tokens as unused) or clarify how to interpret findings.
- **Component tokens CSV:** If present, use it as the source of truth for "associated tokens." First column (or column named `Token Name`, `Full Token`, or `name`) = token name. Include a column `variableId` or `figmaVariableId` with the Figma variable ID from your variables export so usage can be checked. One token per row.
- **Figma variables JSON:** Array of variable objects with `id`, `name`, `valuesByMode` (and optional `scopes`). Used to resolve aliases and ensure only variables (no hex/raw) are used.

---

## Getting component data (Figma MCP preferred)

**Prefer the Figma MCP server** when it is configured in the user's environment. Then the component link alone is enough; no manual JSON export is required.

1. **Parse componentUrl** to get:
   - **fileKey:** The first path segment after `/design/` (e.g. from `.../design/yvoTWRBHHMvvVdTphS2UpN/branch/...` use `yvoTWRBHHMvvVdTphS2UpN`). Ignore any `branch/...` segment for the key.
   - **nodeId:** The `node-id` query parameter (e.g. `5-3602`). If the URL has `node-id=5%3A3602`, decode to `5-3602`.

2. **Call Figma MCP tools** (if the Figma MCP server is available):
   - **get_variable_defs(fileKey, nodeId)** — Returns the variables and styles used in the selection (colors, spacing, typography). Use this as the primary source for: which variables are used (token coverage), and whether typography uses defined styles. If the response lists variable names and values, treat listed variables as "correctly applied"; any raw values or non-variable entries in the response should be flagged as issues (no hex / non-variable).
   - **get_design_context(fileKey, nodeId)** — Optional. Use if you need more granular node-level detail (e.g. which node has which fill or spacing) to report specific nodes for raw-value or typography issues.
   - **get_metadata(fileKey, nodeId)** — Optional. Sparse XML of layer IDs, names, types, positions, sizes; use if you need to map issues to specific layer names/IDs.

3. **Owned subcomponents (when additional rules apply):** If **additionalRules** defines owned subcomponents (e.g. local and not published), **you must get the full context for each owned subcomponent’s component set** and include it in the review. Use **[reference.md](reference.md)#resolving-owned-subcomponent-node-ids-for-mcp** to resolve each subcomponent’s **(fileKey, nodeId)** correctly:
   - Call **get_metadata(fileKey, rootNodeId)** (and optionally get_design_context) for the **root** so the response includes the full tree. Parse it for **INSTANCE** nodes and any property that references the main component (e.g. `mainComponent`, `componentId`, or a top-level `components`/`componentSets` map with `node_id` and `file_key`). If you only have **variant** node IDs (sibling COMPONENT nodes), the **component set node ID is their parent**’s id—use that.
   - **Node ID format:** Use the format the MCP expects (often colon, e.g. `3672:742`; try hyphen `3672-742` if needed).
   - For each owned subcomponent, once you have the **component set** (fileKey, nodeId), call **get_variable_defs(fileKey, nodeId)**, **get_design_context(fileKey, nodeId)**, and **get_metadata(fileKey, nodeId)**. Merge the returned data into the review scope and run all review criteria on the root **and** each owned subcomponent. In the results, label issues by component (e.g. "Root component: …" or "Subcomponent [name]: …").

4. **If Figma MCP is not available:** Use **componentExportJson** as described in [reference.md](reference.md). The user must supply an exported component tree (plugin or Figma API) with variable bindings. Ask the user to export to the path in `inputs.json` or to configure the Figma MCP for a simpler workflow.

---

## Review Criteria

Perform these checks and report every finding. If an input file is missing, note it and skip the checks that depend on it. **When additional rules define owned subcomponents,** "component data" means the root component’s context **plus** the full context (variables, design context, metadata) fetched for each owned subcomponent’s component set; run each check against the root and each owned subcomponent, and label findings by component.

### 1. Token coverage (all associated tokens applied)

- **When:** `componentTokensCsv` is provided and component data is available (from Figma MCP **get_variable_defs** or from `componentExportJson`). When owned subcomponents are in scope, use the combined context (root + each owned subcomponent).
- **Check:** Every token listed in the CSV should appear as a variable used in the component (and in owned subcomponents, when applicable). Match by variable ID or by token name → variable name (Figma variable names often use slashes, e.g. `color/button/bg/resting`).
- **Additional rules:** If **additionalRules** is loaded, apply any exceptions (e.g. position tokens: do not report them as unused, because Figma cannot bind variables to x/y).
- **Report:** List each token from the CSV that does **not** appear in the component’s used variables and is **not** excluded by additional rules. Highlight these as **issues** (tokens not used). If any tokens were excluded per additional rules, note that in the results.

### 2. No hex or non-variable values; no direct base tokens

- **When:** Component data is available (from Figma MCP **get_variable_defs** / **get_design_context** or from `componentExportJson`). Optionally use `figmaVariablesJson` to resolve variable IDs and variable names.
- **Check:** For spacing, color, border radius, stroke color, and stroke width, values must be variable references only (no hex, no raw RGB/RGBA, no raw numbers). When using MCP: **get_variable_defs** lists “variables and styles used”; treat anything that is a raw value (hex, numeric, or explicit RGB) in the response as an issue. When using JSON export: require bound variable IDs for fills, strokes, cornerRadius, layout padding/gap, stroke weight. (2) **No direct base tokens:** Any variable used for those properties whose **name begins with `base/`** (the base token set) must also be flagged as an issue. Components should use component or semantic tokens, not base tokens directly; resolve variable names via `figmaVariablesJson` when needed to detect `base/` usage.
- **Report:** For each place where a raw value is used instead of a variable, record: node/layer name or ID (if available), property, and the raw value. For each place where a variable with a name starting with `base/` is used, record: node/layer (if available), property, and the variable name. Mark all as **issue**.

### 3. Typography uses library styles

- **When:** Component data includes text or typography (from Figma MCP **get_variable_defs** “styles” / **get_design_context** or from `componentExportJson` text nodes).
- **Check:** All typography must use **defined styles** from the library (e.g. bound text style). When using MCP: **get_variable_defs** returns “variables and styles used”; typography should appear as named styles, not ad-hoc font/size/lineHeight. When using JSON: text nodes should have `textStyleId` bound to a library style.
- **Report:** List each text node or style entry that does not use a library typography style. Mark as **issue**.

### 4. Component property naming (variant, boolean, content swap, text)

- **When:** `namingRules` file exists and is readable (e.g. knowledge/naming-rules.md).
- **Check:** Apply the rules in that file **only** to component set properties: **variant** (e.g. Interaction with values Resting, Hover, Focus-Visible, Pressed, Disabled), **boolean**, **content swap**, and **text** properties. Verify property names and their values match the defined rules. Do not use this check for variable/token names or token usage—those are covered by checks 1 and 2.
- **Report:** List each violation with: component property name, actual value(s), the rule that was broken, and expected name or value. Mark as **issue**.

---

## Output

Write exactly one results file:

- **Path:** `results/YYYY-MM-DD-HH-MM-{componentName}-figma-imp-review.md`. Use `componentName` from inputs.json if present; sanitize for filenames (lowercase, replace spaces and invalid chars with hyphens, e.g. "Merchant Tile" → `merchant-tile`). If `componentName` is missing, use `component`. Use today’s date in ISO format for YYYY-MM-DD-HH-MM.
- **Contents:**
  1. **Inputs used** – componentName (if set); componentUrl; whether component data came from Figma MCP or from componentExportJson; which of CSV, variables JSON, naming rules, and additional rules were present. If owned subcomponents were in scope, list them and confirm their context was fetched and included.
  2. **1. Token coverage** – Tokens not used (from CSV) or note that CSV/export was missing.
  3. **2. Raw values and direct base tokens** – List of node/property where a raw value was used or a variable whose name starts with `base/` was used.
  4. **3. Typography** – Text nodes not using library typography styles.
  5. **4. Component property naming** – Violations of naming-rules (variant, boolean, content swap, text property names and values; or note that rules file was missing).
  6. **Summary** – Count of issues per category and any critical vs non-critical note if the rules define them.

Use clear headings and bullet lists. When the review includes owned subcomponents, label each finding by component (e.g. "Root component:", "Subcomponent [name]:") so readers can see where each issue lives. If a section has no findings, write "None" or "No issues." Do not modify input files; only write the results file.

---

## Workflow

1. Read **inputs/inputs.json** and resolve paths relative to the skill root. Require **componentUrl**. If **additionalRules** is specified, load that file and apply its rules throughout the review.
2. **Get component data:** If the Figma MCP server is available, parse **componentUrl** for fileKey and nodeId, then call **get_variable_defs** (and optionally **get_design_context** or **get_metadata**) and use the response as component data. If **additionalRules** defines owned subcomponents, identify each owned subcomponent and **get the full context** (get_variable_defs, get_design_context, get_metadata) for each one’s component set and include it in the data used for the review. Otherwise, load **componentExportJson** if provided; if neither MCP nor export is available, inform the user that they should either configure the Figma MCP or supply a component export at `componentExportJson`.
3. Load other optional inputs (CSV, variables JSON, naming rules).
4. Run each applicable check (1–4) using the component data and collect issues.
5. Write **results/YYYY-MM-DD-HH-MM-{componentName}-figma-imp-review.md** with all findings (componentName from inputs, sanitized; date = today).

**Note:** With Figma MCP configured, the user only needs to set **componentUrl** in inputs.json (and optionally the CSV and naming rules). No manual component export is required.
