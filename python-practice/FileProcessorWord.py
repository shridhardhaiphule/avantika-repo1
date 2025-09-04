import csv
import os
import json
from JumbleWord import JumbleWord

class FileProcessorWord:
    def __init__(self, input_file, columns_to_jumble=None):
        self.input_file = input_file
        self.columns_to_jumble = columns_to_jumble or []

    def check_file_size(self, max_size_mb=10):
        file_size = os.path.getsize(self.input_file)
        file_size_mb = file_size / (1024 * 1024)

        if file_size_mb < max_size_mb:
            print(f"✅ File size is OK: {file_size_mb:.2f} MB")
            return True
        else:
            print(f"❌ File too large! Size: {file_size_mb:.2f} MB (Limit {max_size_mb} MB)")
            return False

    def process_file(self, output_file):
        if not self.check_file_size():
            print("⚠ File not processed because it exceeds the size limit.")
            return

        with open(self.input_file, "r", encoding="utf-8") as infile, \
            open(output_file, "w", newline="", encoding="utf-8") as outfile:

            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)

            writer.writeheader()

            for row in reader:
                for col in self.columns_to_jumble:
                    if col in row and row[col]:
                        row[col] = JumbleWord().jumble(row[col])
                writer.writerow(row)

        print("✅ Output file created:", output_file)

    def toJSON(self, output_file):

        if not self.input_file.endswith(".csv"):
            raise ValueError("❌ Input file is not a CSV")

        if not os.path.exists(self.input_file) or os.path.getsize(self.input_file) == 0:
            with open(output_file, "w", encoding="utf-8") as outfile:
                json.dump([], outfile, indent=4)
            print("⚠ Input CSV is empty → JSON file contains []")
            return []

        json_array = []
        with open(self.input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                json_array.append(row)

        with open(output_file, "w", encoding="utf-8") as outfile:
            json.dump(json_array, outfile, indent=4)

        print("✅ JSON file created:", output_file)
        return json_array


if __name__ == "__main__":
    processor = FileProcessorWord("input_csv_file1.csv", ["name", "city"])
    processor.process_file("output_csv_file1.csv")
    processor.toJSON("output_json_file1.json")
