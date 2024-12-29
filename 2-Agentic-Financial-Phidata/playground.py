from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import phi
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

load_dotenv()
phi.api = os.getenv("PHI_API_KEY")

web_search_agent= Agent(
    name="web search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True
)

finance_agent=Agent(
    name="finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)