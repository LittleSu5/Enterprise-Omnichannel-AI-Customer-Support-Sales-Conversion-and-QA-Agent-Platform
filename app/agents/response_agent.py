from __future__ import annotations

from app.services.llm import MockLLMService


class ResponseAgent:
    def __init__(self) -> None:
        self.llm = MockLLMService()

    def run(self, intent: str, profile: dict, documents: list[dict], user_message: str, order: dict | None = None) -> dict:
        context = {
            "intent": intent,
            "profile": profile,
            "documents": documents,
            "user_message": user_message,
            "order": order,
        }
        prompt = f"Generate enterprise-grade support response using context: {context}"
        llm_result = self.llm.complete(prompt, max_output_tokens=280)

        if intent == "order_status" and order:
            response_text = (
                f"您好，已为您查询到订单 {order['order_id']} 当前状态为 {order['status']}，"
                f"预计发货时间为 {order['estimated_ship_date']}。"
                "如果您希望，我也可以为您登记催发货并补充一张关怀优惠券。"
            )
            action = "offer_shipping_followup"
        elif intent == "sales_opportunity":
            response_text = (
                f"结合您的使用情况，当前更适合 {profile.get('tier', 'standard')} 客户的升级方案。"
                "我可以为您整理套餐差异并发起专属优惠跟进。"
            )
            action = "sales_followup"
        elif intent == "refund_request":
            response_text = "已理解您的退款诉求，我可以先帮您核对订单与退款条件，并创建售后工单跟进。"
            action = "create_refund_ticket"
        else:
            response_text = "已收到您的问题，我将结合知识库与您的历史记录为您给出处理建议。"
            action = "general_answer"

        return {
            "response_text": response_text,
            "recommended_action": action,
            "input_tokens": llm_result.input_tokens,
            "output_tokens": llm_result.output_tokens,
        }
