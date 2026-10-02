"""Lightweight structural validation for a single Claude plugin repository."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
MIN_README_CHARS = 2500


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


def main(expected):
    manifest_path = ROOT / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        fail(".claude-plugin/plugin.json missing")
    manifest = json.loads(manifest_path.read_text())
    if manifest.get("name") != expected:
        fail(f"plugin name {manifest.get('name')!r} != expected {expected!r}")
    if not NAME.match(manifest["name"]):
        fail("invalid plugin name")
    if not SEMVER.match(str(manifest.get("version", ""))):
        fail("version is not valid semver")
    for key in ("description", "author", "homepage", "license", "keywords"):
        if not manifest.get(key):
            fail(f"manifest missing {key}")
    icon = manifest.get("icon")
    if icon and not (ROOT / icon).is_file():
        fail(f"manifest icon {icon!r} does not exist")
    skills = list((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        fail("no skills/*/SKILL.md found")
    for skill in skills:
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
        low = text.lower()
        if not any(x in low for x in ("authority", "authorization", "human")):
            fail(f"{skill}: no authority boundary stated")
    readme = ROOT / "README.md"
    if not readme.exists() or len(readme.read_text()) < MIN_README_CHARS:
        fail(f"README.md missing or shorter than {MIN_README_CHARS} characters")
    for f in ("SECURITY.md", "LICENSE", "CHANGELOG.md"):
        if not (ROOT / f).exists():
            fail(f"missing {f}")
    print(f"PASS: {manifest['name']} {manifest['version']} validated")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: validate.py <expected-plugin-name>")
    try:
        main(sys.argv[1])
    except Exception as e:
        print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
