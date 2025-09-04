import unittest
import csv
import os
import json
from FileProcessorNumber import FileProcessorNumber

class TestFileProcessorNumber(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_input.csv"
        self.output_file = "test_output.csv"
        self.json_file = "test_output.json"

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

    def test_tojson_positive(self):
        processor = FileProcessorNumber()
        result = processor.toJSON(self.input_file, self.json_file)

        with open(self.json_file, "r") as f:
            data = json.load(f)

        self.assertEqual(len(result), 1)
        self.assertEqual(data[0]["Col1"], "abc")

    def test_tojson_empty_file(self):
        empty_file = "empty.csv"
        open(empty_file, "w").close()

        processor = FileProcessorNumber()
        result = processor.toJSON(empty_file, self.json_file)

        self.assertEqual(result, [])
        with open(self.json_file, "r") as f:
            data = json.load(f)
        self.assertEqual(data, [])

        os.remove(empty_file)

    def test_tojson_non_csv_file(self):
        non_csv_file = "not_a_csv.txt"
        with open(non_csv_file, "w") as f:
            f.write("Not a CSV file!")

        processor = FileProcessorNumber()
        with self.assertRaises(ValueError) as context:
            processor.toJSON(non_csv_file, self.json_file)

        self.assertIn("not a CSV", str(context.exception))


if __name__ == "__main__":
    unittest.main()
