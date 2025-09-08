import unittest
import csv
import os
import json
from FileProcessorWord import FileProcessorWord

class TestFileProcessorWord(unittest.TestCase):
    def setUp(self):
        self.input_file = "input_csv_file1.csv"
        self.output_file = "output_csv_file1.csv"
        self.json_file = "output_json_file1.json"

        with open(self.input_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "city"])
            writer.writerow(["1", "Alice", "London"])
            writer.writerow(["2", "Bob", "Paris"])

    def test_process_file(self):
        processor = FileProcessorWord(self.input_file, ["name", "city"])
        processor.process_file(self.output_file)

        with open(self.output_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        self.assertEqual(len(rows), 2)

        original_names = ["Alice", "Bob"]
        for row, original in zip(rows, original_names):
            self.assertEqual(len(row["name"]), len(original))
            self.assertCountEqual(row["name"], original)

        original_cities = ["London", "Paris"]
        for row, original in zip(rows, original_cities):
            self.assertEqual(len(row["city"]), len(original))
            self.assertCountEqual(row["city"], original)

    def test_tojson_positive(self):
        processor = FileProcessorWord(self.input_file)
        result = processor.toJSON(self.json_file)

        with open(self.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(len(result), 2)
        self.assertEqual(data[0]["name"], "Alice")
        self.assertEqual(data[1]["city"], "Paris")

    def test_tojson_empty_file(self):
        empty_file = "empty.csv"
        open(empty_file, "w").close()

        processor = FileProcessorWord(empty_file)
        result = processor.toJSON(self.json_file)

        self.assertEqual(result, [])
        with open(self.json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data, [])

        os.remove(empty_file)

    def test_tojson_non_csv_file(self):
        non_csv_file = "not_a_csv.txt"
        with open(non_csv_file, "w", encoding="utf-8") as f:
            f.write("This is not a CSV file.")

        processor = FileProcessorWord(non_csv_file)
        with self.assertRaises(ValueError) as context:
            processor.toJSON(self.json_file)

        self.assertIn("not a CSV", str(context.exception))

    # TODO extreme file size test check the output message it should contain:"File size exceeds limit. Processing aborted" 
    


if __name__ == "__main__":
    unittest.main()
