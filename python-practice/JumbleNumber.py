import random

class JumbleNumber:
    def jumble(self, number_str):
        digits = list(str(number_str))
        random.shuffle(digits)
        return "".join(digits)