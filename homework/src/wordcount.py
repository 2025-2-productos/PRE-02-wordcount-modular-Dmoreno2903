
from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_into_words import split_into_words
from ._internals.write_word_counts import write_word_counts


def wordcount(folder: str, output_folder: str) -> None:
    """Count the frequency of the words in the files in the input directory

    Args:
        folder: the folder to count the words in
        output_folder: the folder to write the output to
    """
    counter: dict[str, int] = {}
    files: list[str] = preprocess_lines(folder=folder)
    for file in files:
        lines: list[str] = read_all_lines(folder=folder, file=file)
        for line in lines:
            words: list[str] = split_into_words(line=line)
            for word in words:
                counter = count_words(word=word, counter=counter)
    write_word_counts(counter=counter, output_folder=output_folder)

    

