# Figma Component Implementation Review Skill

Claude skill that reviews a Figma library component for token usage, variable-only values, typography styles, and naming rules.

## Preferred: Figma MCP

If you use the **Figma MCP server** (Cursor/Claude with Figma MCP configured), the skill can pull component data directly from Figma. You only need to set **componentUrl** in `inputs/inputs.json`; no manual export is required. The skill parses the URL for file key and node ID and calls `get_variable_defs` (and optionally `get_design_context`) to run the review.

- **Remote MCP:** [Figma docs](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/) — requires `fileKey` and `nodeId` (both are derived from the component link).
- **Desktop MCP:** Uses the currently open file; the link’s `node-id` still identifies the component.

## Setup

1. **inputs/inputs.json**  
   Set **componentUrl** to the Figma link of the component to review (required). Set **componentName** (e.g. `merchant-tile`) to name the component; the results file will be `results/figma-imp-review-{componentName}-YYYY-MM-DD.md` so reviews of different components stay separate. Paths in this file are relative to this skill root.

2. **Optional: inputs/component-tokens.csv**  
   List tokens that should be used by this component. Include a `variableId` column (Figma variable ID) so the skill can check that each token is actually applied. Tokens in the CSV that are not bound in the component are reported as issues.

3. **Optional: inputs/component-export.json**  
   **Only if Figma MCP is not used.** Exported component tree from Figma (plugin or API) including variable bindings. See **reference.md** for expected shape.

4. **Optional: inputs/figma-variables.json**  
   Your Figma variables export. Used to resolve variable IDs and validate that only variables (no hex/raw values) are used.

5. **knowledge/naming-rules.md**  
   Customize with your team’s naming and value rules for component properties (variant, boolean, content swap, text).

6. **knowledge/additional-rules.md**  
   Optional. Add interpretive rules and exceptions (e.g. “do not flag position tokens as unused because Figma cannot bind variables to x/y”). Claude applies these when running any check.

## Review criteria

- **Token coverage:** Every token in the CSV must be bound in the component; unused tokens are reported.
- **No raw values; no direct base tokens:** Spacing, color, border radius, stroke color, and stroke width must use variables only (no hex or raw numbers). Variables whose name begins with `base/` must be flagged—components should use component/semantic tokens, not base tokens directly.
- **Typography:** All text must use defined typography styles from the library (no ad-hoc font/size).
- **Naming rules:** Names and values must follow **knowledge/naming-rules.md**.

## Output

Results are written to **results/figma-imp-review-{componentName}-YYYY-MM-DD.md** (e.g. `figma-imp-review-merchant-tile-2026-02-16.md`). Use **componentName** in inputs.json to keep reviews of different components on different days separate.

## Getting component data without MCP

If the Figma MCP server is not configured, you need the component tree with variable bindings in **inputs/component-export.json**. Options:

- **Figma plugin:** Add an “Export component” action that serializes the selected component (and its `boundVariables`) to JSON and save as `inputs/component-export.json`.
- **Figma API:** Use the REST API to fetch the file and the component node; map bound variables from the response into the shape described in **reference.md**.
