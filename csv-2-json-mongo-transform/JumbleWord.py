import random
import string

class JumbleWord:
    @staticmethod
    def jumble(word):
        if not isinstance(word, str):
            raise TypeError("Input must be a string")
        if not word.strip():
            raise ValueError("Input string cannot be empty")
        if len(word) <= 1:
            return word

        letters = list(word)
        shuffled = letters[:]
        attempt = 0
        while shuffled == letters and attempt < 10:
            random.shuffle(shuffled)
            attempt += 1
        return ''.join(shuffled)

    @staticmethod
    def jumble_paragraph(text):
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        if not text.strip():
            raise ValueError("Input string cannot be empty")

        words = text.split()
        jumbled_words = []

        for word in words:
            if word[-1] in string.punctuation:
                core_word = word[:-1]
                punctuation = word[-1]
            else:
                core_word = word
                punctuation = ''

            jumbled_word = JumbleWord.jumble(core_word)
            jumbled_words.append(jumbled_word + punctuation)

        return ' '.join(jumbled_words)

    @staticmethod
    def jumble_array(arr):
        if not isinstance(arr, list):
            raise TypeError("Input must be a list")
        
        jumbled_list = []
        for word in arr:
            if not isinstance(word, str):
                raise TypeError("Each element must be a string")
            jumbled_list.append(JumbleWord.jumble(word))
        
        return jumbled_list
