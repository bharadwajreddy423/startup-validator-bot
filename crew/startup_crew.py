from crewai import Task, Crew
from agents.market_researcher   import market_researcher
from agents.competitor_agent    import competitor_agent    # already defined
from agents.feasibility_analyst import feasibility_analyst

def create_startup_crew(startup_idea: str, location: str):

    # 1 ─ Market research
    market_task = Task(
        description=f"Market research for '{startup_idea}' in '{location}'.",
        expected_output="Detailed market-research report.",
        agent=market_researcher,
        verbose=True,
    )

    # 2 ─ Competitor analysis  (NO func=, just agent reasoning)
    competitor_task = Task(
        description=f"Competitor analysis for '{startup_idea}' in '{location}'.",
        expected_output="Competitor-landscape report.",
        agent=competitor_agent,               # ← give the agent here
        input_tasks=[market_task],
        verbose=True,
    )

    # 3 ─ Feasibility verdict
    feasibility_task = Task(
        description="Use research + competitor data and decide Go/No-Go.",
        expected_output="Go/No-Go with 5-6 bullet-point justification.",
        agent=feasibility_analyst,
        input_tasks=[market_task, competitor_task],
        verbose=True,
    )

    crew = Crew(
        tasks=[market_task, competitor_task, feasibility_task],
        process="sequential",
        verbose=True,
    )
    return crew
