import os
import time
import base64
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from openai import AsyncOpenAI

from prompts import load_prompt, FEW_SHOT_EXAMPLES
from schemas import ChatRequest, ChatResponse
from logger import logger


# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is missing")

client = AsyncOpenAI(api_key=api_key)

app = FastAPI(
    title="Prompt Engineering Toolkit",
    description="Practical implementation of Chapter 3",
    version="1.0.0"
)


# 1. Basic chatbot with prompt versioning
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    start_time = time.perf_counter()

    try:

        system_prompt = load_prompt(
            version=request.version,
            context=request.context,
            question=request.question
        )

        response = await client.responses.create(
            model="gpt-5.5",
            instructions=system_prompt,
            input=request.question
        )

        answer = response.output_text

        latency = (time.perf_counter() - start_time) * 1000

        usage = response.usage

        logger.info(
            "Chat completed | version=%s | latency_ms=%.2f | input_tokens=%s | output_tokens=%s",
            request.version,
            latency,
            usage.input_tokens if usage else None,
            usage.output_tokens if usage else None
        )

        return ChatResponse(
            answer=answer,
            prompt_version=request.version,
            success=True
        )

    except Exception:

        logger.exception("Chat request failed")

        raise HTTPException(
            status_code=500,
            detail="Unable to process request"
        )


# 2. Few-shot classification
@app.post("/classify")
async def classify(question: str):

    prompt = f"""
    Classify the student's question into one category:

    admission, examination, fees.

    Follow these examples:

    {FEW_SHOT_EXAMPLES}

    Student question:
    {question}

    Return only the category.
    """

    response = await client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return {
        "category": response.output_text.strip()
    }


# 3. Task decomposition
@app.post("/decompose")
async def decompose(task: str):

    prompt = f"""
    Break the following complex task into smaller steps.

    For every step:
    1. Give the step name.
    2. Explain what needs to happen.
    3. Mention its expected result.

    Task:
    {task}
    """

    response = await client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    return {
        "steps": response.output_text
    }


# 4. Image understanding
@app.post("/analyze-image")
async def analyze_image(
    question: str = Form(...),
    image: UploadFile = File(...)
):

    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ]

    if image.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image format"
        )

    image_bytes = await image.read()

    if len(image_bytes) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="Image too large"
        )

    encoded_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    response = await client.responses.create(
        model="gpt-5.5",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": question
                    },
                    {
                        "type": "input_image",
                        "image_url": (
                            f"data:{image.content_type};"
                            f"base64,{encoded_image}"
                        ),
                        "detail": "high"
                    }
                ]
            }
        ]
    )

    return {
        "answer": response.output_text
    }


# 5. Home route
@app.get("/")
async def home():

    return {
        "message": "Prompt Engineering Toolkit is running"
    }