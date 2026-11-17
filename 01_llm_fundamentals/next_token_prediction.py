text = "Artificial Intelligence is"

predictions = {
    "powerful": 0.50,
    "useful": 0.30,
    "interesting": 0.20
}

next_token = max(predictions, key=predictions.get)

print("Input:", text)
print("Predicted next token:", next_token)
print("Generated sentence:", text + " " + next_token)