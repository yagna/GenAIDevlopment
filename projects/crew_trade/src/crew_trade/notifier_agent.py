from crewai import Agent
from src.clients.telegram_client import send_message

NotifierAgent = Agent(
    role="Notifier",
    goal="Send trade status and updates to Telegram and system logs.",
    backstory="You communicate trade outcomes and alerts to users in real-time.",
    tools=[send_message],
    verbose=True,
)
