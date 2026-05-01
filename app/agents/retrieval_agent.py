from __future__ import annotations

from app.services.vector_store import MockVectorStore


class RetrievalAgent:
    def __init__(self) -> None:
        self.store = MockVectorStore()

    def run(self, query: str) -> dict:
        docs = self.store.search(query)
        return {"documents": docs, "document_count": len(docs)}
