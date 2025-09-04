import csv
import os
import json
from JumbleNumber import JumbleNumber

class FileProcessorNumber:
    def process_file(self, input_file, output_file, columns_to_jumble):
        max_size = 10 * 1024 * 1024
        file_size = os.path.getsize(input_file)
        if file_size > max_size:
            raise ValueError(f"❌ Input file is too large ({file_size} bytes). Maximum allowed size is 10 MB.")
        print(f"✅ File size is OK: {file_size / (1024*1024):.2f} MB")

        jumble = JumbleNumber()

        with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            reader = csv.reader(infile)
            rows = list(reader)

            if not rows:
                raise ValueError("❌ Input file is empty.")

            fieldnames = [f"Col{i}" for i in range(len(rows[0]))]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                row_dict = {fieldnames[i]: row[i] for i in range(len(row))}
                for col in columns_to_jumble:
                    if col in row_dict and row_dict[col].isdigit():
                        row_dict[col] = jumble.jumble(row_dict[col])
                writer.writerow(row_dict)

        print(f"✅ Output file created: {output_file}")

    def toJSON(self, input_file, output_file):
        if not input_file.endswith(".csv"):
            raise ValueError("❌ Input file is not a CSV")

        if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
            with open(output_file, "w", encoding="utf-8") as outfile:
                json.dump([], outfile, indent=4)
            print("⚠ Input CSV is empty → JSON file contains []")
            return []

        json_array = []
        with open(input_file, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue
                fieldnames = [f"Col{i}" for i in range(len(row))]
                row_dict = {fieldnames[i]: row[i] for i in range(len(row))}
                json_array.append(row_dict)

        with open(output_file, "w", encoding="utf-8") as outfile:
            json.dump(json_array, outfile, indent=4)

        print(f"✅ JSON file created: {output_file}")
        return json_array


if __name__ == "__main__":
    processor = FileProcessorNumber()
    processor.process_file("test_input.csv", "test_output.csv", ["Col0", "Col2"])
    processor.toJSON("test_input.csv", "test_output.json")
