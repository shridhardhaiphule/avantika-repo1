import random

class JumbleNumber:
    def jumble(self, number_str):
        if number_str == "":
            raise ValueError("❌ Empty string not allowed")

        if not str(number_str).isdigit():
            raise ValueError("❌ Input must be numeric")

        digits = list(str(number_str))
        random.shuffle(digits)
        return "".join(digits)
