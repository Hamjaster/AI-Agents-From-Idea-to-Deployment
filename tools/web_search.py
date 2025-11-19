"""DuckDuckGo-powered open web search tool."""
from __future__ import annotations

from langchain_community.tools import DuckDuckGoSearchResults


def create_web_search_tool() -> DuckDuckGoSearchResults:
    """Create a tool that performs top-k DuckDuckGo searches."""
    return DuckDuckGoSearchResults(name="duckduckgo_search", k=5)
