# Finn-loop Sandbox

Private verification repository for Chad's local Hermes Finn-loop.

The workflow is:

1. Human-approved Linear issue labelled `agent-ready`.
2. Hermes `build` creates a branch and pull request.
3. GitHub Actions runs the required `test` check.
4. Hermes `review` posts a commit-specific verdict.
5. Chad explicitly approves every final merge.

This repository contains no family, client, or business data.
