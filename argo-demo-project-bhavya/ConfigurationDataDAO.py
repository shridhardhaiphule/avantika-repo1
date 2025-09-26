# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 11:23:56 2025

@author: Lenovo
"""

# graphql_manager.py - Single file containing all classes and execution logic.

import pymongo
import os
import json 
import sys
import csv
from pathlib import Path
from datetime import datetime, timezone
from bson.objectid import ObjectId

# --- FILE PATHS (Assumed to exist in the current directory) ---
CSV_FILE_PATH = "Agro_trident_data.csv"
JSON_FILE_PATH = "countries.json" 
CONNECTION_STRING = "mongodb://localhost:27017/"
DATABASE_NAME = "argo_data_db1"


# PATH SETUP FOR CROSS-DIRECTORY DataProcessor
# This runs first and is CRUCIAL for importing the external module.
CURRENT_DIR = Path(__file__).resolve().parent
REPO_ROOT = CURRENT_DIR.parent 
# External directory where the file DataProcessor.py is located
DATA_PROCESSOR_DIR = REPO_ROOT / "csv-2-json-mongo-transform"

if str(DATA_PROCESSOR_DIR) not in sys.path:
    sys.path.append(str(DATA_PROCESSOR_DIR))
    print(f"[Setup] Added external path to sys.path: {DATA_PROCESSOR_DIR}")

# 1. ConfigurationDataDAO Class (Data Access Layer)
class ConfigurationDataDAO:
    """Data Access Object for configuration_data and related collections."""
    
    def __init__(self, db):
        self.config_collection = db['configuration_data']
        

        try:
            # This calls the code in C:\KoolNano\workspace\avantika-repo1\csv-2-json-mongo-transform\DataProcessor.py
            from DataProcessor import DataProcessor as ExternalDataProcessor
            self.processor = ExternalDataProcessor()
            print("Successfully linked to external DataProcessor for CSV methods.")
        except ImportError as e:
            raise ImportError(f"FATAL: Could not import DataProcessor from {DATA_PROCESSOR_DIR}. "
                              f"Ensure the file is named 'DataProcessor.py' (Title Case) and the class name inside is 'DataProcessor'. Error: {e}")

    def _prepare_config_docs(self, config_list):
        """Internal helper to clean and timestamp configuration_data records."""
        docs_to_insert = []
        now_utc = datetime.now(timezone.utc)
        
        for doc in config_list:
            cleaned_doc = {k: v for k, v in doc.items() if v is not None and v != ''}
            is_active_str = str(cleaned_doc.get('is_active', 'TRUE')).upper()
            cleaned_doc['is_active'] = is_active_str == 'TRUE'

            cleaned_doc.update({
                'created_at': now_utc,
                'updated_at': now_utc,
                'deleted_at': None
            })
            docs_to_insert.append(cleaned_doc)
        return docs_to_insert


    # --- Mutation: CSV Read, Convert, and Insert ---
    def create_config_data_from_csv(self, filepath):
        """Reads CSV using external DataProcessor.file_read, converts, and inserts."""
        
        data_list = self.processor.file_read(filepath)
        if not data_list: return []

        # Requirement: Use external DataProcessor.csv2Json 
        json_output = self.processor.csv2Json(data_list)
        print(f" CSV data converted to JSON string (length: {len(json_output)}).")

        docs_to_insert = self._prepare_config_docs(data_list)
        
        print(f"Inserting {len(docs_to_insert)} records into 'configuration_data'.")
        return self.config_collection.insert_many(docs_to_insert).inserted_ids
    
    
    # --- Mutation: Read JSON and Insert (Implemented internally as json_read is unavailable) ---
    def create_countries_data_from_json(self, filepath, collection_name="countries"):
        """Reads the 'countries.json' file internally and inserts data."""
        
        # Internal JSON reading logic (due to external method unavailability)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                config_list = json.load(f)
            print(f"Read {len(config_list)} records from JSON file: {filepath} (Internal).")
        except FileNotFoundError:
            print(f"JSON File not found: {filepath}")
            return []
        
        if not config_list: return []
        
        now_utc = datetime.now(timezone.utc)
        docs_to_insert = []
        for doc in config_list:
            doc.update({'created_at': now_utc})
            docs_to_insert.append(doc)

        target_collection = self.config_collection.database[collection_name]
        print(f"Inserting {len(docs_to_insert)} records into '{collection_name}'.")
        return target_collection.insert_many(docs_to_insert).inserted_ids


    # --- Query (similar to search_by_category) ---
    def search_by_category(self, category_name):
        """Retrieves all active configuration items for a given category."""
        print(f"Searching by category: {category_name}")
        return list(self.config_collection.find({
            'category': category_name, 
            'deleted_at': None
        }).sort('created_at', pymongo.DESCENDING))
    def search_by_category_subcategory(self, category_name, sub_category_name):
        """Retrieves active configuration items for a given category and sub-category."""
        return list(self.config_collection.find({
            'category': category_name, 
            'sub_category': sub_category_name,
            'deleted_at': None
        }).sort('created_at', pymongo.DESCENDING))


# 3. GraphQLManager Class (Orchestration Layer)

class GraphQLManager:
    """Manages the MongoDB connection and orchestrates DAO operations."""
    
    def __init__(self, connection_string, database_name):
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.db = None
        self.config_dao = None
        
    def __enter__(self):
        try:
            self.client = pymongo.MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            self.config_dao = ConfigurationDataDAO(self.db)
            return self
        except pymongo.errors.ConnectionFailure as e:
            print(f"[Manager] ERROR: Failed to connect to MongoDB: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()

    def insert_csv(self, filepath):
        """Orchestrates CSV ingestion via DAO."""
        return self.config_dao.create_config_data_from_csv(filepath)

    def insert_countries_json(self, filepath):
        """Orchestrates JSON ingestion via DAO."""
        return self.config_dao.create_countries_data_from_json(filepath)


# 4. Execution Block

if __name__ == "__main__":
    
    # Final checks before running
    if not os.path.exists(CSV_FILE_PATH):
        print(f"\n[FATAL] CSV file '{CSV_FILE_PATH}' not found in the current directory.")
        sys.exit(1)
    if not os.path.exists(JSON_FILE_PATH):
        print(f"\n[FATAL] JSON file '{JSON_FILE_PATH}' not found in the current directory.")
        sys.exit(1)
    
    try:
        print("\n--- Starting MongoDB Connection and Data Ingestion ---")
        with GraphQLManager(CONNECTION_STRING, DATABASE_NAME) as manager:
            # Clear collections for a clean run
            manager.config_dao.config_collection.delete_many({}) 
            manager.db['countries'].delete_many({})
            print("[Manager] Cleared configuration_data and countries collections.")
            
            # 1. Execute CSV Ingestion (Uses external DataProcessor)
            inserted_ids_csv = manager.insert_csv(CSV_FILE_PATH)
            print(f"CSV Insert Successful. Total inserted into 'configuration_data': {len(inserted_ids_csv)}")

            # 2. Execute JSON Ingestion (Uses internal logic)
            inserted_ids_json = manager.insert_countries_json(JSON_FILE_PATH)
            print(f"JSON Insert Successful. Total inserted into 'countries': {len(inserted_ids_json)}")


    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred: {e}")
            
    finally:
        print("\n--- Execution Finished ---")