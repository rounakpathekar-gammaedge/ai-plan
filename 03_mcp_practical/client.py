
import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    # 1. Configure MCP server
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("main.py"))],
    )

    # 2. Connect to MCP server
    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            # 3. Initialize connection
            await session.initialize()

            print("\nConnected to MCP Todo Server!")

            # 4. Discover available tools
            tools_result = await session.list_tools()

            print("\nAvailable MCP Tools:")

            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            # 5. Create a Todo
            print("\nCreating a Todo...")

            add_result = await session.call_tool(
                "add_todo",
                arguments={
                    "title": "Learn MCP Client",
                    "description": "Connect Python client to MCP server",
                },
            )

            for content in add_result.content:
                if content.type == "text":
                    print(content.text)

            # 6. List all Todos
            print("\nFetching all Todos...")

            list_result = await session.call_tool(
                "list_todos",
                arguments={},
            )

            for content in list_result.content:
                if content.type == "text":
                    print(content.text)


if __name__ == "__main__":
    asyncio.run(main())
