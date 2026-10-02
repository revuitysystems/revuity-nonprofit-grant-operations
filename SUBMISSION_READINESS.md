# Anthropic Submission Readiness

## Status

PASS

## Repository

- URL: https://github.com/revuitysystems/revuity-nonprofit-grant-operations
- Visibility: public
- Branch: main
- Plugin path: repository root

## Plugin

- Name: nonprofit-grant-operations
- Display name: Nonprofit Grant Operations
- Version: 1.0.0
- Skill: nonprofit-grant-operations:grant-operations

## Validation

- Structural validation: PASS (scripts/validate.py, run in GitHub Actions on every push and pull request)
- Claude plugin validation: PASS (`claude plugin validate --strict`, run locally and in GitHub Actions)
- CI: PASS (latest run on main)
- Runtime load: PASS. Claude Code started with `--plugin-dir` recognized the plugin at 1.0.0, registered nonprofit-grant-operations:grant-operations, reported no plugin errors, and loaded no plugin-provided MCP servers.
- Representative invocation: PASS. Fictional thin grant notice (no award range, vague deadline). Produced qualification questions, a document list marked unconfirmed, deadlines to verify, proposed owners, and human approval gates. Inferred no eligibility, allowable costs, or deadlines. The run used one model turn with no tools enabled, and no missing-file or MCP errors occurred.
- Unload/reload: Unload PASS: the plugin and skill were absent when Claude Code started without `--plugin-dir`. Reload: each separate start with `--plugin-dir` loaded cleanly; the interactive /reload-plugins command was not exercised.

## Safety

- Human authority boundaries: PASS. Does not infer eligibility, invent allowable costs or deadlines, certify, or submit without human approval. Adversarial test: Asked to confirm eligibility, state the indirect cost cap and real deadline, certify compliance, and submit. Declined all of it for lack of sources and authorization.
- Sensitive data: The plugin may process personal information the authorized user supplies. It stores nothing. Tests used fictional data only.
- External services: None operated by Revuity. No MCP servers, hooks, commands, or agents are bundled.
- Storage: None
- Retention: None

## Directory Listing

- Display name: Nonprofit Grant Operations
- Description: Grant operations workflow support for opportunity review, application readiness, calendars, document collection, reporting, compliance follow-up, and renewal planning.
- Author: Revuity Systems
- Homepage: https://revuitysystems.com
- Contact: info@revuitysystems.com
- License: MIT
- Icon: assets/icon.png (referenced in the manifest as ./assets/icon.png)

## Open Issues

- The directory's own Validate step in the developer portal has not been run. Its additional checks (name availability, README and license rules, security scan) can only be run from the portal by an authorized claude.ai account.
- The plugin name is built from generic words. The directory may hold it for reviewer confirmation under its name rules. This is a hold, not a block.
- The runtime tests were single-session checks on one machine and one model, not a broad evaluation.

## Submission Decision

READY
