# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:57:15 2025

@author: Lenovo
"""

import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import country_code_for_region
from pymongo import MongoClient
import json

# Countries to mark as active
active_countries_input = {"India", "Thailand", "Mexico", "Turkey", "Hungary", "Costa Rica"}

# Map pycountry names to expected names (special cases)
name_corrections = {
    "Türkiye": "Turkey"
}

countries_list = []
for idx, country in enumerate(pycountry.countries, start=1):
    alpha2 = country.alpha_2
    alpha3 = country.alpha_3
    name = country.name

    # Apply name correction if needed
    normalized_name = name_corrections.get(name, name)

    try:
        isd_code = f"+{country_code_for_region(alpha2)}"
    except Exception:
        isd_code = ""

    countries_list.append({
        "order": idx,
        "short_name": alpha3,
        "long_name": normalized_name,
        "isd_code": isd_code,
        "active": True if normalized_name in active_countries_input else False
    })

# --- Save backup to countries.json ---
with open("countries.json", "w", encoding="utf-8") as f:
    json.dump(countries_list, f, indent=4, ensure_ascii=False)

print("Backup created: countries.json")

# --- MongoDB Connection ---
# client = MongoClient("mongodb://localhost:27017/")
# db = client["argo_demo_project_bhavya"]
# collection = db["countries"]

# # Clear old data and insert new data
# collection.delete_many({})
# collection.insert_many(countries_list)

# --- Count active & inactive countries ---
active_count = sum(1 for c in countries_list if c["active"])
inactive_count = len(countries_list) - active_count

print(f"Total countries inserted: {len(countries_list)}")
print(f"Active countries: {active_count}")
print(f"Inactive countries: {inactive_count}")
print(f"Active countries: {', '.join(active_countries_input)}")
