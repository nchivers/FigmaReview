# Additional Rules

Use this file to define **interpretive rules** and **exceptions** that Claude should follow during the component implementation review. These rules can clarify Figma platform limits, scope certain checks, or add context so the reviewer does not incorrectly flag valid cases.

---

## Position tokens

**Rule:** Position tokens (e.g. variables used for x, y, left, top, or other layout position) may **not** appear as bound variables on the component in Figma, because Figma does not allow variables to be bound to position properties (x or y).

**Effect on review:** When evaluating **token coverage** (Check 1), do **not** report position tokens from the CSV as "tokens not used" or as issues. Treat them as expected exceptions. You may note in the results that position tokens were excluded from the unused-token count per this rule.

---

## Subcomponents

**Rule:** An instance of another component used inside the component being reviewed falls into two groups. Instances whose **name begins with a '.' or '_'** are **subcomponents** owned by the component being reviewed. Instances whose name **does not** begin with '.' or '_' are **not** true subcomponents (they are external or shared components).

**Effect on review:**

- **Names starting with '.' or '_' (subcomponents):** Treat these as part of the component under review. Apply **all** review criteria to them: token coverage, no hex/non-variable values, typography uses library styles, and component property naming. Include their tokens, variables, and properties in the full review.
- **Names not starting with '.' or '_' (not subcomponents):** Do **not** full-review these instances. Evaluate them **only for overrides** (e.g. whether any overrides applied to the instance are token-based or valid). Do not report missing tokens, raw values, or naming issues for the internal structure of these instances—they are out of scope.

When reporting, you may note which nested instances were treated as subcomponents (name starts with '.' or '_') vs override-only (name does not start with '.' or '_').

---

## Typography selection

**Rule:** All typography used in components must come from the **`affirm.typography/component/`** set. Typography style names (or their path/identifier) must **begin with** `affirm.typography/component/`. Any typography that does not begin with that name is out of scope and should be considered an issue.

**Effect on review:** When evaluating **typography** (Check 3), in addition to requiring that text uses defined library styles, require that the style name or path **starts with** `affirm.typography/component/`. For each text node or typography style that does **not** begin with `affirm.typography/component/`, report it as an **issue** (e.g. "Typography style [name] is not from affirm.typography/component/ set"). Include the actual style name and, if available, the node or layer it applies to.

---

## Adding more rules

Add further rules below in the same format:

- **Rule:** One-sentence description of the rule or exception.
- **Effect on review:** How Claude should apply it (which check, what to do or not do, what to note in the output).

Examples of rules you might add:

- Excluding certain token types from coverage checks (e.g. tokens used only in code, not in Figma).
- Figma limitations (e.g. a property that cannot be bound to a variable).
- Scoping a check to specific layers or property types.
- When to report something as a warning vs an issue.
