
# Original text
text = "I love Python"

# Split text into words
tokens = text.split()

# Display tokens
print("Tokens:", tokens)

# Assign numerical IDs
vocabulary = {
    "I": 0,
    "love": 1,
    "Python": 2
}

# Convert tokens into IDs
token_ids = []

for token in tokens:
    token_ids.append(vocabulary[token])

print("Token IDs:", token_ids)
