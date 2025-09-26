import csv
import os
import json
from JumbleWord import JumbleWord

class FileProcessorWord:
    MAX_FILE_SIZE_MB = 10
    MAX_FILE_SIZE = MAX_FILE_SIZE_MB * 1024 * 1024  # in bytes

    def __init__(self, input_file, columns_to_jumble=None):
        self.input_file = input_file
        self.columns_to_jumble = columns_to_jumble or []

    def check_file_size(self, max_size_mb=None, print_ok=True):
        """Check if file size exceeds the limit and optionally print message."""
        limit = (max_size_mb or self.MAX_FILE_SIZE_MB) * 1024 * 1024
        file_size = os.path.getsize(self.input_file)

        if file_size > limit:
            raise ValueError("File size exceeds limit. Processing aborted")

        if print_ok:
            print(f"✅ File size is OK: {file_size / (1024*1024):.2f} MB")
        return True

    def process_file(self, output_file, max_size_mb=None):
        if not os.path.exists(self.input_file):
            raise FileNotFoundError("Input file does not exist")

        self.check_file_size(max_size_mb=max_size_mb, print_ok=True)

        with open(self.input_file, "r", encoding="utf-8") as infile, \
             open(output_file, "w", newline="", encoding="utf-8") as outfile:

            reader = csv.DictReader(infile)
            if not reader.fieldnames:
                raise ValueError("Input CSV has no header or is empty")

            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            row_count = 0
            for row in reader:
                for col in self.columns_to_jumble:
                    if col in row and row[col]:
                        row[col] = JumbleWord.jumble(row[col])
                writer.writerow(row)
                row_count += 1

            if row_count == 0:
                raise ValueError("Input CSV has no data rows")

        print("✅ Output file created:", output_file)
        return output_file

    def toJSON(self, output_file, max_size_mb=None):
        if not self.input_file.endswith(".csv"):
            raise ValueError("Input file is not a CSV")

        if not os.path.exists(self.input_file):
            raise FileNotFoundError("Input file does not exist")

        # Skip printing file size for JSON conversion
        self.check_file_size(max_size_mb=max_size_mb, print_ok=False)

        with open(self.input_file, "r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

        if not reader:
            raise ValueError("Input CSV is empty")

        with open(output_file, "w", encoding="utf-8") as outfile:
            json.dump(reader, outfile, indent=4)

        print("✅ JSON file created:", output_file)
        return reader


if __name__ == "__main__":
    processor = FileProcessorWord("input_csv_file1.csv", ["name", "city"])
    processor.process_file("output_csv_file1.csv")
    processor.toJSON("output_json_file1.json")
