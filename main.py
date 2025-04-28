# main.py
import streamlit as st
import re

from crew.startup_crew import create_startup_crew
from agents.competitor_analyzer import analyze_competitors
from config import GROQ_API_KEY, GROQ_MODEL_NAME
from groq import Groq

groq_client = Groq(api_key=GROQ_API_KEY)

def analyze_feasibility(startup_idea: str, location: str,
                        market_report: str, competitor_report: str) -> str:
    prompt = (
        "You are a senior startup mentor.\n\n"
        f"Startup Idea: {startup_idea}\n"
        f"Location: {location}\n\n"
        "Market Research Report:\n"
        f"{market_report}\n\n"
        "Competitor Analysis Report:\n"
        f"{competitor_report}\n\n"
        "Tasks:\n"
        "- Decide if this startup should proceed (Go) or not (No-Go).\n"
        "- Provide 5-6 plain-text bullet points explaining the reasoning.\n"
        "Answer in one concise paragraph followed by the bullet list."
    )
    res = groq_client.chat.completions.create(
        model=GROQ_MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an expert startup feasibility analyst."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_completion_tokens=600,
        top_p=1,
    )
    return res.choices[0].message.content

# 🖌 Vibrant colorful styling
st.set_page_config(page_title="🚀 Startup Feasibility Validator", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
        color: #212121;
    }
    .main-box {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 12px 25px rgba(0,0,0,0.2);
    }
    h1 {
        text-align: center;
        font-size: 3.2em;
        background: linear-gradient(45deg, #ff4e50, #f9d423);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }
    h2, h3 {
        color: #0d47a1;
        font-weight: 800;
    }
    .stButton>button {
        background: linear-gradient(90deg, #36d1dc, #5b86e5);
        color: white;
        padding: 0.8rem 2.5rem;
        border: none;
        border-radius: 15px;
        font-size: 1.4rem;
        font-weight: bold;
        box-shadow: 0px 8px 24px rgba(91,134,229,0.4);
        transition: 0.4s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        transform: scale(1.05);
        box-shadow: 0px 10px 30px rgba(255,105,180,0.5);
    }
    .market-block {
        background: linear-gradient(135deg, #fddb92 0%, #d1fdff 100%);
        padding: 2rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-radius: 18px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    }
    .competitor-block {
        background: linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%);
        padding: 2rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-radius: 18px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    }
    .feasibility-block {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 2rem;
        margin-top: 1rem;
        border-radius: 18px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

def clean(txt: str) -> str:
    if not txt:
        return ""
    txt = re.sub(r"\*\*(.*?)\*\*", r"\1", txt)
    txt = re.sub(r"#+\s*", "", txt)
    return txt.replace("*", "-").strip()

# ---- Main UI ----
with st.container():
    st.title("🚀 Startup Feasibility Validator")

    st.markdown(
        """
        <div class="main-box">
            <h3 style='text-align:center;'>Empowering your dreams through AI-driven research, real competitor analysis, and intelligent feasibility prediction.</h3>
            <p style='text-align:center; font-weight:bold;'>Crafted with 💎 CrewAI · LangChain · Groq Llama-3 · Streamlit</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    idea = st.text_input("🌟 What's your Startup Idea?", placeholder="e.g. Drone Delivery Platform")
    location = st.text_input("📍 Target Market Location?", placeholder="e.g. Mumbai")

    if st.button("🔍 Let's Analyze!"):

        if not idea or not location:
            st.error("⚠️ Please fill BOTH fields.")
            st.stop()

        with st.spinner("⏳ Researching, Analyzing, Strategizing..."):
            crew = create_startup_crew(idea, location)
            market_output = list(crew.kickoff())[0][1]
            competitor_output = analyze_competitors(idea, location)
            feasibility_output = analyze_feasibility(
                idea, location, market_output, competitor_output)

        st.success("✅ Feasibility Report Ready!")

        st.subheader("📈 Market Research")
        st.markdown(f"<div class='market-block'>{clean(market_output)}</div>", unsafe_allow_html=True)

        st.subheader("🏢 Competitor Analysis")
        st.markdown(f"<div class='competitor-block'>{clean(competitor_output)}</div>", unsafe_allow_html=True)

        st.subheader("🧠 Final Feasibility Verdict")
        st.markdown(f"<div class='feasibility-block'>{clean(feasibility_output)}</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<center><small> Powered by innovation, designed for dreamers. | CrewAI · LangChain · Groq · Streamlit</small></center>", unsafe_allow_html=True)
