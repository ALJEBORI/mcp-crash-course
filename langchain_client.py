import asyncio
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv(override=True)
model = ChatGoogleGenerativeAI(model="gemini-flash-latest")


async def main():
    print("Hello from langchain-mcp-adapters!")

    # Instantiated directly without 'async with'
    mcp_client = MultiServerMCPClient(
        {
            "math_server": {
                "transport": "stdio",
                "command": "python",
                "args": [
                    "D:/Dr.Mohammed/OnLine_Courses/Udemy/MCP Crash Course/langchain-mcp-adapters/servers/math_server.py"
                ],
            },
            "weather_server": {
                "transport": "sse",
                "url": "http://localhost:8000/sse",
            },
        }
    )

    # Fetch tools asynchronously
    tools = await mcp_client.get_tools()

    agent = create_agent(model, tools)
    result = await agent.ainvoke({"messages": [("user", "what is 3 + 2?")]})
    #result = await agent.ainvoke({"messages": [("user", "what is the weather in sf?")]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())