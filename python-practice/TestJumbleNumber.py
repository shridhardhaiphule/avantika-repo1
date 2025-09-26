import unittest
from JumbleNumber import JumbleNumber


class TestJumbleNumber(unittest.TestCase):

    def setUp(self):
        self.jumbler = JumbleNumber()

    def test_jumble_valid_number(self):
        """✅ Positive Test: jumbling a valid number string"""
        num = "12345"
        jumbled = self.jumbler.jumble(num)
        self.assertCountEqual(jumbled, num)
        self.assertNotEqual(jumbled, num)
        print(f"✅ Positive Test: '{num}' -> '{jumbled}'")

    def test_single_digit(self):
        self.assertEqual(self.jumbler.jumble("7"), "7")
        print("✅ Boundary Test: single digit '7' unchanged")

    def test_two_digits(self):
        num = "12"
        jumbled = self.jumbler.jumble(num)
        self.assertCountEqual(jumbled, num)
        self.assertEqual(len(jumbled), 2)
        print(f"✅ Boundary Test: '{num}' -> '{jumbled}'")

    def test_large_number(self):
        num = "1234567890" * 100  # 1000 digits
        jumbled = self.jumbler.jumble(num)
        self.assertCountEqual(jumbled, num)
        self.assertEqual(len(jumbled), len(num))
        print(f"✅ Extreme Test: {len(num)}-digit number jumbled successfully")

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            self.jumbler.jumble("abcd")
        print("✅ Negative Test: ValueError raised for non-numeric input")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            self.jumbler.jumble("")
        print("✅ Negative Test: ValueError raised for empty string")


if __name__ == "__main__":
    unittest.main()
