import random

class JumbleWord:
    def jumble(self, input_string):
        chars = list(input_string)
        random.shuffle(chars)
        return ''.join(chars)

jumbleWordClass = JumbleWord()
output = JumbleWord.jumble("abcd")
print(output)