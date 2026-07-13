import asyncio
from dotenv import load_dotenv
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import StdioClient
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters import load_mcp_tools
from langchain.agents import create_agent
load_dotenv()
async def main():
    print("Hello from langchain-mcp-adapters!")


if __name__ == "__main__":
    asyncio.run(main())