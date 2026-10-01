from google.adk.agents.llm_agent import Agent
from google.adk.tools.agent_tool import AgentTool

from .calculator_agent import coverage_calculator_agent
from .search_agent import search_agent
from .tools import set_session_value

root_agent = Agent(
    model="gemini-3.5-flash",
    name="root_agent",
    description="Paint expert for Cymbal Shops.",
    instruction=(
        "You are the paint consultant of Cymbal Shops. "
        "For any question about paint facts, use the search specialist. "
        "When the customer chooses or asks about one specific paint, "
        "also call set_session_value twice: key PRICE with the price per "
        "2.5 L can (number only, EUR) and key COVERAGE_RATE with the "
        "coverage in square meters per liter (number only). "
        "For any calculation of liters, cans or cost for a given area, "
        "make sure the paint is selected and stored, then use the "
        "coverage calculator; never do this arithmetic yourself. "
        "Answer in the user's language."
    ),
    tools=[
        AgentTool(agent=search_agent),
        AgentTool(agent=coverage_calculator_agent),
        set_session_value,
    ],
)
