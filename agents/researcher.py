"""Research agent that combines RAG retrieval with live web search."""
from __future__ import annotations

from typing import Iterable, Optional

from crewai import Agent
from crewai.llms import OpenAI

from config.settings import LLM_CONFIG

SYSTEM_PROMPT = (
    "You are the Research Specialist for the workshop. "
    "Synthesize information from the local RAG knowledge base and the live web. "
    "Validate claims, cite sources, and prepare concise bullet summaries for downstream teams."
)


def _build_llm() -> OpenAI:
    """Instantiate an OpenRouter-backed LLM compatible with CrewAI."""
    return OpenAI(
        model=LLM_CONFIG["model"],
        api_key=LLM_CONFIG["openrouter_api_key"],
        base_url="https://openrouter.ai/api/v1",
        temperature=float(LLM_CONFIG["temperature"]),
        max_tokens=int(LLM_CONFIG["max_tokens"]),
    )


def create_researcher_agent(tools: Optional[Iterable[object]] = None) -> Agent:
    """Create the researcher agent that fuses structured and unstructured sources."""
    return Agent(
        name="Insight Researcher",
        role="Curate authoritative context for workshop deliverables",
        goal="Blend RAG insights with verified web findings to back every recommendation",
        backstory=(
            "Placeholder: Replace with scenario-specific research focus during the workshop. "
            "You are rigorous about citations, fact-checking, and keeping insights actionable."
        ),
        llm=_build_llm(),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
