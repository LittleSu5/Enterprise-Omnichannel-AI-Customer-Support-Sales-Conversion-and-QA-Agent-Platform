from __future__ import annotations


class MetricsService:
    def dashboard(self) -> dict:
        return {
            "cards": [
                {"label": "今日总用量", "value": "124.8M tokens", "trend": "较昨日", "delta": "+28.7%"},
                {"label": "本周用量", "value": "682.4M tokens", "trend": "较上周", "delta": "+32.3%"},
                {"label": "本月累计", "value": "1.28B tokens", "trend": "较上月", "delta": "+19.6%"},
                {"label": "输入 Tokens", "value": "745.3M tokens", "trend": "占比", "delta": "58.2%"},
                {"label": "输出 Tokens", "value": "502.6M tokens", "trend": "占比", "delta": "39.2%"},
                {"label": "缓存命中", "value": "92.4%", "trend": "命中率", "delta": "稳定"},
                {"label": "请求次数", "value": "18,472 次", "trend": "较昨日", "delta": "+21.4%"},
            ],
            "daily_usage": [
                {"date": "2026-04-25", "tokens": 102_400_000},
                {"date": "2026-04-26", "tokens": 111_700_000},
                {"date": "2026-04-27", "tokens": 116_300_000},
                {"date": "2026-04-28", "tokens": 121_900_000},
                {"date": "2026-04-29", "tokens": 124_800_000},
                {"date": "2026-04-30", "tokens": 128_200_000},
                {"date": "2026-05-01", "tokens": 132_900_000},
            ],
        }
