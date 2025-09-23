import unittest
from JumbleWord import JumbleWord

class TestJumbleWord(unittest.TestCase):

    def test_jumble_single_word(self):
        word = "hello"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        print(f"Single Word Test: '{word}' -> '{jumbled}'")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            JumbleWord.jumble(123)
        print("Non-string input correctly raised TypeError")

    def test_empty_string_input(self):
        with self.assertRaises(ValueError):
            JumbleWord.jumble("")
        print("Empty string correctly raised ValueError")

    def test_single_character(self):
        word = "a"
        jumbled = JumbleWord.jumble(word)
        self.assertEqual(jumbled, word)
        print(f"Single Character Test: '{word}' -> '{jumbled}'")

    def test_two_characters(self):
        word = "ab"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        print(f"Two Characters Test: '{word}' -> '{jumbled}'")

    def test_paragraph(self):
        paragraph = "apple banana cherry"
        jumbled = JumbleWord.jumble_paragraph(paragraph)
        self.assertEqual(len(jumbled.split()), len(paragraph.split()))
        print(f"Paragraph Test: '{paragraph}' -> '{jumbled}'")

    def test_large_paragraph(self):
        paragraph = (
            "Python is a powerful programming language that is widely used for web development, "
            "data analysis, artificial intelligence, and scientific computing. Learning Python "
            "can help you solve complex problems efficiently and quickly."
        )
        print(f"Original Paragraph:\n{paragraph}\n")

        jumbled = JumbleWord.jumble_paragraph(paragraph)
        print(f"Jumbled Paragraph:\n{jumbled}\n")

        self.assertEqual(len(jumbled), len(paragraph))
        self.assertEqual(len(jumbled.split()), len(paragraph.split()))
        print("Large Paragraph Test Passed Successfully")

    def test_array_input(self):
        words = ["hello", "world", "python"]
        jumbled = JumbleWord.jumble_array(words)
        self.assertEqual(len(jumbled), len(words))
        for original, j in zip(words, jumbled):
            self.assertCountEqual(j, original)
        print(f"Array Test: {words} -> {jumbled}")

    def test_must_change_word(self):
        word = "CCCL"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        print(f"Test repeated letters word: '{word}' -> '{jumbled}'")

    def test_short_word(self):
        word = "aa"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        print(f"Short Word Test: '{word}' -> '{jumbled}'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
