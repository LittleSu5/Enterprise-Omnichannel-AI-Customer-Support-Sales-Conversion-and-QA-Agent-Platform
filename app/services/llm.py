from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLMResult:
    text: str
    input_tokens: int
    output_tokens: int


class MockLLMService:
    """Deterministic mock LLM used to emulate platform behavior."""

    def complete(self, prompt: str, max_output_tokens: int = 256) -> LLMResult:
        input_tokens = max(80, len(prompt) // 2)
        output_tokens = min(max_output_tokens, max(60, len(prompt) // 8))
        text = (
            "[MockLLM] "
            + prompt[:180].replace("\n", " ")
            + ("..." if len(prompt) > 180 else "")
        )
        return LLMResult(text=text, input_tokens=input_tokens, output_tokens=output_tokens)
