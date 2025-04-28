# agents/competitor_analyzer.py
import os
import openai                         # openai ≥ 1.x
from openai import OpenAI             # Client class
from config import GROQ_API_KEY, GROQ_MODEL_NAME

# ── Groq-compatible client ────────────────────────────────────────────
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",  # Groq’s endpoint
)

# ── Competitor-analysis helper ────────────────────────────────────────
def analyze_competitors(startup_idea: str, location: str) -> str:
    """Return a concise competitor landscape for this idea/location."""
    prompt = (
        "You are an expert startup advisor.\n\n"
        f"Startup Idea: {startup_idea}\n"
        f"Location: {location}\n\n"
        "Tasks:\n"
        "- Identify 3-5 existing competitors.\n"
        "- Analyse their strengths and weaknesses.\n"
        "- Highlight market gaps a new entrant can exploit.\n\n"
        "Give a concise but detailed report."
    )

    try:
        resp = client.chat.completions.create(
            model=GROQ_MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a startup competitor analyst."},
                {"role": "user",   "content": prompt},
            ],
            temperature=0.5,
            max_tokens=700,
        )
        return resp.choices[0].message.content
    except Exception as exc:
        return f"Error analysing competitors: {exc}"
