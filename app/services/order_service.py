class OrderService:
    def get_latest_order(self, user_id: str) -> dict:
        return {
            "user_id": user_id,
            "order_id": f"ORD-{user_id[-3:]}-2025",
            "status": "processing",
            "estimated_ship_date": "2026-05-03",
            "has_delay_risk": True,
        }
