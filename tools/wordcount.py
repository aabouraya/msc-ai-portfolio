"""Count the words on each Intelligent Agents page.

Counted: everything a reader sees on the page that I wrote for it: the title,
summary, headings, prose, tables, figure captions and screenshot labels.
Reported separately: code blocks (the KQML messages and parse trees).
Not counted: reference lists, screenshots and the appendix, which holds only
original documents reproduced unchanged.

    python3 -I tools/wordcount.py
"""
import re
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "modules/intelligent-agents"
PAGES = [  # (file, label) in sub-navigation order
    ("index.md", "Overview"),
    ("team-project.md", "Team project"),
    ("evaluation.md", "Final project"),
    ("formative-activities.md", "Formative activities"),
    ("discussions.md", "Discussions"),
    ("case-studies.md", "Case studies"),
]
LIMIT_REST = 1500  # the reflective piece (1,000) is counted by the submission build
WORD = re.compile(r"\S*[A-Za-z0-9]\S*")


def words(text):
    text = re.sub(r"\]\([^)]*\)", "]", text)          # keep link text, drop URL
    text = re.sub(r"<https?://[^>]*>", "", text)      # bare URLs
    text = re.sub(r"<[^>]+>", " ", text)              # tags, with their attributes
    text = re.sub(r"[|*_`#>\[\]]", " ", text)         # markdown punctuation
    return len(WORD.findall(text))


def count(name):
    """Return (words, code words) for one page."""
    raw = (SITE / name).read_text()
    front = re.match(r"\A---\n(.*?)\n---\n", raw, flags=re.S)
    meta = front.group(1) if front else ""
    body = raw[front.end():] if front else raw

    title = re.search(r"^title:\s*(.*)$", meta, flags=re.M)
    summary = re.search(r"^summary:\s*>-\n((?:  .*\n?)+)", meta, flags=re.M)
    shown = (title.group(1).strip('"') if title else "") + " " + (summary.group(1) if summary else "")

    body = body.split("\n## References")[0]
    body = re.sub(r'<div class="references".*?</div>', "", body, flags=re.S)
    body = re.sub(r"\{%.*?%\}|\{\{.*?\}\}", "", body, flags=re.S)
    code = re.findall(r"^```.*?^```", body, flags=re.S | re.M)
    body = re.sub(r"^```.*?^```", "", body, flags=re.S | re.M)
    body = "\n".join(l for l in body.splitlines() if not re.fullmatch(r"[|:\- ]+", l.strip()))
    return words(shown + " " + body), sum(words(c.strip("`")) for c in code)


def main():
    rows = [(label, *count(name)) for name, label in PAGES]
    rest = sum(n for _, n, _ in rows)
    code = sum(c for _, _, c in rows)
    for label, n, c in rows:
        print(f"{n:5d}  {label}" + (f"  (+{c} code)" if c else ""))
    print(f"{rest:5d}  TOTAL (limit {LIMIT_REST}); with code {rest + code} (penalty above {LIMIT_REST * 11 // 10})")
    return 0 if rest <= LIMIT_REST else 1


if __name__ == "__main__":
    sys.exit(main())
