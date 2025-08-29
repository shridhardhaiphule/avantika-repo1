import unittest
import csv
import os
from FileProcessorNumber import FileProcessorNumber

class TestFileProcessorNumber(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_input.csv"
        self.output_file = "test_output.csv"
        with open(self.input_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["123", "abc", "456"])

    def test_process_file(self):
        processor = FileProcessorNumber()
        processor.process_file(self.input_file, self.output_file, ["Col0", "Col2"])

        with open(self.output_file, "r") as f:
            reader = list(csv.DictReader(f))
            row = reader[0]

            self.assertCountEqual(row["Col0"], "123")
            self.assertCountEqual(row["Col2"], "456")

            self.assertEqual(row["Col1"], "abc")

if __name__ == "__main__":
    unittest.main()
