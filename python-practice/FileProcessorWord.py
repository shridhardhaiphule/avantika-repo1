import csv
import os
from JumbleWord import JumbleWord

class FileProcessorWord:
    def __init__(self, input_file, columns_to_jumble):
        self.input_file = input_file
        self.columns_to_jumble = columns_to_jumble

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


if __name__ == "__main__":
    processor = FileProcessorWord("input_csv_file1.csv", ["name", "city"])
    processor.process_file("output_csv_file1.csv")