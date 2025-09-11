import unittest
from JumbleWord import JumbleWord

class TestJumbleWord(unittest.TestCase):
    def test_jumble_valid_input(self):
        word = "hello"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        print(f"✅ Positive Test: '{word}' -> '{jumbled}'")

    def test_non_string_input_raises(self):
        with self.assertRaises(TypeError):
            JumbleWord.jumble(123)
        print("✅ Negative Test: TypeError raised for non-string input")

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            JumbleWord.jumble("")
        print("✅ Negative Test: ValueError raised for empty string")

    def test_single_character(self):
        result = JumbleWord.jumble("a")
        self.assertEqual(result, "a")
        print("✅ Boundary Test: single char 'a' unchanged")

    def test_two_characters(self):
        word = "ab"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        print(f"✅ Boundary Test: '{word}' -> '{jumbled}'")

    def test_large_input(self):
        big_text = " ".join([f"word{i}" for i in range(600)])
        print(f"Extreme Test: 600-word text: {big_text}")
        # TODO Implement & use jumble for paragraphs
        jumbled = JumbleWord.jumble(big_text)
        print(f"Extreme Test: 600-word jumbled: {jumbled}")
        self.assertCountEqual(jumbled, big_text)
        self.assertEqual(len(jumbled), len(big_text))
        print("✅ Extreme Test: 600-word text jumbled successfully")


if __name__ == "__main__":
    unittest.main(verbosity=2)
