import unittest
import os
from FileProcessor import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def test_process_file(self):
        input_file = "input_file.csv"
        output_file = "output_file.csv"

        processor = FileProcessor()
        processor.process_file(input_file, output_file, ["Col0"])

        self.assertTrue(os.path.exists(output_file))

if __name__ == "__main__":
    unittest.main()
