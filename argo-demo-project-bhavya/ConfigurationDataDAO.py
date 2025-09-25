# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 16:47:22 2025

@author: Lenovo
"""
# import csv
# import json
# class DataProcessor:
#     def file_read(self,filepath):
#         if filepath.endswith(".csv"):
#             delimiter=","
#         else:
#             raise ValueError("only csv files are supported")
#         try:
#             with open(filepath,"r",encoding='utf-8') as f:
#                 reader=csv.DictReader(f, delimiter=delimiter)
#                 data=[row for row in reader]
#             print("Read",len(data),"rows from {filepath}")
#             return data
#         except FileNotFoundError:
#             print(f"File not found:{filepath}")
#             return []
#     def csv2Json(self,data):
#         return json.dumps(data,indent=2,ensure_ascii=False)
import pymongo
import os
import csv
import json
from datetime import datetime, timezone
from bson.objectid import ObjectId

# NOTE: In a real application, you would import the DAO and Processor
# from their respective files (e.g., from configuration_dao import ConfigurationDataDAO).
# For this script, we assume the DAO is defined or available in the scope
# (or we would paste it here for a self-contained file, as shown below).

# --- DataProcessor Class (Placeholder/Import) ---
# Assuming DataProcessor is defined as in the previous response.
class DataProcessor:
    def file_read(self, filepath):
        if not filepath.endswith(".csv"):
            raise ValueError("Only CSV files are supported")
        try:
            with open(filepath, "r", encoding='utf-8') as f:
                reader = csv.DictReader(f)
                # Simple cleanup to remove empty rows
                data = [row for row in reader if any(row.values())] 
            return data
        except FileNotFoundError:
            return []
    
    def csv2Json(self, data):
        return json.dumps(data, indent=2, ensure_ascii=False)

# --- ConfigurationDataDAO Class (Placeholder/Import) ---
# Assuming ConfigurationDataDAO is defined as in the previous response.
class ConfigurationDataDAO:
    def __init__(self, db):
        self.collection = db['configuration_data']

    def create_multiple_configuration_data(self, config_list):
        docs_to_insert = []
        now_utc = datetime.now(timezone.utc)
        
        for doc in config_list:
            cleaned_doc = {k: v for k, v in doc.items() if v is not None and v != ''}
            
            # Type conversion for is_active
            is_active_str = cleaned_doc.get('is_active', 'TRUE').upper()
            cleaned_doc['is_active'] = is_active_str == 'TRUE'

            cleaned_doc.update({
                'created_at': now_utc,
                'updated_at': now_utc,
                'deleted_at': None
            })
            docs_to_insert.append(cleaned_doc)

        if not docs_to_insert:
            return []
        
        return self.collection.insert_many(docs_to_insert).inserted_ids
    
# --- GraphQLManager Class ---

class GraphQLManager:
    """
    Manages the application's connection to MongoDB and coordinates 
    data operations for GraphQL mutations/queries (simulated here).
    """
    def __init__(self, connection_string, database_name):
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.db = None
        
    def __enter__(self):
        """Establishes the MongoDB connection when entering a 'with' block."""
        try:
            self.client = pymongo.MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            # Initialize DAO layer
            self.config_dao = ConfigurationDataDAO(self.db)
            return self
        except pymongo.errors.ConnectionFailure as e:
            print(f"ERROR: Failed to connect to MongoDB: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the MongoDB connection when exiting a 'with' block."""
        if self.client:
            self.client.close()
            # print("MongoDB connection closed by GraphQLManager.")

    def bulk_insert_config_data(self, filepath):
        """
        Reads configuration data from a CSV and performs a bulk insert 
        into the MongoDB 'configuration_data' collection.
        
        This method simulates a GraphQL mutation that triggers data ingestion.
        """
        print(f"\n[GraphQLManager] Starting bulk insert process for: {filepath}")
        
        processor = DataProcessor()
        
        # 1. Read the CSV file
        config_list = processor.file_read(filepath)
        
        if not config_list:
            print("[GraphQLManager] No data read. Insertion skipped.")
            return []

        # 2. Perform the bulk insert using the DAO
        inserted_ids = self.config_dao.create_multiple_configuration_data(config_list)
        
        print(f"[GraphQLManager] Successfully inserted {len(inserted_ids)} records.")
        return inserted_ids

# --- Execution Example ---

if __name__ == "__main__":
    # Configuration details
    CONNECTION_STRING = "mongodb://localhost:27017/"
    DATABASE_NAME = "dental_tourism"
    CSV_FILE_PATH = "Argo_Trident_Dental_Config_Combined.csv" 
    
    # ⚠️ Check if the CSV file exists before running the manager
    if not os.path.exists(CSV_FILE_PATH):
        print(f"Error: CSV file '{CSV_FILE_PATH}' not found in the current directory.")
        print("Please ensure the file is present to run the bulk insert test.")
    else:
        print("--- Testing GraphQLManager Bulk Insert Mutation ---")
        
        # Use the GraphQLManager in a 'with' block to ensure connection is closed
        try:
            with GraphQLManager(CONNECTION_STRING, DATABASE_NAME) as manager:
                
                # OPTIONAL: Clear the collection first for a clean test
                # manager.config_dao.collection.delete_many({}) 
                # print("Collection cleared for a fresh run.")
                
                inserted_ids = manager.bulk_insert_config_data(CSV_FILE_PATH)
                
                if inserted_ids:
                    print(f"\nMutation Successful. Example ID: {inserted_ids[0]}")
                else:
                    print("\nMutation completed, but no records were inserted.")
                    
        except pymongo.errors.ConnectionFailure:
            print("\nTest failed due to MongoDB connection issue.")