# 🤖 FirstAIAgent – AI Agent with Local & Hosted LLMs using LangChain

This project demonstrates how to build intelligent agents using [LangChain](https://www.langchain.com/) with two different configurations:
- **Local LLM** via [Ollama](https://ollama.com/)
- **Hosted LLM** via [OpenRouter](https://openrouter.ai/) 

These agents can answer queries using LLM reasoning, math tools, and live search powered by DuckDuckGo.

---

## 📁 Project Structure

```text
FirstAIAgent/
├── AIAgentLocalLLM.py      # Agent using local Ollama model (e.g., Mistral)
├── AIAgentHostedLLM.py     # Agent using hosted model via OpenRouter API
├── .env                    # Environment variables (API Key and Base URL for hosted LLM)
└── .venv/                  # Python virtual environment (optional)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/FirstAIAgent.git
cd FirstAIAgent
```
### 2. (Optional) Create a Virtual Environment)

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate.bat    # Windows
```
### 3. Install Dependencies

```bash
pip install langchain langchain-community langchain-openai langchain-ollama python-dotenv duckduckgo-search
```
## 4. Create a .env File

```bash
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=https://openrouter.ai/api/v1
```


# ▶️ Run the Agents

## ✅ Local Agent (Ollama)
#### ⚠️ Requires Ollama installed and a local model (e.g., mistral) pulled via ollama pull mistral
```bash
python AIAgentLocalLLM.py
```

## ✅ Hosted Agent (OpenRouter)
#### ⚠️ Ensure .env file is configured correctly
```bash
python AIAgentHostedLLM.py
```