"""
Minimal LLM summarization client using stdlib only.
Uses OpenAI API if available, otherwise falls back to a naive local summary.
"""
from __future__ import annotations
from typing import Iterable


def summarize(chunks: Iterable[str], style: str = "performance") -> str:
    """
    Given note contents, return a concise summary.
    Implement a fallback if no API key is available.
    """
    pass
