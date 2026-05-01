from __future__ import annotations

from datetime import datetime


class TicketService:
    def create_ticket(self, user_id: str, subject: str, details: str) -> dict:
        ticket_id = f"TKT-{user_id[-3:]}-{datetime.utcnow().strftime('%H%M%S')}"
        return {
            "ticket_id": ticket_id,
            "user_id": user_id,
            "subject": subject,
            "details": details,
            "status": "open",
        }
