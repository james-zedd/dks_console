#!/usr/bin/env python3

import os
import csv
import json
import sys

def convert_csv_to_json():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(dir_path, "dks.csv")
    json_file = os.path.join(dir_path, "dks.json")

    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    data = [{k.lower(): v for k, v in row.items()} for row in data]

    for row in data:
        row["categories"] = [c.strip("[]").strip() for c in row["categories"].split(",")]

    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Successfully converted '{csv_file}' to '{json_file}'.")

# Example usage:
if __name__ == "__main__":
    convert_csv_to_json()