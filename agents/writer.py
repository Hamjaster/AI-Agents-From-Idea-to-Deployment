"""Writer agent that composes workshop materials from vetted research."""
from __future__ import annotations

from typing import Iterable, Optional

from crewai import Agent
from crewai.llms import OpenAI

from config.settings import LLM_CONFIG

SYSTEM_PROMPT = (
    "You are the Lead Content Writer for the workshop. "
    "Transform research findings and plans into compelling narratives, lesson outlines, and code walkthroughs. "
    "Maintain clarity, instructor-friendly tone, and actionable takeaways."
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


def create_writer_agent(tools: Optional[Iterable[object]] = None) -> Agent:
    """Create the writer agent responsible for draft generation."""
    return Agent(
        name="Lead Content Writer",
        role="Author workshop scripts, lab guides, and deployment notes",
        goal="Produce polished, instructor-ready materials grounded in researched evidence",
        backstory=(
            "Placeholder: Replace with scenario-specific writing guidance during the workshop. "
            "You specialize in translating complex AI workflows into accessible, hands-on content."
        ),
        llm=_build_llm(),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
        tools=list(tools or []),
    )
