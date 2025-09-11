import random

class JumbleWord:
    @staticmethod
    def jumble(word):
        if not isinstance(word, str):
            raise TypeError("Input must be a string")
        if not word.strip():
            raise ValueError("Input string cannot be empty")

        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)
    
    # TODO Create Method that accepts a paragraph and jumbles each word in it.
    
