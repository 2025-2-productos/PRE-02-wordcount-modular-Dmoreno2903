import os


def write_word_counts(counter: dict[str, int]) -> None:
    """Write the word counts to a TSV file
    
    Args:
        counter: dictionary with the frequency of the words
    """
    folder: str = "data/output/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    with open("data/output/wordcount.tsv", "w", encoding="utf-8") as f:
        for word, count in counter.items():
            f.write(f"{word}\t{count}\n")