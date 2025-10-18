"""
Command-line entry points.
Scripts:
- note: open or append today's note
- notesum: aggregate and summarize notes
"""
from __future__ import annotations


def cmd_note():
    import argparse
    import subprocess
    from datetime import date as _date
    from .dates import today, parse_date
    from .files import ensure_note_file, append_quick_entry

    parser = argparse.ArgumentParser(
        prog="note",
        description="Open today's work note in Notepad or quick-capture an entry."
    )
    parser.add_argument("--date", help="YYYY-MM-DD (default: today)")
    parser.add_argument("--yesterday", action="store_true", help="Open yesterday's note")
    # If any positional words are provided, treat them as a quick-capture entry.
    parser.add_argument(
        "add",
        nargs="*",
        help="Quick-capture text; if present, appends to today's note and does not open Notepad."
    )
    args = parser.parse_args()

    # Resolve target date (priority: --date > --yesterday > today)
    d = today()
    if args.date:
        d = parse_date(args.date)
    elif args.yesterday:
        d = _date.fromordinal(d.toordinal() - 1)

    path = ensure_note_file(d)

    # Quick-capture mode
    if args.add:
        text = " ".join(args.add).strip()
        if text:
            append_quick_entry(path, text)
            print(f"Added to {path}")
        return

    # Open in Windows Notepad; non-blocking
    try:
        subprocess.Popen(["notepad.exe", str(path)])
    except FileNotFoundError:
        # Fallback: just print the path so the user can open it manually
        print(f"Could not launch Notepad. File is at: {path}")


def cmd_notesum():
    import argparse
    from pathlib import Path
    from .dates import today, parse_date, parse_last, human_range
    from .files import collect_files

    parser = argparse.ArgumentParser(
        prog="notesum",
        description="Aggregate a date range of notes and summarize with an LLM (or naive fallback)."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--from", dest="from_", help="Start date YYYY-MM-DD")
    group.add_argument("--last", help="Relative period like 7d, 2w, 1m")
    parser.add_argument("--to", help="End date YYYY-MM-DD (default: today)")
    parser.add_argument(
        "--style",
        choices=["performance", "reflective", "bullets"],
        default="performance",
        help="Summary style (default: performance)"
    )
    parser.add_argument("--out", help="Write summary to this file (optional)")
    args = parser.parse_args()

    # Compute date range
    if args.last:
        start, end = parse_last(args.last)
    else:
        start = parse_date(args.from_)
        end = parse_date(args.to) if args.to else today()

    files = collect_files(start, end)
    if not files:
        print("No notes found in selected range.")
        return

    # Read each file once and build chunks
    chunks: list[str] = []
    for f in files:
        try:
            txt = f.read_text(encoding="utf-8")
        except Exception as e:  # don't crash on a single bad file
            txt = f"(read error: {e})"
        chunks.append(f"# {f.stem}\n\n{txt}")

    # Lazy import keeps cold start fast for other commands
    from .llm import summarize
    summary = summarize(chunks, style=args.style)

    print(f"\n=== Summary ({human_range(start, end)}) [{len(files)} notes] ===\n")
    print(summary)

    if args.out:
        Path(args.out).write_text(summary, encoding="utf-8")
        print(f"\nWrote {args.out}")
