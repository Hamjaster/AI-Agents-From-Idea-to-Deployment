"""FAISS-backed Retrieval-Augmented Generation tool for local knowledge lookup."""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from langchain.docstore.document import Document
from langchain.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


class LocalRAGTool(BaseTool):
    name = "local_rag_search"
    description = (
        "Access the local FAISS vector store built from workshop materials. "
        "Use this to retrieve background information, code snippets, and deployment tips."
    )

    def __init__(self, *, vectorstore_path: Path, top_k: int = 4, embedding_model: str = DEFAULT_EMBEDDING_MODEL) -> None:
        super().__init__()
        self.vectorstore_path = Path(vectorstore_path)
        self.top_k = top_k
        self.embedding_model = embedding_model
        self._vectorstore: Optional[FAISS] = None

    def _load_vectorstore(self) -> FAISS:
        if self._vectorstore is not None:
            return self._vectorstore

        if not self.vectorstore_path.exists():
            raise FileNotFoundError(
                f"Vector store not found at {self.vectorstore_path}. Run 'python rag/build_vector_db.py' first."
            )

        embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
        self._vectorstore = FAISS.load_local(
            folder_path=str(self.vectorstore_path),
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        )
        return self._vectorstore

    def _run(
        self,
        query: str,
        run_manager: CallbackManagerForToolRun | None = None,  # noqa: ARG002 - standard signature
    ) -> str:
        store = self._load_vectorstore()
        docs = store.similarity_search(query, k=self.top_k)
        if not docs:
            return "No relevant documents found in the local knowledge base."

        return self._format_docs(docs)

    async def _arun(
        self,
        query: str,
        run_manager: CallbackManagerForToolRun | None = None,
    ) -> str:  # pragma: no cover - async interface not required for workshop
        raise NotImplementedError("LocalRAGTool does not support async execution.")

    @staticmethod
    def _format_docs(docs: list[Document]) -> str:
        formatted = []
        for idx, doc in enumerate(docs, start=1):
            formatted.append(f"Snippet {idx}:\n{doc.page_content.strip()}")
        return "\n\n".join(formatted)
