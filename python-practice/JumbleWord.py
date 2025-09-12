import random
import string

class JumbleWord:
    @staticmethod
    def jumble(word):
        """Jumble the letters of a single word"""
        if not isinstance(word, str):
            raise TypeError("Input must be a string")
        if not word.strip():
            raise ValueError("Input string cannot be empty")

        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)

    @staticmethod
    def jumble_paragraph(text):
        """
        Jumble each word in a paragraph.
        Keeps punctuation (.,!?) at the end of words intact.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        if not text.strip():
            raise ValueError("Input string cannot be empty")

        words = text.split()
        jumbled_words = []

        for word in words:
            # Check if last character is punctuation
            if word[-1] in string.punctuation:
                core_word = word[:-1]            # letters only
                punctuation = word[-1]           # store punctuation
            else:
                core_word = word
                punctuation = ''

            # Jumble the letters
            jumbled_word = JumbleWord.jumble(core_word)

            # Add back punctuation
            jumbled_words.append(jumbled_word + punctuation)

        return ' '.join(jumbled_words)

    @staticmethod
    def jumble_array(arr):
        """
        Accepts a list of words/strings and returns a list of jumbled words.
        """
        if not isinstance(arr, list):
            raise TypeError("Input must be a list")
        
        jumbled_list = []
        for word in arr:
            if not isinstance(word, str):
                raise TypeError("Each element must be a string")
            jumbled_list.append(JumbleWord.jumble(word))
        
        return jumbled_list
