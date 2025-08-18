import random
import itertools

# Define a class to work with words
class WordJumbler:
    def __init__(self, input_word):
        # Save the input word for use in other methods
        self.word = input_word

    # Method to jumble the characters of the word
    def jumble_word(self):
        # Convert the word to a list of characters
        letters = list(self.word)
        
        # Shuffle the letters randomly
        random.shuffle(letters)
        
        # Join the shuffled letters back into a string
        jumbled = ''.join(letters)
        
        return jumbled

    # Method to create different possible words from the letters
    def create_possible_words(self):
        # This will store all combinations
        possible_words = set()

        # Make words of length 2 to full length
        for length in range(2, len(self.word) + 1):
            # Create all possible arrangements of the letters
            for combo in itertools.permutations(self.word, length):
                # Join the letters to make a word and add to the set
                possible_words.add(''.join(combo))

        # Return the list of possible words
        return possible_words


# === Example usage ===

# Ask the user to enter a word
user_input = input("Enter a word: ")

# Create an object of the class with the input word
jumbler = WordJumbler(user_input)

# Show the jumbled version
print("\nJumbled Word:")
print(jumbler.jumble_word())

# Show some possible word combinations from the letters
print("\nSome possible words from the letters:")
possible_words = jumbler.create_possible_words()

# Print only the first 10 combinations to keep it short
for i, word in enumerate(possible_words):
    print(word)
    if i == 9:
        break
