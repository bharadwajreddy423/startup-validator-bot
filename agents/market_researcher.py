# agents/market_researcher.py

from crewai import Agent
from tools.search_tool import SearchTool

# Instantiate the SearchTool
search_tool = SearchTool()

# Define the Market Researcher Agent
market_researcher = Agent(
    role="Startup Market Researcher",
    goal=(
        "Conduct thorough market research about the startup idea '{startup_idea}' "
        "in the specified location '{location}', finding information like market size, trends, demand, and regulations."
    ),
    backstory=(
        "You are an expert in startup ecosystems and market research. "
        "You have access to real-time information and can quickly gather insights about any industry or region. "
        "You help founders understand the opportunities and challenges before starting a venture."
    ),
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)
