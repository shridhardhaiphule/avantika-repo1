import unittest
import os
import csv
import json
from DataProcessor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        """Setup before each test"""
        self.processor = DataProcessor()
        self.input_file = os.path.join("processed_data", "input.tsv")
        self.collection_name = "test_stock_data"

        # Output files
        self.output_tsv_jumbled = os.path.join("processed_data", "output_jumbled.tsv")
        self.output_json_original = os.path.join("processed_data", "output.json")

    def test_file_read(self):
        """Test reading TSV file"""
        data = self.processor.file_read(self.input_file)
        self.assertTrue(len(data) > 0, "TSV file should not be empty")
        print(f"✅ Read {len(data)} rows from TSV file")

    def test_save_original_json(self):
        """Save original TSV data as JSON (no jumble)"""
        data = self.processor.file_read(self.input_file)
        os.makedirs("processed_data", exist_ok=True)
        with open(self.output_json_original, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Original input saved as JSON '{self.output_json_original}'")

    def test_jumble_words(self):
        """Jumble text columns and save as TSV"""
        data = self.processor.file_read(self.input_file)

        # Detect text columns automatically
        first_row = data[0]
        text_columns = [col for col, val in first_row.items() if isinstance(val, str) and val.strip()]
        print(f"Text columns to jumble: {text_columns}")

        # Jumble text columns
        jumbled_data = self.processor.jumbleWord(data, text_columns, paragraph=True)
        print("✅ Text columns jumbled")

        # Save jumbled data to TSV
        with open(self.output_tsv_jumbled, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=jumbled_data[0].keys(), delimiter='\t')
            writer.writeheader()
            writer.writerows(jumbled_data)
        print(f"✅ Jumbled data saved to TSV '{self.output_tsv_jumbled}'")

        # Optional: simple check to ensure jumbling happened
        self.assertEqual(len(jumbled_data), len(data), "Row count mismatch after jumbling")

    def test_mongo_insert(self):
        """Insert jumbled data into MongoDB"""
        # Read jumbled TSV to insert
        with open(self.output_tsv_jumbled, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter='\t')
            jumbled_data = [row for row in reader]

        self.processor.mongoManyInsert(jumbled_data, self.collection_name)
        print(f"✅ Inserted {len(jumbled_data)} rows into MongoDB collection '{self.collection_name}'")

if __name__ == "__main__":
    unittest.main()
