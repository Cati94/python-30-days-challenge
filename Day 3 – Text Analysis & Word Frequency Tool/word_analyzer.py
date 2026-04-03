import logging
import argparse
import re
from collections import Counter
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Basic stopwords list (can expand)
STOPWORDS = {
    "the", "is", "and", "in", "to", "of", "a", "with"
}


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze word frequency in a text file"
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="document.txt",
        help="Path to text file"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top words to display"
    )
    parser.add_argument(
        "--no-stopwords",
        action="store_true",
        help="Remove common stopwords"
    )
    return parser.parse_args()


def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation (keep only letters/numbers)
    text = re.sub(r"[^\w\s]", "", text)

    return text


def analyze_text(file_path, remove_stopwords=False):
    if not Path(file_path).exists():
        logging.error(f"File not found: {file_path}")
        return None

    word_counter = Counter()

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            cleaned = clean_text(line)
            words = cleaned.split()

            for word in words:
                if remove_stopwords and word in STOPWORDS:
                    continue

                word_counter[word] += 1

    logging.info(f"Processed {sum(word_counter.values())} words")

    return word_counter


def print_results(counter, top_n):
    if not counter:
        print("No words to analyze.")
        return

    print(f"\nTop {top_n} most common words:\n")

    for word, count in counter.most_common(top_n):
        print(f"{word}: {count}")


def main():
    args = parse_arguments()

    counter = analyze_text(args.file, args.no_stopwords)

    print_results(counter, args.top)


if __name__ == "__main__":
    main()
