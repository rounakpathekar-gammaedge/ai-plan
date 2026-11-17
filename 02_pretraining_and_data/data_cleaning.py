import re
from html import unescape
from pathlib import Path


# Locate the project files
BASE_DIR = Path(__file__).parent

RAW_FILE = BASE_DIR / "raw_data.txt"
CLEAN_FILE = BASE_DIR / "cleaned_data.txt"


def clean_text(text):
    # Decode HTML entities
    text = unescape(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def remove_duplicates(lines):
    unique_lines = []
    seen = set()

    for line in lines:

        # Normalize text for duplicate checking
        normalized = line.lower().strip()

        if normalized and normalized not in seen:
            seen.add(normalized)
            unique_lines.append(line)

    return unique_lines


def main():

    # Read raw data
    raw_text = RAW_FILE.read_text(encoding="utf-8")

    # Split into separate lines
    lines = raw_text.splitlines()

    # Clean individual lines
    cleaned_lines = []

    for line in lines:
        cleaned = clean_text(line)

        if cleaned:
            cleaned_lines.append(cleaned)

    # Remove duplicate lines
    unique_lines = remove_duplicates(cleaned_lines)

    # Save cleaned dataset
    CLEAN_FILE.write_text(
        "\n".join(unique_lines),
        encoding="utf-8"
    )

    print("Data cleaning completed!")
    print("Original lines:", len(lines))
    print("Cleaned unique lines:", len(unique_lines))
    print("Output file:", CLEAN_FILE)


if __name__ == "__main__":
    main()