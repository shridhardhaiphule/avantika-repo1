import unittest
import csv
import os
from FileProcessor import FileProcessor

class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        # Create a sample input CSV file
        self.input_file = "test_input.csv"
        self.output_file = "test_output.csv"

        with open(self.input_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "city"])
            writer.writerow(["1", "Alice", "London"])
            writer.writerow(["2", "Bob", "Paris"])

    def tearDown(self):
        # Delete test files after running
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_processFile_jumbles_columns(self):
        processor = FileProcessor(self.input_file, ["name", "city"])
        processor.processFile(self.output_file)

        # Read the processed output
        with open(self.output_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Check: same number of rows
        self.assertEqual(len(rows), 2)

        # Check: jumbled words have same length and letters
        original_names = ["Alice", "Bob"]
        for row, original in zip(rows, original_names):
            self.assertEqual(len(row["name"]), len(original))
            self.assertCountEqual(row["name"], original)

        original_cities = ["London", "Paris"]
        for row, original in zip(rows, original_cities):
            self.assertEqual(len(row["city"]), len(original))
            self.assertCountEqual(row["city"], original)

if __name__ == "__main__":
    unittest.main()
