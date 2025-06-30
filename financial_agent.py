"""
Minimal phi‑framework demo that runs 100 % on Hugging‑Face models.
Save as `agent_app.py`, then run:  python agent_app.py
"""

import os
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.huggingface import HuggingFaceChat  # HF wrapper
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

# -------------------------------------------------------------------
# 0. Load Environment
# -------------------------------------------------------------------
load_dotenv()  # Load variables from .env file
HF_TOKEN = os.getenv("HUGGINGFACE_API")  # Match this name in your .env file

# -------------------------------------------------------------------
# 1. Setup Hugging Face Model
# -------------------------------------------------------------------
# Recommended model: 7B-8B instruct class
# If using local inference, use base_url instead

hf_model = HuggingFaceChat(
    id="mistralai/Mistral-7B-Instruct-v0.2",
    max_tokens=2048,
    api_key=HF_TOKEN,  # Optional if running locally
    # base_url="http://localhost:8080",  # Uncomment for local model
)

# -------------------------------------------------------------------
# 2. Build Web Search Agent
# -------------------------------------------------------------------
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=hf_model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True,
)

# -------------------------------------------------------------------
# 3. Build Finance Agent
# -------------------------------------------------------------------
finance_agent = Agent(
    name="Finance Agent",
    role="Get live market data",
    model=hf_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_news=True,
            stock_fundamentals=True,
        )
    ],
    instructions=["Use tables to display the data."],
    show_tool_calls=True,
    markdown=True,
)

# -------------------------------------------------------------------
# 4. Multi-Agent Team
# -------------------------------------------------------------------
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=[
        "Always include sources.",
        "Use tables to display the data where appropriate.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# -------------------------------------------------------------------
# 5. Run Query
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("🤖 Starting Hugging Face-based Agent...")
    multi_ai_agent.print_response(
        "Summarize analyst recommendations and share the latest news for NVDA",
        stream=True,
    )
