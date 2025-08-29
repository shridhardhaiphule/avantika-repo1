import csv
from JumbleWord import JumbleWord

class FileProcessorWord:
    def __init__(self, input_file, columns_to_jumble):
        self.input_file = input_file
        self.columns_to_jumble = columns_to_jumble

    def process_file(self, output_file):
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
