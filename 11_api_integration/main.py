from openai import OpenAI
from dotenv import load_dotenv
import os

# 1. Load environment variables
load_dotenv()

# 2. Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 3. Get input from user
user_input = input("You: ")

# 4. Send request to LLM
response = client.responses.create(
    model=os.getenv("OPENAI_MODEL"),
    input=user_input
)

# 5. Display LLM response
print("\nAI:", response.output_text)

# 6. Display token usage
print("\nToken Usage:")
print("Input:", response.usage.input_tokens)
print("Output:", response.usage.output_tokens)