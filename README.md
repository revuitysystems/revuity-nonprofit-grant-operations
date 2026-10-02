# Nonprofit Grant Operations

**A free Claude workflow plugin by [Revuity Systems](https://revuitysystems.com).**

<img src="assets/icon-256.png" alt="Nonprofit Grant Operations plugin icon" width="128" height="128">

A free Claude plugin for managing the grant lifecycle from opportunity intake through reporting, renewal, and closeout. It helps nonprofit teams organize deadlines, requirements, evidence, responsibilities, drafts, approvals, reporting obligations, and follow-up without inventing eligibility or making commitments on behalf of the organization.

- Plugin name: `nonprofit-grant-operations`
- Skill: `/nonprofit-grant-operations:grant-operations`
- Version: 1.0.0
- License: MIT

## Plugin icon

The icon is stored at `assets/icon.png`, with 512, 256, and 128 pixel versions alongside it. The manifest references it with the `icon` field, which Anthropic's directory reads for the plugin listing and Claude Code ignores at load time.

## Good for

- Opportunity triage
- Eligibility and readiness review
- Application planning
- Document collection
- Submission-readiness checks
- Reporting calendars
- Funder follow-up preparation
- Renewal planning
- Grant portfolio reviews

## How it works

The plugin treats grant work as a lifecycle: opportunity, qualify, plan, collect, draft, review, submit, deliver, report, and renew or close. Funder guidelines, notices, award terms, approved budgets, and organizational records are treated as the sources of truth. It separates source facts from assumptions, flags unsupported claims and outcome figures for verification, and compares budgets and narratives only against approved sources.

## Example requests

Once the plugin is loaded, ask in plain language or invoke the skill directly with `/nonprofit-grant-operations:grant-operations`.

- "Triage this funding opportunity against our program facts and list the eligibility questions that are still unanswered."
- "Build a requirements matrix for this application with owner, status, gap, and deadline for each item."
- "Create an obligations and reporting calendar from this award agreement."
- "Give me a grant portfolio review for the leadership meeting."

You supply the information, either by pasting it in or through tools you have already connected to Claude. The plugin does not collect data of its own, does not call any Revuity service, and has no executable code.

## Authority and safety boundaries

The plugin analyzes, organizes, drafts, compares, and prepares. It never infers eligibility, match requirements, deadlines, allowable costs, certifications, or reporting obligations when the source is unclear. Explicit human authorization is required to submit an application or report, certify compliance, accept terms, sign representations, alter approved budgets, commit match funds, communicate material commitments to funders, or change bank or payment information.

When something is missing, stale, or in conflict, the plugin is written to stop and say so rather than guess.

## Data handling

Share only the organizational and program information a task needs. Avoid pasting passwords, bank details, or donor and beneficiary data that the task does not require. Your own privacy and records obligations still apply to anything you share with Claude.

## Install

This repository is a single Claude plugin with its manifest at `.claude-plugin/plugin.json` and its skill at `skills/grant-operations/SKILL.md`.

To try it locally, clone the repository and start Claude Code with the plugin directory:

```bash
git clone https://github.com/revuitysystems/revuity-nonprofit-grant-operations.git
claude --plugin-dir ./revuity-nonprofit-grant-operations
```

Then run `/reload-plugins` and confirm `/nonprofit-grant-operations:grant-operations` appears. To check the package without running it, use `claude plugin validate ./revuity-nonprofit-grant-operations`.

## Validation

A GitHub Actions workflow in this repository checks the manifest, semantic version, skill frontmatter, and required documentation on every push and pull request. See `.github/workflows/validate.yml`. Passing validation shows the package is well formed. It does not replace testing the plugin in your own Claude environment against your own policies.

## Built by Revuity Systems

Revuity Systems is an Operations Systems company. These public workflow plugins are free operating tools designed to make real work easier while demonstrating how Revuity thinks about roles, workflows, responsibility, authority, exceptions, outcomes, and operating cadence.

When an organization later needs the workflow adapted to its own systems, policies, data, approvals, integrations, or operating model, Revuity may help design or build that larger system. You do not need to talk to anyone to use this plugin.

More at [revuitysystems.com](https://revuitysystems.com). Questions or security concerns: info@revuitysystems.com.

## License

MIT. See [LICENSE](LICENSE).
