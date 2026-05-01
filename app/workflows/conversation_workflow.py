from __future__ import annotations

from app.agents.execution_agent import ExecutionAgent
from app.agents.intent_agent import IntentAgent
from app.agents.profile_agent import ProfileAgent
from app.agents.qa_agent import QAAgent
from app.agents.response_agent import ResponseAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.summary_agent import SummaryAgent
from app.models.chat import AgentTrace, ChatResponse
from app.services.order_service import OrderService


class ConversationWorkflow:
    def __init__(self) -> None:
        self.intent_agent = IntentAgent()
        self.profile_agent = ProfileAgent()
        self.retrieval_agent = RetrievalAgent()
        self.response_agent = ResponseAgent()
        self.execution_agent = ExecutionAgent()
        self.qa_agent = QAAgent()
        self.summary_agent = SummaryAgent()
        self.order_service = OrderService()

    def run(self, user_id: str, message: str, history: list[str]) -> ChatResponse:
        traces: list[AgentTrace] = []
        total_input_tokens = 0
        total_output_tokens = 0

        intent_result = self.intent_agent.run(message)
        traces.append(AgentTrace(agent="intent_agent", summary=f"intent={intent_result['intent']}"))

        profile_result = self.profile_agent.run(user_id)
        traces.append(AgentTrace(agent="profile_agent", summary=f"tier={profile_result['profile']['tier']}"))

        retrieval_query = " ".join([message, *history])
        retrieval_result = self.retrieval_agent.run(retrieval_query)
        traces.append(AgentTrace(agent="retrieval_agent", summary=f"docs={retrieval_result['document_count']}"))

        order = self.order_service.get_latest_order(user_id) if intent_result["intent"] == "order_status" else None
        response_result = self.response_agent.run(
            intent=intent_result["intent"],
            profile=profile_result["profile"],
            documents=retrieval_result["documents"],
            user_message=message,
            order=order,
        )
        total_input_tokens += response_result["input_tokens"]
        total_output_tokens += response_result["output_tokens"]
        traces.append(AgentTrace(agent="response_agent", summary=f"action={response_result['recommended_action']}"))

        execution_result = self.execution_agent.run(
            user_id=user_id,
            action=response_result["recommended_action"],
            response_text=response_result["response_text"],
        )
        traces.append(AgentTrace(agent="execution_agent", summary=f"ticket_created={bool(execution_result['ticket'])}"))

        qa_result = self.qa_agent.run(message, response_result["response_text"])
        traces.append(AgentTrace(agent="qa_agent", summary=f"quality={qa_result['quality_score']}"))

        summary_result = self.summary_agent.run(message, response_result["response_text"])
        traces.append(AgentTrace(agent="summary_agent", summary=summary_result["summary"]))

        ticket_id = execution_result["ticket"]["ticket_id"] if execution_result["ticket"] else None
        return ChatResponse(
            response_text=response_result["response_text"],
            detected_intent=intent_result["intent"],
            recommended_action=response_result["recommended_action"],
            qa_score=qa_result["quality_score"],
            sales_opportunity_score=profile_result["sales_opportunity_score"],
            ticket_id=ticket_id,
            traces=traces,
            token_usage={
                "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens,
                "total_tokens": total_input_tokens + total_output_tokens,
            },
        )
