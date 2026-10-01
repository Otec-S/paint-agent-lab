"""Агент-калькулятор: считает расход краски и стоимость по данным из state."""

from google.adk.agents.llm_agent import Agent

coverage_calculator_agent = Agent(
    model="gemini-3.5-flash",
    name="coverage_calculator_agent",
    description=(
        "Calculates how many liters and 2.5 L cans of the selected paint are "
        "needed for a given area and number of coats, and the total cost."
    ),
    instruction="""
You calculate paint quantities for Cymbal Shops.

Known values for the selected paint (from session state):
- Price per 2.5 L can, EUR: {PRICE?}
- Coverage rate, square meters per liter: {COVERAGE_RATE?}

If either value above is empty, reply that a paint must be selected first and stop.

Given the area in square meters and the number of coats (use 1 if not stated):
1. liters = area * coats / coverage rate
2. cans = liters / 2.5, rounded UP to a whole can
3. total cost = cans * price per can

Show each step with the numbers, then give the final answer:
liters needed, number of cans, total cost in EUR. Answer in the user's language.
""",
)
