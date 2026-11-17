def tokenize(prompt):
    tokens = prompt.split()
    return tokens


def create_token_ids(tokens):
    vocabulary = {
        word: index
        for index, word in enumerate(set(tokens))
    }

    token_ids = [vocabulary[word] for word in tokens]

    return token_ids


def generate_response(prompt):

    print("\n1. Original Prompt:")
    print(prompt)

    # Step 1: Tokenization
    tokens = tokenize(prompt)

    print("\n2. Tokens:")
    print(tokens)

    # Step 2: Token IDs
    token_ids = create_token_ids(tokens)

    print("\n3. Token IDs:")
    print(token_ids)

    # Step 3: Simulated response
    response = "Virat Kohli is one of the greatest Indian T20 batsmen."

    print("\n4. Generated Response:")
    print(response)


user_prompt = input("Enter your prompt: ")

generate_response(user_prompt)