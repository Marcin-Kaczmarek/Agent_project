# MarketPulse: Autonomous Competitive Intelligence Agent 🚀

**An Enterprise Agent submitted for the "Agents for All" Capstone (Enterprise Track).**

## 📖 Overview
MarketPulse is a hierarchical multi-agent system designed to automate the labor-intensive process of competitive market research. By orchestrating specialized agents (Researcher, Analyst, Writer), it transforms a simple user prompt into a comprehensive strategic SWOT analysis in minutes.

## 🤖 Architecture
The system utilizes **LangGraph** for orchestration and **Google Gemini 1.5 Pro** for reasoning.

### The Agent Squad:
1.  **🕵️‍♂️ Researcher Agent:** - **Role:** Autonomous navigation and data gathering.
    - **Tools:** Uses `Tavily` for optimized search queries to fetch real-time market data.
2.  **🧠 Analyst Agent:** - **Role:** Strategy synthesis.
    - **Logic:** Ingests raw search data into Gemini's long-context window to identify trends and sentiments.
3.  **✍️ Writer Agent:** - **Role:** Executive reporting.
    - **Output:** Formats the analysis into a clean Markdown report with Executive Summaries and SWOT tables.

## 🛠️ Key Concepts Applied
1.  **Multi-Agent System:** Sequential orchestration of specialized personas.
2.  **Tools:** Integration of external search tools (Tavily/Google Search).
3.  **Context Engineering:** Utilizing Gemini 1.5 Pro's context window for analyzing aggregated unstructured web data.

## 💻 How to Run

### Prerequisites
- Python 3.9+
- A Google Cloud API Key (for Gemini)
- A Tavily API Key (for Search)

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
