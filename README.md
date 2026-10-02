# Nonprofit Grant Operations

**A free Claude workflow plugin by [Revuity Systems](https://revuitysystems.com).**

![Nonprofit Grant Operations plugin icon](assets/icon-128.png)

A nonprofit grant operations system for managing the full lifecycle from opportunity intake through application development, award setup, implementation, reporting, renewal, and closeout.

It is designed for nonprofit leaders, grant managers, development teams, program staff, finance staff, and operations teams that need grant work to be visible, owned, evidence-backed, and ready for human decision.

- Plugin name: `nonprofit-grant-operations`
- Skill: `/nonprofit-grant-operations:grant-operations`
- Version: 1.1.0
- License: MIT

## What it helps run

### Pipeline and qualification

- Grant opportunity intake
- Grant pipeline reviews
- Eligibility and readiness checks
- Go / hold / no-go decision briefs
- Mission, program, geography, capacity, and burden review

### Application operations

- Backward application plans
- Requirements and evidence matrices
- Organizational evidence libraries
- Narrative planning and drafting
- Evidence-to-claim checks
- Budget / narrative consistency reviews
- Attachment and partner-input tracking
- Submission-readiness gates

### Award operations

- Award acceptance briefs
- Award-term review
- Award kickoff packs
- Obligations registers
- Reporting calendars
- Evidence collection plans
- Budget / delivery monitoring
- Risk and exception tracking

### Reporting and change control

- Reporting workbenches
- Metric and evidence verification
- Financial / narrative reconciliation
- Funder communication drafts
- Amendment and change records
- Extension and budget-revision preparation

### Renewal and closeout

- Renewal readiness briefs
- Continuation planning
- Closeout plans
- Final reporting coordination
- Records-retention requirement tracking from authoritative sources

### Operating rhythm

- Weekly grant operations reviews
- Monthly portfolio reviews
- Quarterly leadership briefs
- Decision, risk, and exception tracking across the grant portfolio

## How it works

The plugin treats grant work as an operating lifecycle:

`discover -> intake -> qualify -> decide -> plan -> collect -> draft -> review -> submit -> award setup -> deliver -> monitor -> report -> amend if needed -> renew/close`

Funder guidelines, notices, award documents, approved organizational records, approved program facts, approved budgets, and connected systems are treated as sources of truth.

The plugin separates facts, assumptions, open questions, recommendations, and decisions. It is designed to stop unsupported claims from quietly becoming grant facts.

## Example requests

Once the plugin is loaded, ask in plain language or invoke the skill directly with `/nonprofit-grant-operations:grant-operations`.

### Opportunity and pipeline

- "Build a grant pipeline from these opportunities and show me which ones need a decision this month."
- "Create a go/no-go brief for this opportunity using only the eligibility and program facts we can support."
- "Compare these three opportunities by fit, burden, timing, and evidence gaps."

### Application development

- "Turn this funding notice into a requirements and evidence matrix."
- "Build a backward application plan with owners, dependencies, review gates, and risks."
- "Draft this narrative section from our approved program facts and flag every unsupported claim."
- "Compare the budget, budget narrative, staffing plan, and program narrative for inconsistencies."
- "Run a submission-readiness review and tell me exactly what is blocked."

### Award management

- "Turn this award agreement into an award acceptance brief and obligations register."
- "Build an award kickoff pack for program, finance, and leadership."
- "Create our reporting calendar and evidence collection plan from these award terms."
- "Give me a weekly grant operations review with deadlines, blocked work, decisions, and risks."

### Reporting and changes

- "Build a reporting workbench for this quarterly report and identify the evidence we still need."
- "Draft an amendment request based on this program change, but do not assume funder approval is not required."
- "Compare our performance evidence against the claims in this report before leadership approves it."

### Renewal and closeout

- "Create a renewal readiness brief using this award's actual performance and current funder guidance."
- "Build a closeout plan from the award terms and show what is still unresolved."
- "Give leadership a portfolio review across all active grants, applications, reports, renewals, and closeouts."

## Reusable operating templates

The plugin includes reusable structures in `references/GRANT_OPS_TEMPLATES.md`, including:

- Grant Pipeline
- Grant Qualification Brief
- Requirements and Evidence Matrix
- Application Operating Plan
- Evidence-to-Claim Map
- Budget Consistency Review
- Submission Readiness Gate
- Award Acceptance Brief
- Obligations Register
- Award Kickoff Pack
- Reporting Workbench
- Grant Change Record
- Renewal Readiness Brief
- Closeout Plan
- Weekly Grant Operations Review
- Monthly Portfolio Review
- Leadership Brief

These are designed as operating artifacts, not decorative templates. Claude should adapt them to the evidence and task at hand rather than filling unknown fields with guesses.

## Authority and safety boundaries

The plugin may analyze, organize, compare, draft, plan, identify gaps, prepare materials, and recommend next actions.

It does **not** independently determine or invent:

- eligibility
- deadlines or time zones
- match or cost-share requirements
- allowable costs
- indirect-cost treatment
- certifications
- award terms
- reporting obligations
- renewal conditions
- program outcomes
- demographic claims
- partner commitments
- compliance status

Explicit human authorization is required to submit an application or report, certify compliance or accuracy, accept award terms, sign representations, alter approved budgets, commit match funds, enter binding commitments, make material funder commitments, or change bank or payment information.

Legal, regulatory, tax, audit, accounting, procurement, and employment determinations remain with qualified humans.

When something is missing, stale, unsupported, or in conflict, the plugin is written to surface the exception rather than guess.

## Data handling

Share only the organizational and program information a task needs. Avoid pasting passwords, bank credentials, or donor and beneficiary data that the task does not require.

The plugin itself does not collect data, store data, send data to Revuity, or operate an external service. It relies only on the information you provide and the tools or connectors you have already enabled in your own Claude environment.

## Install

This repository is a single Claude plugin with its manifest at `.claude-plugin/plugin.json` and its skill at `skills/grant-operations/SKILL.md`.

To try it locally, clone the repository and start Claude Code with the plugin directory:

```bash
git clone https://github.com/revuitysystems/revuity-nonprofit-grant-operations.git
claude --plugin-dir ./revuity-nonprofit-grant-operations
```

Then confirm `/nonprofit-grant-operations:grant-operations` appears. To check the package without running it, use:

```bash
claude plugin validate ./revuity-nonprofit-grant-operations --strict
```

## Validation

A GitHub Actions workflow in this repository checks the manifest, semantic version, skill frontmatter, and required documentation on every push and pull request.

Passing structural validation means the package is well formed. Runtime behavior should also be smoke-tested after material skill changes and before directory submission.

## Built by Revuity Systems

Revuity Systems is an Operations Systems company. These public workflow plugins are free operating tools designed to make real work easier while demonstrating how Revuity thinks about roles, workflows, responsibility, authority, exceptions, outcomes, and operating cadence.

When an organization later needs the workflow adapted to its own systems, policies, data, approvals, integrations, or operating model, Revuity may help design or build that larger system. You do not need to talk to anyone to use this plugin.

More at [revuitysystems.com](https://revuitysystems.com). Questions or security concerns: info@revuitysystems.com.

## Privacy

This plugin does not collect or store data itself. Revuity's privacy policy is at [revuitysystems.com/privacy](https://revuitysystems.com/privacy).

## License

MIT. See [LICENSE](LICENSE).
