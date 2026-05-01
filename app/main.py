from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.metrics import router as metrics_router
from app.api.qa import router as qa_router
from app.api.tickets import router as tickets_router

app = FastAPI(
    title="Enterprise Omnichannel AI Agent Platform",
    version="1.0.0",
    description="Demo platform for intelligent support, sales conversion, QA, and platform-scale metrics.",
)

app.include_router(chat_router)
app.include_router(qa_router)
app.include_router(tickets_router)
app.include_router(metrics_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "omni-agent-platform"}
