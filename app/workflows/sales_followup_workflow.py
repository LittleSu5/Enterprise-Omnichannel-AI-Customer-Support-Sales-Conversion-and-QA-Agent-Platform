from __future__ import annotations

from app.agents.profile_agent import ProfileAgent
from app.agents.response_agent import ResponseAgent
from app.models.chat import AgentTrace, SalesFollowupResponse


class SalesFollowupWorkflow:
    def __init__(self) -> None:
        self.profile_agent = ProfileAgent()
        self.response_agent = ResponseAgent()

    def run(self, user_id: str, objective: str, recent_activity: list[str]) -> SalesFollowupResponse:
        traces: list[AgentTrace] = []
        profile_result = self.profile_agent.run(user_id)
        traces.append(AgentTrace(agent="profile_agent", summary=f"tier={profile_result['profile']['tier']}"))

        response_result = self.response_agent.run(
            intent="sales_opportunity",
            profile=profile_result["profile"],
            documents=[{"title": "campaign_objective", "content": objective}, {"title": "recent_activity", "content": str(recent_activity)}],
            user_message=objective,
        )
        traces.append(AgentTrace(agent="response_agent", summary="generated follow-up"))

        return SalesFollowupResponse(
            followup_message=response_result["response_text"],
            sales_opportunity_score=profile_result["sales_opportunity_score"],
            next_best_action="assign_sales_rep" if profile_result["sales_opportunity_score"] > 0.8 else "send_coupon",
            traces=traces,
            token_usage={
                "input_tokens": response_result["input_tokens"],
                "output_tokens": response_result["output_tokens"],
                "total_tokens": response_result["input_tokens"] + response_result["output_tokens"],
            },
        )
