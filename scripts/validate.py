"""Production structural validation for the Nonprofit Grant Operations Claude plugin."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
MIN_README_CHARS = 4000
REQUIRED_MANIFEST_KEYS = (
    "name", "displayName", "version", "description", "author", "homepage",
    "privacyPolicyUrl", "license", "keywords", "repository", "icon",
)
REQUIRED_SKILL_SECTIONS = (
    "# 1. Grant pipeline and opportunity intake",
    "# 2. Qualification and go/no-go decision support",
    "# 3. Application operating plan",
    "# 8. Submission control",
    "# 9. Award review and acceptance",
    "# 10. Award kickoff and implementation setup",
    "# 12. Reporting workbench",
    "# 14. Change control and amendments",
    "# 15. Renewal and continuation planning",
    "# 16. Closeout",
    "# 17. Portfolio and leadership review",
    "# 18. Operating cadence",
    "# 19. Exceptions and escalation",
    "# 20. Authority boundary",
)
REQUIRED_BOUNDARY_PHRASES = (
    "never infer eligibility",
    "submission itself requires explicit human authorization",
    "never certify compliance or performance without authoritative evidence and human approval",
    "explicit human authorization is required to",
    "change bank or payment information",
)


def fail(msg):
    raise AssertionError(msg)


def frontmatter(text):
    if not text.startswith("---\n"):
        fail("SKILL.md missing opening frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md missing closing frontmatter")
    out = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def require_contains(text, needle, label):
    if needle not in text:
        fail(f"{label} missing required content: {needle}")


def main(expected):
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        fail(".claude-plugin/plugin.json missing")
    manifest = json.loads(manifest_path.read_text())
    for key in REQUIRED_MANIFEST_KEYS:
        if not manifest.get(key):
            fail(f"manifest missing {key}")
    if manifest["name"] != expected:
        fail(f"plugin name {manifest['name']!r} != expected {expected!r}")
    if not NAME.match(manifest["name"]):
        fail("invalid plugin name")
    if not SEMVER.match(str(manifest["version"])):
        fail("version is not valid semver")
    if not str(manifest["privacyPolicyUrl"]).startswith("https://"):
        fail("privacyPolicyUrl must use https")
    icon_path = ROOT / str(manifest["icon"]).lstrip("./")
    if not icon_path.exists():
        fail(f"manifest icon not found: {manifest['icon']}")

    skills = list((ROOT / "skills").glob("*/SKILL.md"))
    if len(skills) != 1:
        fail(f"expected exactly one skill, found {len(skills)}")
    skill = skills[0]
    text = skill.read_text()
    fm = frontmatter(text)
    if not NAME.match(fm.get("name", "")):
        fail(f"{skill}: invalid skill name")
    if fm["name"] != skill.parent.name:
        fail(f"{skill}: skill name does not match its directory")
    desc = fm.get("description", "")
    if not desc or len(desc) > 1024:
        fail(f"{skill}: missing or oversize description")
    if not desc.startswith("This skill should be used"):
        fail(f"{skill}: description should begin 'This skill should be used'")
    for section in REQUIRED_SKILL_SECTIONS:
        require_contains(text, section, "SKILL.md")
    low = text.lower()
    for phrase in REQUIRED_BOUNDARY_PHRASES:
        require_contains(low, phrase, "SKILL.md safety contract")

    templates = ROOT / "references" / "GRANT_OPS_TEMPLATES.md"
    if not templates.exists() or len(templates.read_text()) < 2500:
        fail("references/GRANT_OPS_TEMPLATES.md missing or too small")
    require_contains(text, "references/GRANT_OPS_TEMPLATES.md", "SKILL.md")

    readme = ROOT / "README.md"
    if not readme.exists() or len(readme.read_text()) < MIN_README_CHARS:
        fail(f"README.md missing or shorter than {MIN_README_CHARS} characters")
    readme_text = readme.read_text()
    require_contains(readme_text, manifest["version"], "README.md")
    require_contains(readme_text, "https://revuitysystems.com/privacy", "README.md")

    submission = ROOT / "SUBMISSION.md"
    readiness = ROOT / "SUBMISSION_READINESS.md"
    for f in (submission, readiness):
        if not f.exists():
            fail(f"missing {f.name}")
    require_contains(submission.read_text(), manifest["version"], "SUBMISSION.md")
    require_contains(readiness.read_text(), manifest["version"], "SUBMISSION_READINESS.md")

    for f in ("SECURITY.md", "LICENSE", "CHANGELOG.md"):
        if not (ROOT / f).exists():
            fail(f"missing {f}")

    print(f"PASS: {manifest['name']} {manifest['version']} production contract validated")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: validate.py <expected-plugin-name>")
    try:
        main(sys.argv[1])
    except Exception as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
