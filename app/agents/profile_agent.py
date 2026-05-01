from __future__ import annotations

from app.services.crm_service import CRMService


class ProfileAgent:
    def __init__(self) -> None:
        self.crm = CRMService()

    def run(self, user_id: str) -> dict:
        customer = self.crm.get_customer(user_id)
        score = 0.85 if customer.get("tier") in {"vip", "enterprise"} else 0.62
        return {"profile": customer, "sales_opportunity_score": score}
