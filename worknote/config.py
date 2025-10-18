# worknote/config.py

from __future__ import annotations
import os
from pathlib import Path

def notes_root() -> Path:
    """Return the root directory for all notes"""
    env = os.environ.get("WORKNOTE_DIR")
    if env:
        return Path(env).expanduser()
    # Default: ~/Documents/Worknotes
    return Path.home() / "Documents" / "Worknotes"


def model_name() -> str:
    """Return the model name for summaries."""
    return os.environ.get("WORKNOTE_MODEL", "gpt-4o-mini")


def api_key() -> str | None:
    """Return the API key for LLM provider."""
    return os.environ.get("OPENAI_API_KEY")