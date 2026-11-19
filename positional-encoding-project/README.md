# Positional Encoding Implementation

## 1. Project Overview

This project demonstrates **Sinusoidal Positional Encoding** in the Transformer architecture using Python and NumPy.

Positional Encoding provides information about the position and order of tokens by adding positional vectors to token embeddings.

## 2. How Positional Encoding Works

Each token has two types of information:

- **Token Embedding:** Represents the token.
- **Positional Encoding:** Represents the token's position.

**Final Embedding = Token Embedding + Positional Encoding**

Example:

| Token | Position |
|---|---:|
| I | 0 |
| love | 1 |
| artificial | 2 |
| intelligence | 3 |

## 3. Sinusoidal Positional Encoding

This project implements Sinusoidal PE from the original Transformer paper, *Attention Is All You Need (2017)*.

**Formulas:**

Even dimensions:

`PE(pos, 2i) = sin(pos / 10000^(2i / d_model))`

Odd dimensions:

`PE(pos, 2i + 1) = cos(pos / 10000^(2i / d_model))`

- `pos`: Token position
- `i`: Dimension pair index
- `d_model`: Embedding dimension
- `10000`: Frequency scaling constant

## 4. Project Workflow

1. Take a sentence as input.
2. Tokenize the sentence.
3. Generate token embeddings.
4. Generate sinusoidal positional encodings.
5. Add both embeddings.
6. Display final embeddings and matrix shapes.

## 5. Project Structure

```text
positional-encoding-project/
│
├── main.py
├── README.md
├── requirements.txt
└── .venv/  # Ignored by Git
```

## 6. Technologies Used

- Python
- NumPy
- Sinusoidal Positional Encoding

## 7. Installation and Execution

Clone the repository and navigate to the project:

```bash
git clone <repository-url>
cd ai-plan/positional-encoding-project
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## 8. Sample Output

Input:

```text
Enter a sentence: Hello world
```

Expected matrix shapes:

```text
Embedding Matrix Shape: (2, 8)
Positional Encoding Shape: (2, 8)
Final Embeddings Shape: (2, 8)
```

## 9. Important Note

- Token embeddings are randomly generated for demonstration.
- Positional encodings are calculated using the original sinusoidal formula.
- This project implements Sinusoidal PE, not Learned PE or RoPE.

## 10. Learning Outcomes

- Understanding the need for positional information in Transformers.
- Generating token embeddings.
- Implementing sinusoidal positional encoding.
- Combining token embeddings with positional encodings.

---

**Project:** Positional Encoding Implementation  
**Architecture:** Transformer  
**Technique:** Sinusoidal Positional Encoding