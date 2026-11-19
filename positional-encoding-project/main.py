
import numpy as np


# Configuration
D_MODEL = 8


# Step 1: Tokenize the input sentence
def tokenize_sentence(sentence):

    tokens = sentence.split()

    return tokens


# Step 2: Generate token embeddings
def generate_token_embeddings(tokens, d_model):

    np.random.seed(42)

    token_embeddings = np.random.rand(
        len(tokens), d_model
    )

    return token_embeddings


# Step 3: Generate sinusoidal positional encoding
def positional_encoding(seq_len, d_model):

    position = np.arange(seq_len)[:, np.newaxis]

    dimensions = np.arange(d_model)[np.newaxis, :]

    angle_rates = 1 / np.power(
        10000,
        (2 * (dimensions // 2)) / d_model
    )

    angles = position * angle_rates

    encoding = np.zeros((seq_len, d_model))

    encoding[:, 0::2] = np.sin(angles[:, 0::2])

    encoding[:, 1::2] = np.cos(angles[:, 1::2])

    return encoding


# Step 4: Main function
def main():

    # Take input from the user
    sentence = input("Enter a sentence: ")

    # Tokenization
    tokens = tokenize_sentence(sentence)

    if not tokens:
        print("Please enter a valid sentence.")
        return

    print("\nOriginal Sentence:", sentence)
    print("Tokens:", tokens)
    print("Total Tokens:", len(tokens))

    # Generate token embeddings
    token_embeddings = generate_token_embeddings(
        tokens, D_MODEL
    )

    print("\nToken Embeddings:")

    for token, embedding in zip(tokens, token_embeddings):
        print(f"{token}: {embedding}")

    print("\nEmbedding Matrix Shape:", token_embeddings.shape)

    # Generate positional encodings
    position_vectors = positional_encoding(
        len(tokens), D_MODEL
    )

    print("\nPositional Encodings:")
    print(position_vectors)

    print("\nPositional Encoding Shape:", position_vectors.shape)

    # Combine token embeddings and positional encodings
    final_embeddings = token_embeddings + position_vectors

    print("\nFinal Embeddings (Token + Position):")
    print(final_embeddings)

    print("\nFinal Embeddings Shape:", final_embeddings.shape)


# Program execution starts here
if __name__ == "__main__":
    main()
