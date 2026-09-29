"""Агент-справочник: отвечает на вопросы о красках по даташиту Cymbal Shops."""

from pathlib import Path

from google.adk.agents.llm_agent import Agent
from google.adk.agents.readonly_context import ReadonlyContext

DATASHEET = (Path(__file__).parent / "data" / "paint_datasheet.txt").read_text()


def instruction_provider(context: ReadonlyContext) -> str:
    """Собирает инструкцию search_agent вместе с текстом документа."""
    return (
        "You are a lookup specialist for Cymbal Shops paints. "
        "Answer only from the datasheet below, quoting exact prices, "
        "coverage rates and finishes. If something is not in the datasheet, say so.\n\n"
        "=== DATASHEET ===\n" + DATASHEET
    )


search_agent = Agent(
    model="gemini-3.5-flash",
    name="search_agent",
    description="Looks up paint facts: price per 2.5 L can, coverage rate, finishes, ideal use cases.",
    instruction=instruction_provider,
)