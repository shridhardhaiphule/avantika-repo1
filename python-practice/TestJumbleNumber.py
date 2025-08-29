import unittest
from JumbleNumber import JumbleNumber

class TestJumbleNumber(unittest.TestCase):
    def test_jumble(self):
        jumbler = JumbleNumber()

        num = "12345"
        jumbled = jumbler.jumble(num)
        self.assertCountEqual(jumbled, num)
        self.assertNotEqual(jumbled, num)

        self.assertEqual(jumbler.jumble("7"), "7")
        self.assertEqual(jumbler.jumble(""), "")

if __name__ == "__main__":
    unittest.main()
