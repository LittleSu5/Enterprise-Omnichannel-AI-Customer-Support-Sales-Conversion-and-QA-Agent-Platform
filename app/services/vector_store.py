from __future__ import annotations

import json
from pathlib import Path


class MockVectorStore:
    def __init__(self, data_dir: str = "data") -> None:
        base = Path(__file__).resolve().parents[2] / data_dir
        with open(base / "faq.json", "r", encoding="utf-8") as f:
            self.faq = json.load(f)
        with open(base / "policies.json", "r", encoding="utf-8") as f:
            self.policies = json.load(f)

    def search(self, query: str) -> list[dict]:
        query_lower = query.lower()
        results: list[dict] = []
        for item in self.faq + self.policies:
            haystack = f"{item.get('title', '')} {item.get('content', '')}".lower()
            if any(token in haystack for token in query_lower.split() if token):
                results.append(item)
        return results[:5] or (self.faq + self.policies)[:3]
