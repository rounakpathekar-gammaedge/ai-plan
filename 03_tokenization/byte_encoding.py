text = "Hello AI"

# Convert text into UTF-8 bytes
encoded_bytes = text.encode("utf-8")

print("Original Text:", text)

print("Encoded Bytes:", encoded_bytes)

print("Byte Values:", list(encoded_bytes))

# Convert bytes back into text
decoded_text = encoded_bytes.decode("utf-8")

print("Decoded Text:", decoded_text)