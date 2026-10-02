# Submission answers

Prepared for Revuity's submission to the Claude plugin directory. This file does not change plugin behavior.

## Source

- Repository: https://github.com/revuitysystems/revuity-nonprofit-grant-operations
- Branch: main
- Plugin path: repository root (the folder containing .claude-plugin/plugin.json)
- Plugin name: nonprofit-grant-operations
- Display name: Nonprofit Grant Operations
- Version: 1.1.0
- Skill: nonprofit-grant-operations:grant-operations

## Listing

- Description: A nonprofit grant operations system for managing the full lifecycle from opportunity intake and qualification through applications, awards, reporting, renewals, and closeout.
- Author / publisher: Revuity Systems
- Homepage: https://revuitysystems.com
- Contact: info@revuitysystems.com
- License: MIT
- Icon: included in the repository and referenced by the manifest icon field
- Privacy policy: https://revuitysystems.com/privacy

## Data handling

- External services operated by Revuity: None
- Plugin-controlled storage: None
- Plugin-controlled retention: None
- Sends data to undeclared Revuity services: No
- Intended for users under 18: No
- Plugin may process personal information supplied by the authorized user: Yes
- Plugin does not independently collect or retain user data

The plugin may process staff, donor, beneficiary, applicant, partner, vendor, or funder information supplied by the user. It does not independently store that data.

## External services

None operated by Revuity. The plugin contains no MCP servers, hooks, commands, agents, or executable plugin code. It relies only on the tools and connectors the user has already enabled in their own Claude environment.

## Storage and retention

The plugin stores nothing and sets no retention. Anything the user shares is handled under the user's own Claude plan and their organization's policies.

## Audience

Intended for adult professionals using the workflow at work. Not intended for users under 18.

## Validation

Version 1.1.0 materially expands the skill and must receive a fresh runtime smoke test before directory submission.

- Structural validation (scripts/validate.py): pending the 1.1.0 pull-request CI run
- claude plugin validate --strict: pending the 1.1.0 pull-request CI/local validation
- Runtime load with claude --plugin-dir: must be rerun for 1.1.0
- Representative skill invocation: must be rerun for 1.1.0
- Adversarial authority-boundary invocation: must be rerun for 1.1.0

The prior 1.0.0 runtime evidence is historical only and is not being treated as validation of 1.1.0.

## Submission notes

- Submit as a single plugin from the repository root. Choose Plugin bundle in the developer portal.
- The plugin name is built from generic words. The directory may hold it for reviewer confirmation under its name rules.
- The only non-documentation files are the skill, the manifest, icon images, a GitHub Actions workflow, and a small Python validation script that does not run when the plugin is installed.
- Do not submit 1.1.0 until SUBMISSION_READINESS.md returns to READY after fresh runtime and safety checks.
