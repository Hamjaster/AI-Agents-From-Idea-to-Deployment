"""Reviewer agent that checks quality, accuracy, and completeness."""
from __future__ import annotations

from typing import Iterable, Optional

from crewai import Agent
from crewai.llms import OpenAI

from config.settings import LLM_CONFIG

SYSTEM_PROMPT = (
    "You are the Quality Reviewer for the workshop. "
    "Audit drafts for factual accuracy, pedagogy, deployment readiness, and alignment with the plan. "
    "Provide actionable feedback and highlight risks or missing pieces."
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


def create_reviewer_agent(tools: Optional[Iterable[object]] = None) -> Agent:
    """Create the reviewer agent that validates deliverables before release."""
    return Agent(
        name="Quality Reviewer",
        role="Ensure every deliverable is accurate, actionable, and polished",
        goal="Deliver constructive critiques and sign-off criteria before publication",
        backstory=(
            "Placeholder: Replace with scenario-specific review standards during the workshop. "
            "You safeguard against gaps, errors, and unclear guidance."
        ),
        llm=_build_llm(),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
