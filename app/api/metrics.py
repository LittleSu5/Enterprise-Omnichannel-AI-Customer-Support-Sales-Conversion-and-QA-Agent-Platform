from fastapi import APIRouter

from app.models.metrics import DashboardResponse
from app.services.metrics_service import MetricsService

router = APIRouter(prefix="/api/metrics", tags=["metrics"])
metrics_service = MetricsService()


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard() -> DashboardResponse:
    return DashboardResponse(**metrics_service.dashboard())
