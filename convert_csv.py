#!/usr/bin/env python3
"""
Module for converting CSV files to JSON format.

This module provides functionality to convert a CSV file named 'dks.csv' 
located in the same directory as this script into a JSON file named 'dks.json'.

The conversion process includes:
- Reading CSV data with headers
- Converting all dictionary keys to lowercase
- Parsing the 'categories' column into a list of stripped strings
- Writing the transformed data to a JSON file with proper formatting

Example:
    Run the conversion by executing this module directly:
    
        $ python convert_csv.py
"""

import os
import csv
import json
import sys



def convert_csv_to_json():
    """
    Converts the 'dks.csv' file to 'dks.json' format.

    throwsError:
        If the CSV file is not found, an error message is printed to stderr and the program
        exits with a non-zero status code.

    Returns:
        None: The function does not return any value. It performs file I/O operations to read
              from the CSV file and write to the JSON file.
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(dir_path, "dks.csv")
    json_file = os.path.join(dir_path, "dks.json")

    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(csv_file, mode='r', newline="", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if not row["correct_answer"].strip():
                continue  # Skip rows where 'correct_answer' is empty
            # process the row and add it to the data list
            data.append(row)

    # Convert all keys to lowercase
    data = [{k.lower(): v for k, v in row.items()} for row in data]

    print("Successfully read CSV data. Converting to JSON format...")
    print(f"Total records read: {len(data)}")
    print(data[:2])  # Print the first 2 records for verification

    # Parse the 'categories' column into a list of stripped strings
    # collect all answers and put them into a list, then split the
    # list by comma and strip the brackets and whitespace
    for row in data:
        row["categories"] = [c.strip("[]").strip() for c in row["categories"].split(",")]
        row["answers"] = [
            row["answer_a"].strip(),
            row["answer_b"].strip(),
            row["answer_c"].strip(),
            row["answer_d"].strip()
        ]
        # Remove "A | B | C | D + ' - ' " prefix from correct_answer and strip whitespace
        row["correct_answer"] = row["correct_answer"][4:].strip()
        del row["answer_a"]
        del row["answer_b"]
        del row["answer_c"]
        del row["answer_d"]

    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Successfully converted '{csv_file}' to '{json_file}'.")

# Example usage:
if __name__ == "__main__":
    convert_csv_to_json()
