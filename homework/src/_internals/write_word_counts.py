import os


def write_word_counts(counter: dict[str, int], output_folder: str) -> None:
    """Write the word counts to a TSV file

    Args:
        counter: dictionary with the frequency of the words
        output_folder: the folder to write the output to
    """
    # Ensure the output folder path ends with a slash
    if not output_folder.endswith("/"):
        output_folder += "/"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, "wordcount.tsv")
    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in counter.items():
            f.write(f"{word}\t{count}\n")