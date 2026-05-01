from __future__ import annotations


class IntentAgent:
    def run(self, message: str) -> dict:
        message_lower = message.lower()
        if any(word in message_lower for word in ["退款", "退货", "refund"]):
            intent = "refund_request"
        elif any(word in message_lower for word in ["发货", "物流", "shipping", "order"]):
            intent = "order_status"
        elif any(word in message_lower for word in ["优惠", "套餐", "购买", "升级", "discount"]):
            intent = "sales_opportunity"
        else:
            intent = "general_support"
        return {"intent": intent, "confidence": 0.91}
