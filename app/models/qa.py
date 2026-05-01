from pydantic import BaseModel


class QAEvaluationRequest(BaseModel):
    user_message: str
    agent_response: str
    channel: str = "webchat"


class QAEvaluationResponse(BaseModel):
    quality_score: float
    compliance_score: float
    conversion_score: float
    risk_flags: list[str]
    summary: str
