from typing import List, Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    channel: str = Field(..., examples=["webchat"])
    user_id: str = Field(..., examples=["cust_001"])
    message: str
    conversation_history: List[str] = Field(default_factory=list)
    metadata: dict = Field(default_factory=dict)


class AgentTrace(BaseModel):
    agent: str
    summary: str


class ChatResponse(BaseModel):
    response_text: str
    detected_intent: str
    recommended_action: str
    qa_score: float
    sales_opportunity_score: float
    ticket_id: Optional[str] = None
    traces: List[AgentTrace]
    token_usage: dict


class SalesFollowupRequest(BaseModel):
    user_id: str
    campaign_name: str
    objective: str
    recent_activity: List[str] = Field(default_factory=list)


class SalesFollowupResponse(BaseModel):
    followup_message: str
    sales_opportunity_score: float
    next_best_action: str
    traces: List[AgentTrace]
    token_usage: dict
