import re


def tokenize(text):
    # Split text into words and punctuation
    tokens = re.findall(r"\w+|[^\w\s]", text)

    return tokens


def create_vocabulary(tokens):

    # Create unique tokens
    unique_tokens = sorted(set(tokens))

    # Assign numerical IDs
    vocabulary = {
        token: index
        for index, token in enumerate(unique_tokens)
    }

    return vocabulary


def main():

    text = "I love Artificial Intelligence. I love Python!"

    # Step 1: Tokenization
    tokens = tokenize(text)

    print("Original Text:")
    print(text)

    print("\nTokens:")
    print(tokens)

    # Step 2: Create vocabulary
    vocabulary = create_vocabulary(tokens)

    print("\nVocabulary:")
    print(vocabulary)

    # Step 3: Convert tokens into IDs
    token_ids = [
        vocabulary[token]
        for token in tokens
    ]

    print("\nToken IDs:")
    print(token_ids)


if __name__ == "__main__":
    main()