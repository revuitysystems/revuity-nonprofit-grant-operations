# Changelog

## Unreleased

- Added plugin icon assets (`assets/icon.png` and 512, 256, 128 pixel versions), an `icon` manifest field for the Anthropic directory listing, and a README icon section. No change to plugin behavior.

## 1.0.0 — Initial public release

- Initial public release of Nonprofit Grant Operations as a standalone plugin repository.
- Added the `nonprofit-grant-operations` plugin with the `grant-operations` skill covering opportunity triage, application readiness, budget and narrative consistency checks, submission readiness, post-award reporting, and portfolio review.
- Includes source-discipline rules against inferred eligibility, deadlines, and compliance obligations.
- Includes explicit authorization boundaries for submissions, certifications, term acceptance, budget changes, match commitments, and funder commitments.
- Added a GitHub Actions workflow that validates the manifest, semantic version, skill frontmatter, and required documentation.

### Verification

Package validation runs in GitHub Actions. This release has not been installed or exercised in a user's Claude runtime by its authors; smoke-test the plugin in your own Claude environment after installing it.
