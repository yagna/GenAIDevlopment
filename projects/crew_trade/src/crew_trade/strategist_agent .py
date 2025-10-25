from crewai import Agent

StrategistAgent = Agent(
    role="Trade Strategist",
    goal="Validate and analyze incoming trade signals, remove duplicates, and calculate confidence",
    backstory="You analyze trading signals to ensure they are valid and high-quality.",
    verbose=True,
)
