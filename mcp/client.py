
import asyncio
import sys
import os
import json
from pathlib import Path

from mcp import Client, StdioServerParameters


async def main():
    server_file = Path(__file__).with_name("server.py")

    server_parameters = StdioServerParameters(
        command=sys.executable,
        args=[str(server_file)],
        env=os.environ.copy()
    )

    async with Client(server_parameters) as client:

        print("\n========== MCP SECURITY TEST ==========")
        print("MCP CONNECTION: SUCCESSFUL")

        # Discover available tools
        result = await client.list_tools()

        print("\nAVAILABLE TOOLS:")
        for tool in result.tools:
            print(f"- {tool.name}: {tool.description}")

        # Test 1: Public information
        print("\n--- TEST 1: PUBLIC ACCESS ---")

        public_result = await client.call_tool(
            "get_public_information",
            {}
        )

        for item in public_result.content:
            if hasattr(item, "text"):
                print(item.text)

        # Test 2: Confidential information
        print("\n--- TEST 2: CONFIDENTIAL ACCESS ---")

        confidential_result = await client.call_tool(
            "get_confidential_information",
            {}
        )

        for item in confidential_result.content:
            if hasattr(item, "text"):
                print(item.text)

        print("\n========== TEST COMPLETED ==========")


if __name__ == "__main__":
    asyncio.run(main())
