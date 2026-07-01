import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))
async def main():
    print("Hello from langchain-mcp-adapters!")


if __name__ == "__main__":
    asyncio.run(main())