import random

class JumbleWord:
    @staticmethod
    def jumble(word):
        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)
