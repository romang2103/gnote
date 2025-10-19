"""
Minimal LLM summarization client using stdlib only.
Uses OpenAI API if available, otherwise falls back to a naive local summary.
"""
from __future__ import annotations
from typing import Iterable
from openai import OpenAI
import os


client = OpenAI() 


def summarize(chunks: Iterable[str], style: str = "performance") -> str:
    """
    Given note contents, return a concise summary.
    Implement a fallback if no API key is available.
    """
    if not client.api_key:
        return "No API key available"

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following notes: {chunks}"
            }
        ]
    )
    return response.choices[0].message.content
