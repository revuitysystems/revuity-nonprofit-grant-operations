# Submission answers

Prepared for Revuity's submission to the Claude plugin directory. This file does not change plugin behavior.

## Source

- Repository: https://github.com/revuitysystems/revuity-nonprofit-grant-operations
- Branch: main
- Plugin path: repository root (the folder containing .claude-plugin/plugin.json)
- Plugin name: nonprofit-grant-operations
- Display name: Nonprofit Grant Operations
- Version: 1.0.0
- Skill: nonprofit-grant-operations:grant-operations

## Listing

- Description: Grant operations workflow support for opportunity review, application readiness, calendars, document collection, reporting, compliance follow-up, and renewal planning.
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

The plugin may process staff, donor, beneficiary, applicant, partner, or funder contact information supplied by the user. It does not independently store that data.

## External services

None operated by Revuity. The plugin contains no MCP servers, hooks, commands, agents, or executable plugin code. It relies only on the tools and connectors the user has already enabled in their own Claude environment.

## Storage and retention

The plugin stores nothing and sets no retention. Anything the user shares is handled under the user's own Claude plan and their organization's policies.

## Audience

Intended for adult professionals using the workflow at work. Not intended for users under 18.

## Validation

- Structural validation (scripts/validate.py): PASS in GitHub Actions
- claude plugin validate --strict: PASS locally and in GitHub Actions
- Runtime load with claude --plugin-dir: PASS (plugin recognized at 1.0.0, skill nonprofit-grant-operations:grant-operations registered, no plugin errors, no plugin-provided MCP servers, absent when started without the flag)
- Representative skill invocation: PASS (fictional-data prompt plus one adversarial boundary prompt; details in SUBMISSION_READINESS.md)

## Submission notes

- Submit as a single plugin from the repository root. Choose Plugin bundle in the developer portal.
- The plugin name is built from generic words. The directory may hold it for reviewer confirmation under its name rules.
- The only non-documentation files are the skill, the manifest, icon images, a GitHub Actions workflow, and a small Python validation script that does not run when the plugin is installed.
