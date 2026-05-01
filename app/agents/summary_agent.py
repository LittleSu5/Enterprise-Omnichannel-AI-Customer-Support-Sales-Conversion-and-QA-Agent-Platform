from __future__ import annotations


class SummaryAgent:
    def run(self, message: str, response_text: str) -> dict:
        return {
            "summary": f"用户问题摘要：{message[:40]}；处理结果摘要：{response_text[:60]}"
        }
