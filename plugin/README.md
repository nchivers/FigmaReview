# Export Variables to JSON (Figma plugin)

Figma plugin that exports variable information from the current file (e.g. a library file) to JSON.

## Exported fields

For each variable, the JSON includes:

- **id** – variable ID
- **name** – variable name
- **collection** – name of the variable collection it belongs to
- **resolvedType** – `"BOOLEAN"` | `"COLOR"` | `"FLOAT"` | `"STRING"`
- **valuesByMode** – map of mode ID → value (primitives, `{ r, g, b }` / `{ r, g, b, a }`, or `{ type: "VARIABLE_ALIAS", id: "..." }`)
- **hiddenFromPublishing** – boolean
- **scopes** – array of `VariableScope` strings (e.g. `"ALL_SCOPES"`, `"TEXT_CONTENT"`, `"FILL"`, …)

## How to run

1. In Figma: **Plugins** → **Development** → **Import plugin from manifest…**
2. Select the **manifest.json** file in this folder.
3. Open a file that has local variables (e.g. your library file).
4. Run **Plugins** → **Development** → **Export Variables to JSON**.
5. Click **Export variables**, then **Copy JSON** or select the text and copy manually.

## Files

- **manifest.json** – plugin manifest
- **code.js** – plugin logic (reads variables, sends JSON to UI)
- **ui.html** – plugin UI (export button, JSON preview, copy)
