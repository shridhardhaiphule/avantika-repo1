import unittest
from JumbleWord import JumbleWord

class TestJumbleWord(unittest.TestCase):
    def test_jumble(self):
        word = "hello"
        jumbled = JumbleWord.jumble(word)
        self.assertCountEqual(jumbled, word)
        self.assertNotEqual(jumbled, word)

        self.assertEqual(JumbleWord.jumble(""), "")
        self.assertEqual(JumbleWord.jumble("a"), "a")

if __name__ == "__main__":
    unittest.main()
