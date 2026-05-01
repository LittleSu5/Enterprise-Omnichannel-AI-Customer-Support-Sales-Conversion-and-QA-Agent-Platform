from __future__ import annotations

from app.agents.qa_agent import QAAgent
from app.models.qa import QAEvaluationResponse


class QAWorkflow:
    def __init__(self) -> None:
        self.qa_agent = QAAgent()

    def run(self, user_message: str, agent_response: str) -> QAEvaluationResponse:
        result = self.qa_agent.run(user_message, agent_response)
        return QAEvaluationResponse(**result)
