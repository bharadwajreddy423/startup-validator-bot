# agents/competitor_agent.py
from crewai import Agent

competitor_agent = Agent(
    role="Competitor Analyst",
    goal=(
        "Analyse key competitors for '{startup_idea}' in '{location}', "
        "summarise strengths and weaknesses, and highlight market gaps."
    ),
    backstory=(
        "You are a strategic analyst who specialises in mapping competitive "
        "landscapes for new ventures."
    ),
    tools=[],                # no external tool needed
    verbose=True,
    allow_delegation=False,
)
