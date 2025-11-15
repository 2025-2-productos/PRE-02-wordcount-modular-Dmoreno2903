def count_words(word: str, counter: dict[str, int]) -> dict[str, int]:
    """Count the frequency of the words in a file
    
    Args:
        word: the word to count
        counter: dictionary with the frequency of the words
        
    Returns:
        dictionary with the frequency of the words
    """
    word: str = word.lower().strip(",.!?")
    counter[word] = counter.get(word, 0) + 1
    return counter
    