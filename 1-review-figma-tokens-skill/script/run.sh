#!/usr/bin/env bash
# Compile the Figma review prompt and run it with Claude.
# Run from the review-skill directory so inputs/ and results/ paths resolve.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REVIEW_SKILL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
KNOWLEDGE="$REVIEW_SKILL_ROOT/knowledge"
BUILD="$REVIEW_SKILL_ROOT/build"
RESULTS="$REVIEW_SKILL_ROOT/results"
COMPILED_PROMPT="$BUILD/compiled-prompt.md"

cd "$REVIEW_SKILL_ROOT"
mkdir -p "$BUILD" "$RESULTS"

# Compile prompt: core instructions + embedded scoping rules (so the model has full context)
{
  echo "---"
  echo "Read the input files from this workspace (paths relative to review-skill):"
  echo "  - inputs/inputs.json (componentName for output file names)"
  echo "  - inputs/component-tokens.csv"
  echo "  - inputs/figma-variables.json"
  echo "---"
  echo ""
  cat "$KNOWLEDGE/prompt-core.md"
  echo ""
  echo "---"
  echo "## Scoping rules (reference)"
  echo ""
  cat "$KNOWLEDGE/scoping-rules.md"
} > "$COMPILED_PROMPT"

echo "Compiled prompt to $COMPILED_PROMPT"

# Run Claude with the compiled prompt (non-interactive). Claude will read the inputs and write results.
if command -v claude &>/dev/null; then
  claude -p "$(cat "$COMPILED_PROMPT")"
else
  echo "Claude CLI not found. Run the review manually:"
  echo "  1. From $REVIEW_SKILL_ROOT, open inputs/inputs.json, inputs/component-tokens.csv and inputs/figma-variables.json in context."
  echo "  2. Use the compiled prompt: $COMPILED_PROMPT"
  echo "  3. Claude will write output to results/figma-review-<componentName>-<date>.md and results/figma-token-mapping-<componentName>-<date>.csv"
fi
