
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful Python tutor. Explain concepts simply."
    }
]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    # Request a streaming response
    stream = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        max_completion_tokens=400,
        stream=True,
        stream_options={"include_usage": True}
    )

    print("\nAI: ", end="", flush=True)

    full_reply = ""
    usage = None
    finish_reason = None

    # Receive response chunk by chunk
    for chunk in stream:

        if chunk.choices:

            content = chunk.choices[0].delta.content

            if content:
                print(content, end="", flush=True)
                full_reply += content

            if chunk.choices[0].finish_reason:
                finish_reason = chunk.choices[0].finish_reason

        # Final chunk contains usage information
        if chunk.usage:
            usage = chunk.usage

    print()

    # Save the complete response in conversation history
    messages.append({
        "role": "assistant",
        "content": full_reply
    })

    # Display token usage
    if usage:
        print("\nTOKEN USAGE:")
        print("Input tokens:", usage.prompt_tokens)
        print("Output tokens:", usage.completion_tokens)
        print("Total tokens:", usage.total_tokens)

    print("Finish reason:", finish_reason)

ticket_data = json.loads(result)

ticket = SupportTicket(**ticket_data)

print(ticket)
print(ticket.category)
print(ticket.priority)

class SupportTicket(BaseModel):
    category: str
    priority: str
    summary: str
    sentiment: str

    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": """
            Extract customer support information.
            Return ONLY valid JSON with these fields:
            category, priority, summary, sentiment.
            """
        },
        {
            "role": "user",
            "content": "My payment was deducted twice but my order is pending."
        }
    ],
    response_format={"type": "json_object"}
)

result = response.choices[0].message.content

print(result)