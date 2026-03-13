"""
CSV to JSON converter for Rashi predictions
============================================
HOW TO USE (every month):
  1. Joshi ji fills Google Sheet with new predictions
  2. File > Download > Comma Separated Values (.csv)  →  save as "rashis.csv" in this folder
  3. Open Terminal, go to this folder:
         cd "/Users/shrinidhikatti/Documents/rashi4 claude"
  4. Run:
         python3 csv_to_json.py
  5. data.json is updated  →  upload it to the website

GOOGLE SHEET COLUMN ORDER (Row 1 = these exact headers):
  rashi | month_year |
  intro_en | intro_kn |
  career_en | career_kn |
  finance_en | finance_kn |
  family_en | family_kn |
  health_en | health_kn |
  growth_en | growth_kn |
  remedy_en | remedy_kn |
  conclusion_en | conclusion_kn

ROWS 2–13: one row per rashi in this order:
  mesha, vrishabha, mithuna, karka, simha, kanya,
  tula, vrischika, dhanus, makara, kumbha, meena

TIPS FOR JOSHI JI:
  - Type English text in the _en columns, Kannada in _kn columns
  - Multiple paragraphs in one cell are fine — just press Enter inside the cell
  - Do not change the column header names
  - Do not change the rashi names in column A (must stay lowercase English)
"""

import csv
import json
import os
import sys

CSV_FILE  = "rashis.csv"
JSON_FILE = "data.json"

FIELDS = [
    "intro_en",    "intro_kn",
    "career_en",   "career_kn",
    "finance_en",  "finance_kn",
    "family_en",   "family_kn",
    "health_en",   "health_kn",
    "growth_en",   "growth_kn",
    "remedy_en",   "remedy_kn",
    "conclusion_en", "conclusion_kn",
]

def convert(csv_path, json_path):
    if not os.path.exists(csv_path):
        print(f"ERROR: '{csv_path}' not found.")
        print("Download the Google Sheet as CSV and save it as 'rashis.csv' in this folder.")
        sys.exit(1)

    data = {}

    with open(csv_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row["rashi"].strip().lower()
            if not key:
                continue
            entry = {"month": row["month_year"].strip()}
            for field in FIELDS:
                entry[field] = row.get(field, "").strip()
            data[key] = entry

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Done! {len(data)} rashis written to {json_path}")
    print("Upload data.json to your website and you're done.")

if __name__ == "__main__":
    convert(CSV_FILE, JSON_FILE)
