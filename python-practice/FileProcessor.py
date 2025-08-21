import csv
import random

class FileProcessor:
    def __init__(self, inputFileName, columnsToRandomise):
        self.inputFileName = inputFileName
        self.columnsToRandomise = columnsToRandomise

    def jumble(self, text):
        letters = list(text)
        random.shuffle(letters)
        return ''.join(letters)

    def processFile(self, outputFileName):
        with open(self.inputFileName, 'r', encoding='utf-8') as infile, \
        open(outputFileName, 'w', newline='', encoding='utf-8') as outfile:

            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()

            for row in reader:
                for col in self.columnsToRandomise:
                    if col in row and row[col]:
                        row[col] = self.jumble(row[col])
                writer.writerow(row)

        print("✅ Output file created:", outputFileName)

if __name__ == "__main__":
    processor = FileProcessor(
        "input_csv_file1.csv",
        ["name", "city"]
    )
    processor.processFile("output_csv_file1.csv")

