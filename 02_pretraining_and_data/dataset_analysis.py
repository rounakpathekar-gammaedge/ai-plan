from pathlib import Path
from collections import Counter

BASE_DIR = Path(__file__).parent
CLEAN_FILE = BASE_DIR / "cleaned_data.txt"


def analyze_dataset():

    # Read cleaned dataset
    text = CLEAN_FILE.read_text(encoding="utf-8")

    # Split text into records
    records = text.splitlines()

    # Calculate total records
    total_records = len(records)

    # Calculate total characters
    total_characters = len(text)

    # Extract words
    words = text.lower().split()

    # Calculate total words
    total_words = len(words)

    # Calculate unique words
    unique_words = set(words)

    # Calculate average words per record
    average_words = total_words / total_records if total_records else 0

    # Find most frequent words
    word_frequency = Counter(words)

    print("\n===== DATASET ANALYSIS =====")

    print("Total Records:", total_records)
    print("Total Characters:", total_characters)
    print("Total Words:", total_words)
    print("Unique Words:", len(unique_words))

    print("Average Words Per Record:", round(average_words, 2))

    print("\nMost Frequent Words:")

    for word, count in word_frequency.most_common(5):
        print(word, ":", count)


if __name__ == "__main__":
    analyze_dataset()