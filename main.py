
# Step 1: Store some sentences
sentences = [
    "Python is easy",
    "Python is useful",
    "Python is powerful"
]

# Step 2: Create an empty dictionary
words_data = {}

# Step 3: Learn which word comes after another word
for sentence in sentences:

    words = sentence.split()

    for i in range(len(words) - 1):

        current = words[i]
        next_word = words[i + 1]

        if current not in words_data:
            words_data[current] = []

        words_data[current].append(next_word)


# Step 4: Create a function to predict the next word
def predict(word):

    if word in words_data:
        return words_data[word][0]

    else:
        return "Word not found"


# Step 5: Test the program
input_word = "Python"

prediction = predict(input_word)

print("Input word:", input_word)
print("Predicted next word:", prediction)
