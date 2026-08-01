import asyncio
import os
from dotenv import load_dotenv
'''
Instructor
from langchain.agents import create_agent   Instructor
from langgraph.prebuilt import create_react_agent  # Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import StdioClient
'''
# Gemini
# 1. Import the modern agent runner instead of legacy `create_agent`
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv

load_dotenv(override=True)

async def main():
    print("Hello from langchain-mcp-adapters!")
# 2. Initialize your buddy Gemini!
# gemini-2.5-flash is fast, cheap, and excellent at tool-calling.
    model = ChatGoogleGenerativeAI(model="gemini-flash-latest")

# 3. Define the parameters for your MCP server.
# Swap out "your_mcp_server.py" with the actual path to your server file.
    server_params = StdioServerParameters(
        command="python", 
        args=["D:/Dr.Mohammed/OnLine_Courses/Udemy/MCP Crash Course/langchain-mcp-adapters/servers/math_server.py"], 
    )
# 4. Connect to the MCP server and run the agent
    print("Connecting to MCP Server...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the MCP session
            await session.initialize()
            
            # Load the MCP tools and convert them to LangChain tools
            tools = await load_mcp_tools(session)
            print(f"Loaded {len(tools)} tools.")
            print(tools)

            # Create your Gemini agent with the tools
            agent = create_agent(model, tools)

            # 5. Run a prompt to test your agent
            user_prompt = input("User Prompt like What is (3 + 2) times 10? ") # Swap with a prompt that needs your MCP tools!
            print(f"Asking Gemini: '{user_prompt}'")
            
            response = await agent.ainvoke({"messages": [HumanMessage(content=user_prompt)]})
            
            # Print Gemini's final response
            print("\nGemini's Response:")
            print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())