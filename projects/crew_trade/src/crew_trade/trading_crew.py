from crewai import Crew, Task
from crew_trade.signal_agent import SignalAgent
from crew_trade.execution_agent import ExecutionAgent
from crew_trade.notifier_agent import NotifierAgent
from crew_trade.strategist_agent  import StrategistAgent

# Define the tasks
signal_task = Task(
    description="Ingest trade signal and normalize it.",
    agent=SignalAgent
)
strategy_task = Task(
    description="Analyze the normalized signal and decide if it’s actionable.",
    agent=StrategistAgent,
    depends_on=[signal_task]
)
execute_task = Task(
    description="Execute the approved trade using Fyers API.",
    agent=ExecutionAgent,
    depends_on=[strategy_task]
)
notify_task = Task(
    description="Send Telegram notification about trade result.",
    agent=NotifierAgent,
    depends_on=[execute_task]
)

# Combine all agents into a Crew
TradingCrew = Crew(
    agents=[SignalAgent, StrategistAgent, ExecutionAgent, NotifierAgent],
    tasks=[signal_task, strategy_task, execute_task, notify_task],
    verbose=True
)
