
# STEP 1: IMPORT LIBRARIES

from transformers import AutoTokenizer
from sentence_transformers import SentenceTransformer


# STEP 2: LOAD MODELS

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

embedding_model = SentenceTransformer(MODEL_NAME)


# STEP 3: INPUT TEXT

text = "FastAPI is a modern Python framework."


# STEP 4: GENERATE TOKENS

tokens = tokenizer.tokenize(text)

print("\nTokens:")
print(tokens)


# STEP 5: GENERATE TOKEN IDS

encoded_text = tokenizer(text)

print("\nToken IDs:")
print(encoded_text["input_ids"])


# STEP 6: GENERATE EMBEDDINGS

embedding = embedding_model.encode(text)

print("\nEmbeddings:")
print(embedding)

print("\nEmbedding Dimensions:")
print(len(embedding))
