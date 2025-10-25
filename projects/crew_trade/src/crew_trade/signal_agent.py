from crewai import Agent

SignalAgent = Agent(
    role="Signal Ingestor",
    goal="Receive trade signals from any source and normalize into a unified structure",
    backstory="You collect signals from multiple providers like TradingView, Telegram, or APIs.",
    verbose=True,
)
