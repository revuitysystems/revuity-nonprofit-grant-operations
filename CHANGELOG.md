# Changelog

## Unreleased

- Added `SUBMISSION_READINESS.md` recording validation, runtime load, and invocation results. No change to plugin behavior.
- Added a privacy policy link to the manifest and README.
- Added `displayName` to the manifest and `SUBMISSION.md` for the directory submission. Switched the README icon to Markdown image syntax. No change to plugin behavior.
- Added the plugin icon files, an icon field in the manifest for the Anthropic directory listing, and a README icon section. No change to plugin behavior.

## 1.0.0 — Initial public release

- Initial public release of Nonprofit Grant Operations as a standalone plugin repository.
- Added the `nonprofit-grant-operations` plugin with the `grant-operations` skill covering opportunity triage, application readiness, budget and narrative consistency checks, submission readiness, post-award reporting, and portfolio review.
- Includes source-discipline rules against inferred eligibility, deadlines, and compliance obligations.
- Includes explicit authorization boundaries for submissions, certifications, term acceptance, budget changes, match commitments, and funder commitments.
- Added a GitHub Actions workflow that validates the manifest, semantic version, skill frontmatter, and required documentation.

### Verification

Package validation runs in GitHub Actions. This release has not been installed or exercised in a user's Claude runtime by its authors; smoke-test the plugin in your own Claude environment after installing it.
