"""Standalone MCP client for the local security demonstration."""

import asyncio
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_file = Path(__file__).with_name("server.py")
    server_parameters = StdioServerParameters(
        command=sys.executable,
        args=[str(server_file)],
        env=os.environ.copy(),
    )

    async with stdio_client(server_parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            print("\n========== MCP SECURITY TEST ==========")
            print("MCP CONNECTION: SUCCESSFUL")

            tools = await session.list_tools()
            print("\nAVAILABLE TOOLS:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            for title, tool_name in (
                ("PUBLIC ACCESS", "get_public_information"),
                ("CONFIDENTIAL ACCESS", "get_confidential_information"),
            ):
                print(f"\n--- TEST: {title} ---")
                result = await session.call_tool(tool_name, arguments={})
                for item in result.content:
                    if getattr(item, "text", None):
                        print(item.text)

            print("\n========== TEST COMPLETED ==========")


if __name__ == "__main__":
    asyncio.run(main())
