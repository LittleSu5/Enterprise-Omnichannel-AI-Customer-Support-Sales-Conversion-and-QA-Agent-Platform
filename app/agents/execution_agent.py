from __future__ import annotations

from app.services.crm_service import CRMService
from app.services.ticket_service import TicketService


class ExecutionAgent:
    def __init__(self) -> None:
        self.crm = CRMService()
        self.ticket_service = TicketService()

    def run(self, user_id: str, action: str, response_text: str) -> dict:
        note = self.crm.write_note(user_id, response_text)
        ticket = None
        if action in {"create_refund_ticket", "offer_shipping_followup"}:
            ticket = self.ticket_service.create_ticket(
                user_id=user_id,
                subject=action,
                details=response_text,
            )
        return {"crm_note": note, "ticket": ticket}
