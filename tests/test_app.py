from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_respond() -> None:
    payload = {
        "channel": "webchat",
        "user_id": "cust_001",
        "message": "我的订单为什么还没发货？如果今天发不了给我优惠券吧",
        "conversation_history": ["昨天问过物流状态"],
    }
    response = client.post("/api/chat/respond", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["detected_intent"] == "order_status"
    assert body["token_usage"]["total_tokens"] > 0


def test_metrics_dashboard() -> None:
    response = client.get("/api/metrics/dashboard")
    assert response.status_code == 200
    body = response.json()
    assert len(body["cards"]) >= 3
