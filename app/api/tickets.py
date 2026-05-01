from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ticket_service import TicketService

router = APIRouter(prefix="/api/tickets", tags=["tickets"])
ticket_service = TicketService()


class CreateTicketRequest(BaseModel):
    user_id: str
    subject: str
    details: str


@router.post("/create")
def create_ticket(payload: CreateTicketRequest) -> dict:
    return ticket_service.create_ticket(payload.user_id, payload.subject, payload.details)
