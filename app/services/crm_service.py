from __future__ import annotations

from pathlib import Path
import json


class CRMService:
    def __init__(self, data_dir: str = "data") -> None:
        base = Path(__file__).resolve().parents[2] / data_dir
        with open(base / "mock_customers.json", "r", encoding="utf-8") as f:
            self.customers = {row["user_id"]: row for row in json.load(f)}

    def get_customer(self, user_id: str) -> dict:
        return self.customers.get(
            user_id,
            {
                "user_id": user_id,
                "name": "Unknown User",
                "tier": "standard",
                "lifetime_value": 0,
                "tags": ["new"],
                "preferred_channel": "webchat",
            },
        )

    def write_note(self, user_id: str, note: str) -> dict:
        return {"user_id": user_id, "note_saved": True, "note_preview": note[:120]}
