from pydantic import BaseModel


class MetricCard(BaseModel):
    label: str
    value: str
    trend: str
    delta: str


class DashboardResponse(BaseModel):
    cards: list[MetricCard]
    daily_usage: list[dict]
