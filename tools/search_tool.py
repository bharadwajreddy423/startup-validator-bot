# tools/search_tool.py

from crewai.tools import BaseTool
from pydantic import Field
from langchain_community.utilities import GoogleSerperAPIWrapper
from config import SERPER_API_KEY

# Initialize Google Search Tool
class SearchTool(BaseTool):
    name: str = "SearchTool"
    description: str = "Useful for finding current market data, trends, regulations, and startup ecosystem insights."

    search: GoogleSerperAPIWrapper = Field(default_factory=lambda: GoogleSerperAPIWrapper(k=5))

    def _run(self, query: str) -> str:
        """Executes a search query and returns summarized results."""
        try:
            if not query:
                return "No query provided."

            results = self.search.run(query)
            return results

        except Exception as e:
            return f"Error while searching: {str(e)}"
