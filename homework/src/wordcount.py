
from _internals.count_words import count_words
from _internals.preprocess_lines import preprocess_lines
from _internals.read_all_lines import read_all_lines
from _internals.split_into_words import split_into_words
from _internals.write_word_counts import write_word_counts

if __name__ == "__main__":
    # Initialize the counter and list of files
    counter: dict[str, int] = {}
    files: list[str] = preprocess_lines(folder="data/input/")
    
    # Read all the lines from the files
    for file in files:
        lines: list[str] = read_all_lines(file=file)
        for line in lines:
            words: list[str] = split_into_words(line=line)
            for word in words:
                counter = count_words(word=word, counter=counter)
    
    # Write the word counts to a TSV file
    write_word_counts(counter=counter)
    

