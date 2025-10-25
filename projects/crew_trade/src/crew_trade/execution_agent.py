from crewai import Agent
from src.clients.fyers_client import place_order

ExecutionAgent = Agent(
    role="Trade Executor",
    goal="Execute validated trade orders using Fyers API safely and efficiently.",
    backstory="You are responsible for placing accurate and secure orders on behalf of the strategy.",
    tools=[place_order],
    verbose=True,
)
