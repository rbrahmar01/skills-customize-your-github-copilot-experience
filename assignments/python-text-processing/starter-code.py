"""Starter code for Python Text Processing assignment.

Complete the functions below. You may add helper functions as needed.
Follow the README requirements. Do not hard-code results.
"""
from collections import Counter
from pathlib import Path
import string

PUNCTUATION = ".,!?:;\"'"  # punctuation to replace with spaces


def load_raw_text(path: str = "sample.txt") -> str:
    """Read the file contents and return as a string.
    Raises FileNotFoundError if the file does not exist."""
    return Path(path).read_text(encoding="utf-8")


def clean_text(raw: str) -> str:
    """Lowercase, replace punctuation with spaces, collapse spaces, and strip."""
    lowered = raw.lower()
    trans_table = str.maketrans({ch: " " for ch in PUNCTUATION})
    replaced = lowered.translate(trans_table)
    # Collapse multiple spaces
    collapsed = " ".join(replaced.split())
    return collapsed.strip()


def tokenize(cleaned: str) -> list[str]:
    """Split cleaned text into tokens (words)."""
    if not cleaned:
        return []
    return cleaned.split(" ")


def compute_statistics(tokens: list[str]) -> dict:
    """Return core statistics: total_words, unique_words, avg_word_length, top5."""
    if not tokens:
        return {"total_words": 0, "unique_words": 0, "avg_word_length": 0.0, "top5": []}
    total_words = len(tokens)
    unique_words = len(set(tokens))
    avg_word_length = sum(len(t) for t in tokens) / total_words
    counts = Counter(tokens)
    # Sort: frequency desc, then alphabetical
    sorted_items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    top5 = sorted_items[:5]
    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "avg_word_length": avg_word_length,
        "top5": top5,
    }


def write_frequency_report(tokens: list[str], outfile: str = "word_frequencies.txt") -> None:
    counts = Counter(tokens)
    sorted_items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    with open(outfile, "w", encoding="utf-8") as f:
        for word, count in sorted_items:
            if not word:
                continue
            f.write(f"{word},{count}\n")


def main():
    raw = load_raw_text()
    cleaned = clean_text(raw)
    tokens = tokenize(cleaned)
    stats = compute_statistics(tokens)

    print(f"Total words: {stats['total_words']}")
    print(f"Unique words: {stats['unique_words']}")
    print(f"Average word length: {stats['avg_word_length']:.2f}")
    print("Top 5 words:")
    for i, (word, count) in enumerate(stats["top5"], start=1):
        print(f"{i}. {word} ({count})")

    write_frequency_report(tokens)
    print("Wrote word_frequencies.txt")


if __name__ == "__main__":
    main()
