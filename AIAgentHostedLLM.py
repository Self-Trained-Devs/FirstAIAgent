import os
from dotenv import load_dotenv
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun

# Load .env
load_dotenv()

# Setup LLM
llm = ChatOpenAI(
    model_name="mistralai/mistral-7b-instruct",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("OPENAI_API_BASE"),
    temperature=0.7,
)

# Add search and math tools
ddg_tool = DuckDuckGoSearchRun()
tools = load_tools(["llm-math"], llm=llm) + [ddg_tool]

# Create the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Test query
print("\nAgent Result:", agent.run("how do we solve a production bug for spring boot application?"))
