# Enterprise Omnichannel AI Customer Support, Sales Conversion, and QA Agent Platform

A demo Python project for an enterprise-scale multi-agent platform covering customer support, sales follow-up, ticket handling, summaries, QA, and usage metrics.

## Features

- FastAPI service with chat, QA, ticket, and metrics endpoints
- Multi-agent orchestration for intent understanding, profile enrichment, retrieval, response generation, execution, QA, and summarization
- Mock CRM, order, ticket, and metrics services
- Dashboard-ready token usage metrics seeded to platform-scale numbers
- Simple tests for health and chat workflow

## Project structure

```
omni-agent-platform/
├── app/
│   ├── api/
│   ├── agents/
│   ├── models/
│   ├── services/
│   ├── workflows/
│   └── main.py
├── data/
├── tests/
├── requirements.txt
└── README.md
```

## Quick start

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the API docs at:

- `http://127.0.0.1:8000/docs`

## Main endpoints

- `GET /health`
- `POST /api/chat/respond`
- `POST /api/chat/sales-followup`
- `POST /api/qa/evaluate`
- `POST /api/tickets/create`
- `GET /api/metrics/dashboard`

## Example request

```bash
curl -X POST http://127.0.0.1:8000/api/chat/respond \
  -H "Content-Type: application/json" \
  -d '{
    "channel": "webchat",
    "user_id": "cust_001",
    "message": "我的订单为什么还没发货？如果今天发不了能不能给我优惠券？",
    "conversation_history": [
      "用户昨天咨询过物流状态",
      "客服回复仓库正在处理"
    ]
  }'
```

## Notes

This is a demo/starter intended for presentation, internal demos, and architecture illustration. It uses deterministic mock logic instead of real LLM APIs and business systems.
