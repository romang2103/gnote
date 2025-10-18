"""
Handles filesystem operations:
- Where notes are stored
- Creation, reading, and appending
"""
from __future__ import annotations
from pathlib import Path
from datetime import date, datetime
from .config import notes_root
import calendar

HEADER = """# {date} — Daily Notes

## What I worked on
-

## Blockers
-

## Next up
-
"""



def path_for(d: date) -> Path:
    """Return the expected file path for a given date."""
    root = notes_root()
    year = f"{d.year}"
    month = f"{d.strftime("%B")}"
    fname = f"{year}-{d.month}-{d.day}"
    return f"{root}/{year}/{month}/{fname}"

def path_for(d: date) -> Path:
    """
    Return the expected file path for a given date.

    Structure:
      <ROOT>/<YYYY>/<MonthName>/<YYYY-MM-DD>.md
    """
    root: Path = notes_root()               # Path
    year_dir = root / f"{d.year}"           # Path
    month_dir = year_dir / d.strftime("%B") # Path
    fname = f"{d.isoformat()}.md"           # 'YYYY-MM-DD.md'
    return month_dir / fname                # Path
    


def ensure_note_file(d: date) -> Path:
    """Ensure a note file exists for the date; create it if missing."""
    fpath = path_for(d)
    fpath.parent.mkdir(parents=True, exist_ok=True)
    if not fpath.exists():
        fpath.write_text(HEADER.format(date=d.isoformat()), encoding="utf-8")
    return fpath

def append_quick_entry(path: Path, text: str) -> None:
    """Append a timestamped quick entry to a note file."""
    if path.exists():
        content = path.read_text(encoding="utf-8")
    else:
        # Seed a new file if missing
        content = HEADER.format(date=path.stem)
    
    lines = content.splitlines()
    try:
        idx = lines.index('## What I worked on')
        insert_at = idx + 1
        # skip blanks/bullets so entries stay grouped
        while insert_at < len(lines) and lines[insert_at].strip().startswith("-"):
            insert_at += 1
        lines.insert(insert_at, f"- [{datetime.now().strftime('%H:%M')}] : {text}")
    except ValueError:
        # Section not found; append at end
        lines.append(f"- [{datetime.now().strftime('%H:%M')}] : {text}")
    
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def collect_files(start: date, end: date) -> list[Path]:
    """
    Collect all note files within the date range.
    Iterate only through relevant year/month folders for performance.
    """
    files: list[Path] = []
    root = notes_root()
    
    for year in range(start.year, end.year + 1):
        year_dir = root / f"{year}"
        if not year_dir.exists():
            continue

        m_start = 1 if year > start.year else start.month
        m_end = 12 if year < end.year else end.month
            
        for m in range(m_start, m_end + 1):
            month_name = calendar.month_name[m]
            month_dir = year_dir / month_name
            if not month_dir.exists():
                continue
                
            for f in sorted(month_dir.glob("*.md")):
                try:
                    d = date.fromisoformat(f.stem)
                except ValueError:
                    continue
                if start <= d <= end:
                    files.append(f)
    
    return files