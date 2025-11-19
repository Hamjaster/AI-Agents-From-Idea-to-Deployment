"""Global configuration for the Agentic AI workshop project."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Dict

from dotenv import load_dotenv

# Ensure environment variables from a local .env file are available during development.
load_dotenv()

MODEL_NAME = "meta-llama/llama-3.3-70b-instruct:free"

LLM_CONFIG: Dict[str, object] = {
    "model": MODEL_NAME,
    "openrouter_api_key": os.getenv("OPENROUTER_API_KEY", ""),
    "temperature": 0.2,
    "max_tokens": 800,
}


@dataclass
class OpenRouterLLMConfig:
    """Helper container to build consistently configured OpenRouter clients."""

    model: str = MODEL_NAME
    api_key: str = LLM_CONFIG["openrouter_api_key"]  # type: ignore[index]
    temperature: float = float(LLM_CONFIG["temperature"])
    max_tokens: int = int(LLM_CONFIG["max_tokens"])
    base_url: str = "https://openrouter.ai/api/v1"


def get_openrouter_client() -> "OpenAI":
    """Instantiate an OpenAI-compatible client configured for OpenRouter."""
    from openai import OpenAI

    config = OpenRouterLLMConfig()
    if not config.api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is missing. Set it in your environment or .env file."
        )
    return OpenAI(
        base_url=config.base_url,
        api_key=config.api_key,
    )
