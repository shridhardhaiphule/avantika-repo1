import random
import itertools
from nltk.corpus import words
import nltk

# TODO: REmove this lib
`
nltk.download('words')

english_words = set(words.words())

class WordJumbler:
    def __init__(self, input_word):
        self.word = input_word.lower()

    def jumble_word(self):
        letters = list(self.word)
        random.shuffle(letters)
        return ''.join(letters)

    def create_valid_words(self):
        valid_words = set()
        for length in range(4, len(self.word) + 1):
            for combo in itertools.permutations(self.word, length):
                possible_word = ''.join(combo)
                if possible_word in english_words:
                    valid_words.add(possible_word)
        return valid_words

user_input = input("Enter a word: ")

jumbler = WordJumbler(user_input)

print("\nJumbled Word:")
print(jumbler.jumble_word())

print("\nValid English words from the letters:")
valid_words = jumbler.create_valid_words()

if not valid_words:
    print("No real English words could be made.")
else:
    for i, word in enumerate(valid_words):
        print(word)
        if i == 9: 
            break
