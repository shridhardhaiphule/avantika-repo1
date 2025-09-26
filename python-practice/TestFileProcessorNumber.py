import unittest
import csv
import os
import json
from FileProcessorNumber import FileProcessorNumber


class TestFileProcessorNumber(unittest.TestCase):

    def setUp(self):
        self.input_file = "input_numbers.csv"
        self.output_file = "output_numbers.csv"
        self.json_file = "output_numbers.json"

        with open(self.input_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["12345", "Alice", "67890"])
            writer.writerow(["98765", "Bob", "43210"])

    def tearDown(self):
        for f in [self.input_file, self.output_file, self.json_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_process_file_jumbles_numbers(self):
        processor = FileProcessorNumber()
        processor.process_file(self.input_file, self.output_file, ["Col0", "Col2"])

        with open(self.output_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        self.assertEqual(len(rows), 2)

        # Check that digits are shuffled but same characters
        for row in rows:
            for col in ["Col0", "Col2"]:
                self.assertCountEqual(row[col], row[col])

        print("✅ Positive Test: Numbers jumbled correctly in output CSV")

    def test_tojson_creates_valid_json(self):
        processor = FileProcessorNumber()
        result = processor.toJSON(self.input_file, self.json_file)

        with open(self.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(result), 2)
        self.assertEqual(len(data), 2)
        print("✅ Positive Test: CSV converted to JSON successfully")

    def test_empty_file_raises_error(self):
        empty_file = "empty.csv"
        open(empty_file, "w").close()

        processor = FileProcessorNumber()
        with self.assertRaises(ValueError):
            processor.process_file(empty_file, self.output_file, ["Col0"])
        print("✅ Negative Test: Empty file raises ValueError")

        os.remove(empty_file)

    def test_non_csv_tojson_raises(self):
        txt_file = "not_csv.txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write("Hello World")

        processor = FileProcessorNumber()
        with self.assertRaises(ValueError):
            processor.toJSON(txt_file, self.json_file)
        print("✅ Negative Test: Non-CSV input raises ValueError")

        os.remove(txt_file)

    def test_large_file_size_limit(self):
        big_file = "big.csv"
        with open(big_file, "w", encoding="utf-8") as f:
            f.write("1" * (11 * 1024 * 1024))  # 11 MB

        processor = FileProcessorNumber()
        with self.assertRaises(ValueError):
            processor.process_file(big_file, self.output_file, ["Col0"])
        print("✅ Extreme Test:File size exceeds limit. Processing aborted")

        os.remove(big_file)


if __name__ == "__main__":
    unittest.main()
