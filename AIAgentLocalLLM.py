from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

llm = OllamaLLM(model="mistral")
search = DuckDuckGoSearchAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for answering current events or factual questions",
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

print(agent.run("PROMPT"))
