import random

class JumbleWord:
    def jumble(self, word):
        letters = list(word)
        random.shuffle(letters)
        return ''.join(letters)
