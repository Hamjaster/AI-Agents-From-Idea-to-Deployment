"""Crew assembly for the Agentic AI Workshop."""
from __future__ import annotations

from crewai import Crew, Process

from agents import (
    create_planner_agent,
    create_researcher_agent,
    create_reviewer_agent,
    create_writer_agent,
)
from tasks import build_workshop_tasks
from tools import get_default_toolkit


def create_workshop_crew() -> Crew:
    """Instantiate the fully wired crew with agents, tasks, and tools."""
    research_tools = get_default_toolkit()

    planner = create_planner_agent()
    researcher = create_researcher_agent(tools=research_tools)
    writer = create_writer_agent()
    reviewer = create_reviewer_agent()

    tasks = build_workshop_tasks(
        planner,
        researcher,
        writer,
        reviewer,
        research_tools=research_tools,
    )

    return Crew(
        agents=[planner, researcher, writer, reviewer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )


def run_workshop_pipeline(topic: str) -> str:
    """Run the crew for a given workshop topic and return the compiled output string."""
    crew = create_workshop_crew()
    result = crew.kickoff(inputs={"topic": topic})

    if isinstance(result, str):
        return result

    # CrewAI may return a richer object; fall back to common attributes before casting.
    candidate = getattr(result, "raw_output", None) or getattr(result, "output", None)
    if candidate:
        return str(candidate)

    return str(result)
