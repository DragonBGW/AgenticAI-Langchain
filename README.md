# AgenticAI & Langchain Project for Operation n Management Tasks 

# 🧠 Financial Analysis using Agentic AI with Hugging Face + Phi Framework

A lightweight, locally hosted agentic AI system built using the [phi framework](https://github.com/blackhc/phi) and Hugging Face LLMs.  
This project runs **entirely on open-source models**, with integrated tools like real-time web search (DuckDuckGo) and financial analysis (YFinance).
---
## 🔧 Features

- 🤖 Multi-agent architecture (Web Search + Finance)
- 🧠 Hugging Face LLMs (e.g. Mistral-7B)
- 🔍 Live web search via DuckDuckGo
- 📈 Real-time financial data via Yahoo Finance
- 🧾 Agent instructions, tool usage, and markdown/table output

---

## 🚀 Quickstart

### 1. Clone the repo

bash
git clone https://github.com/yourusername/agentic-ai-phi.git
cd agentic-ai-phi

2. Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
OR/ pip install phi[tools] transformers accelerate sentencepiece bitsandbytes torch duckduckgo_search yfinance python-dotenv

🔐 Environment Setup
HUGGINGFACE_API=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
PHI_DATA_API=phi_........

You can create this key at: https://huggingface.co/settings/tokens
Also, you will need OpenAI API key for running Phi framework.

🔐 Running the project
1. If you run "python financial_agent.py" in your VS Code terminal using , a precise analysis will be shown in your terminal like the following->
<img width="713" alt="image" src="https://github.com/user-attachments/assets/10ee2497-1b9e-43d8-adf3-50657a67f5a8" />

2. If you want the project to run as a QNA Chatbot, then run the playground file instead.Enter python run playground.py in your terminal. And then login into your phidata account and go to playground. Connect your localhost (if not connected as default), and now your AIagent is ready for conversation.
<img width="957" alt="image" src="https://github.com/user-attachments/assets/cfab6da7-4a93-4e8c-8669-2bf3c6239a26" />

# 🧠 Using Hugging Face Langchain as Chatbot

This is a minimal working demo of a conversational AI assistant named **Agend**, powered by [LangChain](https://www.langchain.com/), [Featherless AI](https://www.featherless.ai/), and the "mistralai/Mistral-7B-Instruct-v0.2" model. Find the code in lang.ipynb

The assistant can answer natural language questions in a friendly, agent-like tone.  
This project demonstrates how to load API keys securely from a `.env` file, set up LangChain with a third-party model provider, and simulate chat-like behavior programmatically.

---
## 🚀 Features

- Uses `mistral-7B-Instruct` via **Featherless AI**
- Supports **agent-like replies** using LangChain's chat abstraction
- `.env`-based secure key loading
- Pure Python, no frontend/UI needed

---

## 📂 Project Structure

bash
agenticAI/
├── featherless_demo.py      # main script (the one you saved)
├── .env                     # contains FEATHERLESSAI_API_KEY (not committed)
├── .gitignore               # excludes venv, .env, cache, binaries, etc.
└── requirements.txt         # package dependencies (optional)

🔧 Setup Instructions
1. Clone the Repository
git clone https://github.com/DragonBGW/AgenticAI-Langchain.git
cd AgenticAI-Langchain

2. Create Virtual Environment
python -m venv venv
source venv/Scripts/activate      # Windows
# or
source venv/bin/activate          # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt
OR// pip install python-dotenv langchain langchain-featherless-ai

4. Add Your API Key
FEATHERLESSAI_API_KEY=sk-...
HUGGINGFACE_API=hf-...

🧠 Credits
Model: Mistral-7B-Instruct
API Provider: Featherless AI
Framework: LangChain








