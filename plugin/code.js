/**
 * Serialize a variable value for JSON (handles RGB, RGBA, VariableAlias, primitives).
 * @param {VariableValue} value
 * @param {Map<string, string>} variableIdToName - optional map to add alias names
 * @returns {object|string|number|boolean}
 */
function serializeVariableValue(value, variableIdToName) {
  if (value === null || value === undefined) {
    return value;
  }
  if (typeof value === "object" && value !== null) {
    if (value.type === "VARIABLE_ALIAS") {
      const alias = { type: "VARIABLE_ALIAS", id: value.id };
      if (variableIdToName && variableIdToName.has(value.id)) {
        alias.name = variableIdToName.get(value.id);
      }
      return alias;
    }
    if ("r" in value && "g" in value && "b" in value) {
      const color = { r: value.r, g: value.g, b: value.b };
      if ("a" in value) color.a = value.a;
      return color;
    }
  }
  return value;
}

/**
 * Build a JSON-serializable object for one variable.
 * @param {Variable} variable
 * @param {Map<string, string>} collectionIdToName
 * @param {Map<string, string>} modeIdToName
 * @param {Map<string, string>} variableIdToName
 */
function variableToExportShape(variable, collectionIdToName, modeIdToName, variableIdToName) {
  const collectionId = variable.variableCollectionId;
  const collectionName = collectionIdToName.has(collectionId)
    ? collectionIdToName.get(collectionId)
    : collectionId;

  const valuesByMode = {};
  for (const [modeId, value] of Object.entries(variable.valuesByMode)) {
    const modeName = modeIdToName.has(modeId) ? modeIdToName.get(modeId) : modeId;
    valuesByMode[modeId] = {
      modeName: modeName,
      value: serializeVariableValue(value, variableIdToName),
    };
  }

  return {
    id: variable.id,
    name: variable.name,
    collection: collectionName,
    resolvedType: variable.resolvedType,
    valuesByMode,
    hiddenFromPublishing: variable.hiddenFromPublishing,
    scopes: variable.scopes != null ? [...variable.scopes] : [],
  };
}

/**
 * Export all local variables to a JSON-serializable array.
 */
async function exportVariablesToJson() {
  const [variables, collections] = await Promise.all([
    figma.variables.getLocalVariablesAsync(),
    figma.variables.getLocalVariableCollectionsAsync(),
  ]);

  const collectionIdToName = new Map();
  const modeIdToName = new Map();
  for (const coll of collections) {
    collectionIdToName.set(coll.id, coll.name);
    if (coll.modes) {
      for (let i = 0; i < coll.modes.length; i++) {
        const mode = coll.modes[i];
        modeIdToName.set(mode.modeId, mode.name);
      }
    }
  }

  const variableIdToName = new Map();
  for (let i = 0; i < variables.length; i++) {
    variableIdToName.set(variables[i].id, variables[i].name);
  }

  // Resolve alias targets (local or library) so we can include their names
  var aliasIds = [];
  for (let i = 0; i < variables.length; i++) {
    var vals = variables[i].valuesByMode;
    for (var modeId in vals) {
      if (vals.hasOwnProperty(modeId)) {
        var v = vals[modeId];
        if (v && typeof v === "object" && v.type === "VARIABLE_ALIAS" && v.id) {
          if (!variableIdToName.has(v.id)) aliasIds.push(v.id);
        }
      }
    }
  }
  var seen = {};
  for (let j = 0; j < aliasIds.length; j++) {
    var aid = aliasIds[j];
    if (seen[aid]) continue;
    seen[aid] = true;
    try {
      var resolved = await figma.variables.getVariableByIdAsync(aid);
      if (resolved && resolved.name) variableIdToName.set(aid, resolved.name);
    } catch (err) {}
  }

  const payload = variables.map(function (v) {
    return variableToExportShape(v, collectionIdToName, modeIdToName, variableIdToName);
  });
  return payload;
}

figma.showUI(__html__, { themeColors: true, width: 480, height: 360 });

figma.ui.onmessage = async (msg) => {
  if (msg.type === "export-variables") {
    try {
      const data = await exportVariablesToJson();
      figma.ui.postMessage({ type: "export-result", data });
    } catch (e) {
      figma.ui.postMessage({
        type: "export-error",
        message: e instanceof Error ? e.message : String(e),
      });
    }
  }
};
