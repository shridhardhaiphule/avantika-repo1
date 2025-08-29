import csv
from JumbleNumber import JumbleNumber

class FileProcessorNumber:
    def process_file(self, input_file, output_file, columns_to_jumble):
        jumble = JumbleNumber()

        with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
            reader = csv.reader(infile)
            rows = list(reader)

            fieldnames = [f"Col{i}" for i in range(len(rows[0]))]

            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                row_dict = {fieldnames[i]: row[i] for i in range(len(row))}
                for col in columns_to_jumble:
                    if col in row_dict and row_dict[col].isdigit():
                        row_dict[col] = jumble.jumble(row_dict[col])
                writer.writerow(row_dict)