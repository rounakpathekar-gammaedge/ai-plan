from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    question: str = Field(
        min_length=1,
        max_length=1000
    )

    context: str = Field(
        default="",
        max_length=10000
    )

    version: str = Field(
        default="v2",
        pattern="^v[12]$"
    )


class ChatResponse(BaseModel):

    answer: str

    prompt_version: str

    success: bool