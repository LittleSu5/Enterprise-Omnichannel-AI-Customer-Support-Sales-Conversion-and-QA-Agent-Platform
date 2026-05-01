from __future__ import annotations


class QAAgent:
    def run(self, user_message: str, response_text: str) -> dict:
        quality_score = 0.95 if len(response_text) > 30 else 0.78
        compliance_score = 0.97 if "保证" not in response_text else 0.82
        conversion_score = 0.88 if "优惠" in response_text or "升级" in response_text else 0.71
        risk_flags = []
        if "一定" in response_text:
            risk_flags.append("absolute_claim")
        return {
            "quality_score": quality_score,
            "compliance_score": compliance_score,
            "conversion_score": conversion_score,
            "risk_flags": risk_flags,
            "summary": "Response is acceptable for demo QA workflow.",
        }
