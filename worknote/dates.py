"""
Date utilities for note naming and aggregation.
"""
from __future__ import annotations
from datetime import datetime, date, timedelta
import re
# You may also need: datetime, timedelta, re


def today() -> date:
    """Return today's date."""
    return date.today()


def parse_date(s: str) -> date:
    """Parse a date string like '2025-10-18' into a date object."""
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()

def parse_last(expr: str) -> tuple[date, date]:
    """
    Parse a relative time expression like '7d', '2w', or '1m' into a (start, end) range.
    'm' can be approximated as 30 days.
    """
    expr = expr.strip().lower()

    # Match something like "7d", "2w", or "1m"
    match = re.fullmatch(r"(\d+)\s*([dwm])", expr)
    if not match:
        raise ValueError(f"Invalid expression: {expr!r} (expected like '7d', '2w', or '1m')")

    number, unit = match.groups()
    number = int(number)

    # Convert to days
    if unit == "d":
        delta = number
    elif unit == "w":
        delta = number * 7
    elif unit == "m":
        delta = number * 30

    end = date.today()
    start = end - timedelta(days=delta)

    return start, end

def human_range(start: date, end: date) -> str:
    """Return a human-readable representation of a date range."""
    # Case 1: Same day
    if start == end:
        return start.strftime("%Y-%m-%d")

    # Case 2: Same month and year (e.g., 2025-10-01 → 2025-10-07)
    if start.year == end.year and start.month == end.month:
        return f"{start.strftime('%b %d')}–{end.strftime('%d, %Y')}"

    # Case 3: Same year but different months
    if start.year == end.year:
        return f"{start.strftime('%b %d')}–{end.strftime('%b %d, %Y')}"

    # Case 4: Different years
    return f"{start.strftime('%b %d, %Y')}–{end.strftime('%b %d, %Y')}"
