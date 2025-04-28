# config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Search API (Serper)
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# LLM API (Groq)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL_NAME = os.getenv("GROQ_MODEL_NAME", "llama3-70b-8192")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
