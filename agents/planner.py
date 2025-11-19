"""Planner agent responsible for outlining the project roadmap."""
from __future__ import annotations

from crewai import Agent
from crewai.llms import OpenAI

from config.settings import LLM_CONFIG

SYSTEM_PROMPT = (
    "You are the Planning Strategist for the Agentic AI Workshop. "
    "Design actionable blueprints that turn high-level ideas into an "
    "ordered set of milestones, resource lists, and collaboration touchpoints."
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


def create_planner_agent() -> Agent:
    """Create the planner agent used to bootstrap the workflow."""
    return Agent(
        name="Planning Strategist",
        role="Architect the workshop roadmap and align deliverables",
        goal="Produce a milestone-driven execution plan covering research, authoring, and review",
        backstory=(
            "Placeholder: Replace with scenario-specific planning context during the workshop. "
            "You excel at breaking down ambiguous goals into concrete, evidence-backed steps."
        ),
        llm=_build_llm(),
        allow_delegation=False,
        verbose=True,
        system_prompt=SYSTEM_PROMPT,
    )
