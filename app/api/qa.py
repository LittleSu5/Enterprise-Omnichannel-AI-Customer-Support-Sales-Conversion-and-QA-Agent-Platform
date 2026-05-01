from fastapi import APIRouter

from app.models.qa import QAEvaluationRequest, QAEvaluationResponse
from app.workflows.qa_workflow import QAWorkflow

router = APIRouter(prefix="/api/qa", tags=["qa"])
workflow = QAWorkflow()


@router.post("/evaluate", response_model=QAEvaluationResponse)
def evaluate(payload: QAEvaluationRequest) -> QAEvaluationResponse:
    return workflow.run(payload.user_message, payload.agent_response)
