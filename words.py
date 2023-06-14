def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    """
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    
    Only words that begin with 'E' will be printed."""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
            
def print_upper_words3(words, must_start_with1, must_start_with2):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    Only words that start with the two selected letters will be printed."""
    for word in words:
        if word.startswith(must_start_with1) or word.startswith(must_start_with2):
            print(word.upper())