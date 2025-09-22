import csv
import json
from JumbleWord import JumbleWord
from MongoDBClient import MongoDBClient

class DataProcessor:

    def file_read(self, file_path):
        if file_path.endswith(".csv"):
            delimiter = ","
        elif file_path.endswith(".tsv"):
            delimiter = "\t"
        else:
            raise ValueError("Only CSV or TSV files are supported")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter=delimiter)
                data = [row for row in reader]
            print(f"✅ Read {len(data)} rows from '{file_path}'")
            return data
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            return []

    def jumbleWord(self, data, columns, paragraph=False):
        for row in data:
            for col in columns:
                if col in row and row[col]:
                    try:
                        if paragraph:
                            row[col] = JumbleWord.jumble_paragraph(row[col])
                        else:
                            row[col] = JumbleWord.jumble(row[col])
                    except Exception as e:
                        print(f"⚠️ Could not jumble column '{col}': {e}")
        print(f"✅ Jumbled columns: {columns}")
        return data

    def csv2Json(self, data):
        return json.dumps(data, indent=2, ensure_ascii=False)

    def mongoManyInsert(self, data, collection_name):
        if not data:
            print("⚠️ No data to insert into MongoDB")
            return
        client = MongoDBClient()
        client.insert_many(collection_name, data)
