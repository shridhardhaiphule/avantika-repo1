import os
from DataProcessor import DataProcessor

def main():
    processor = DataProcessor()

    data_folder = "data"
    input_file = os.path.join(data_folder, "csv-2-json-mongo-transform-input.tsv")
    output_file = os.path.join(data_folder, "output.json")

    data = processor.file_read(input_file)
    if not data:
        return

    first_row = data[0]
    text_columns = [col for col, val in first_row.items() if isinstance(val, str) and val.strip()]
    print("Text columns to jumble:", text_columns)

    data = processor.jumbleWord(data, text_columns, paragraph=True)

    json_data = processor.csv2Json(data)

    os.makedirs(data_folder, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(json_data)
    print("JSON saved to", output_file)

    processor.mongoManyInsert(data, "stock_data")

if __name__ == "__main__":
    main()
