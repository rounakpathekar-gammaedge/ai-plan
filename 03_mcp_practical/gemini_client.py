
import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


load_dotenv()

MODEL_NAME = "gemini-3.5-flash-lite"


async def main():

    # 1. Get Gemini API key
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY is missing from .env")
        return

    # 2. Configure MCP server
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("main.py"))],
    )

    # 3. Start MCP server and connect client
    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()
            print("Connected to MCP Todo Server!")

            # 4. Get available MCP tools
            mcp_tools = await session.list_tools()

            # 5. Convert MCP tools into Gemini function declarations
            function_declarations = []

            for mcp_tool in mcp_tools.tools:

                tool_data = mcp_tool.model_dump(by_alias=True)

                schema = (
                    tool_data.get("inputSchema")
                    or tool_data.get("input_schema")
                    or {"type": "object", "properties": {}}
                )

                function_declarations.append(
                    types.FunctionDeclaration(
                        name=mcp_tool.name,
                        description=mcp_tool.description or mcp_tool.name,
                        parameters_json_schema=schema,
                    )
                )

            gemini_tool = types.Tool(
                function_declarations=function_declarations
            )

            # 6. Connect to Gemini
            async with genai.Client(api_key=api_key).aio as gemini:

                print("Connected to Gemini!")
                print("Available MCP tools:")

                for tool in mcp_tools.tools:
                    print(f"- {tool.name}")

                # 7. Create Gemini chat
                chat = gemini.chats.create(
                    model=MODEL_NAME,
                    config=types.GenerateContentConfig(
                        temperature=0,
                        tools=[gemini_tool],
                    ),
                )

                print("\nType 'exit' to quit.")

                # 8. Chat loop
                while True:

                    user_prompt = input("\nYou: ").strip()

                    if user_prompt.lower() in ["exit", "quit"]:
                        print("Goodbye!")
                        break

                    if not user_prompt:
                        continue

                    try:
                        response = await chat.send_message(user_prompt)

                        # 9. Handle Gemini tool calls
                        while True:

                            candidate = response.candidates[0]
                            parts = candidate.content.parts or []

                            function_calls = [
                                part.function_call
                                for part in parts
                                if part.function_call is not None
                            ]

                            if not function_calls:
                                break

                            function_responses = []

                            for function_call in function_calls:

                                tool_name = function_call.name
                                arguments = dict(function_call.args or {})

                                print(f"\nExecuting MCP tool: {tool_name}")
                                print("Arguments:", arguments)

                                # 10. Execute actual MCP tool
                                result = await session.call_tool(
                                    tool_name,
                                    arguments=arguments,
                                )

                                result_text = "\n".join(
                                    block.text
                                    for block in (result.content or [])
                                    if hasattr(block, "text")
                                )

                                if not result_text:
                                    structured = getattr(
                                        result,
                                        "structuredContent",
                                        getattr(result, "structured_content", None),
                                    )
                                    result_text = str(structured or "Tool returned no text.")

                                is_error = getattr(
                                    result,
                                    "isError",
                                    getattr(result, "is_error", False),
                                )

                                if is_error:
                                    result_text = "Tool error: " + result_text

                                print("Tool result:", result_text)

                                function_responses.append(
                                    types.Part.from_function_response(
                                        name=tool_name,
                                        response={"result": result_text},
                                    )
                                )

                            # 11. Send tool results back to Gemini
                            # Pass Parts directly, NOT types.Content
                            response = await chat.send_message(
                                function_responses
                            )

                        # 12. Display final Gemini response
                        print(
                            "\nGemini:",
                            response.text or "No text response."
                        )

                    except Exception as error:
                        print(f"\nRequest failed: {error}")


if __name__ == "__main__":
    asyncio.run(main())
