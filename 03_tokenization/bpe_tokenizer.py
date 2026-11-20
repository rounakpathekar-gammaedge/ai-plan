from collections import Counter


def get_pairs(word):
    pairs = []

    for i in range(len(word) - 1):
        pairs.append((word[i], word[i + 1]))

    return pairs


def merge_pair(word, pair):
    result = []
    i = 0

    while i < len(word):

        if (
            i < len(word) - 1
            and word[i] == pair[0]
            and word[i + 1] == pair[1]
        ):
            result.append(word[i] + word[i + 1])
            i += 2

        else:
            result.append(word[i])
            i += 1

    return result


def train_bpe(corpus, num_merges=10):

    # Start with individual characters
    words = [
        list(word) + ["</w>"]
        for word in corpus.split()
    ]

    print("Initial words:")
    print(words)

    for step in range(num_merges):

        pair_counts = Counter()

        # Count adjacent pairs
        for word in words:
            pair_counts.update(get_pairs(word))

        if not pair_counts:
            break

        # Find the most frequent pair
        best_pair = pair_counts.most_common(1)[0][0]

        # Merge the selected pair
        words = [
            merge_pair(word, best_pair)
            for word in words
        ]

        print(f"Merge {step + 1}: {best_pair}")

    print("\nFinal vocabulary units:")

    for word in words:
        print(word)


corpus = "low lower lowest low lower"

train_bpe(corpus)