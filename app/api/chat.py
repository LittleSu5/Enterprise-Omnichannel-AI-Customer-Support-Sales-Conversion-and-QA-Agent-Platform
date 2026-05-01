from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse, SalesFollowupRequest, SalesFollowupResponse
from app.workflows.conversation_workflow import ConversationWorkflow
from app.workflows.sales_followup_workflow import SalesFollowupWorkflow

router = APIRouter(prefix="/api/chat", tags=["chat"])

conversation_workflow = ConversationWorkflow()
sales_followup_workflow = SalesFollowupWorkflow()


@router.post("/respond", response_model=ChatResponse)
def respond(payload: ChatRequest) -> ChatResponse:
    return conversation_workflow.run(
        user_id=payload.user_id,
        message=payload.message,
        history=payload.conversation_history,
    )


@router.post("/sales-followup", response_model=SalesFollowupResponse)
def sales_followup(payload: SalesFollowupRequest) -> SalesFollowupResponse:
    return sales_followup_workflow.run(
        user_id=payload.user_id,
        objective=payload.objective,
        recent_activity=payload.recent_activity,
    )
