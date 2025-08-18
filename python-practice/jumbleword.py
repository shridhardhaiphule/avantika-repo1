import random

class JumbleWord:
    def jumble(self, input_string):
        chars = list(input_string)
        random.shuffle(chars)
        return ''.join(chars)

jumbleWord = JumbleWord()
output = jumbleWord.jumble("stone")
print(output)