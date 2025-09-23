import unittest
import os
import csv
import json
from DataProcessor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()
        self.input_file = os.path.join("data", "csv-2-json-mongo-transform-input.tsv")
        self.collection_name = "test_stock_data"
        self.output_tsv_jumbled = os.path.join("data", "output_jumbled.tsv")
        self.output_json_original = os.path.join("data", "output.json")

    def test_file_read(self):
        data = self.processor.file_read(self.input_file)
        self.assertTrue(len(data) > 0, "TSV file should not be empty")
        print("Read",len(data), "rows from TSV file")

    def test_save_original_json(self):
        data = self.processor.file_read(self.input_file)
        os.makedirs("data", exist_ok=True)
        with open(self.output_json_original, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Original input saved as JSON", self.output_json_original)

    def test_jumble_words(self):
        data = self.processor.file_read(self.input_file)

        text_columns = ["generic_common_keys", "ticker", "notes", "status", "securities_name"]
        print("Text columns to jumble", text_columns)

        jumbled_data = self.processor.jumbleWord(data, text_columns, paragraph=True)
        print("Text columns jumbled")

        with open(self.output_tsv_jumbled, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=jumbled_data[0].keys(), delimiter='\t')
            writer.writeheader()
            writer.writerows(jumbled_data)
        print("Jumbled data saved to TSV", self.output_tsv_jumbled)

        self.assertEqual(len(jumbled_data), len(data), "Row count mismatch after jumbling")

    def test_mongo_insert(self):
        with open(self.output_tsv_jumbled, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter='\t')
            jumbled_data = [row for row in reader]

        self.processor.mongoManyInsert(jumbled_data, self.collection_name)
        print("Inserted", len(jumbled_data), "rows into MongoDB collection", self.collection_name)

if __name__ == "__main__":
    unittest.main(verbosity=2)
