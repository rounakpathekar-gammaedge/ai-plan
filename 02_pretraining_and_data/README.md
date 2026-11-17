# Module 2: Pretraining and Data Preparation

## Overview

This module explains how data is collected, cleaned, processed, and prepared before training a Large Language Model (LLM).

LLMs require large amounts of text data to learn language patterns and predict the next token.

## Topics Covered

1. Introduction to LLM pretraining
2. Web crawling and data collection
3. Raw text data
4. Data cleaning
5. HTML tag removal
6. Whitespace normalization
7. Duplicate detection and removal
8. Dataset analysis
9. Word frequency analysis
10. Dataset preparation for tokenization

## Project Structure

```text
02_pretraining_and_data/
│
├── README.md
├── raw_data.txt
├── cleaned_data.txt
├── data_cleaning.py
└── dataset_analysis.py
```

## Implementations

### 1. Data Cleaning

**File:** `data_cleaning.py`

Implemented a Python data-cleaning pipeline that:

- Reads raw text data.
- Removes HTML tags.
- Removes unnecessary whitespace.
- Removes empty records.
- Detects and removes duplicate lines.
- Saves the cleaned dataset.


### 2. Dataset Analysis

**File:** `dataset_analysis.py`

Implemented a dataset analysis program that calculates:

- Total records.
- Total characters.
- Total words.
- Unique words.
- Average words per record.
- Most frequently occurring words.

## Technologies Used

- Python
- Regular Expressions (`re`)
- Pathlib
- Collections (`Counter`)

## Learning Outcomes

After completing this module, I understood:

- How training data is collected from different sources.
- Why raw data requires cleaning before training.
- How duplicate records affect dataset quality.
- How to analyze text datasets using Python.
- Why data preparation is important for LLM pretraining.
