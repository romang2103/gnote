from datetime import date, timedelta
from pathlib import Path
from worknote.files import path_for, ensure_note_file, append_quick_entry, collect_files

# path_for
print(path_for(date(2025, 10, 18)))

# ensure_note_file
p = ensure_note_file(date(2025, 10, 18))
assert p.exists()

# append_quick_entry
append_quick_entry(p, "Wired up auth middleware")
print(p.read_text(encoding="utf-8"))

# collect_files
start = date(2025, 10, 1)
end = date(2025, 10, 31)
files = collect_files(start, end)
print([f for f in files])
