#!/usr/bin/env python

import csv
import json


def generate_gias_csv(import_file: str, export_file: str, config_file: str):
    # Import configuration from JSON file
    json_file = open(config_file,)
    config = json.load(json_file)

    # File configuration
    file_encoding = config['encoding']

    # Import mapping
    # Required fields
    col_inventarisnummer = config['ColumnInventarisnummer'] if config['ColumnInventarisnummer'] != "" else ""
    col_benaming = config['ColumnBenamingArchiefeenheid'] if config['ColumnBenamingArchiefeenheid'] != "" else raise ValueError("A column for 'Benaming archiefeenheid' is required.")


    # Import CSV file with object numbers and optional extra information
    csv_contents = csv.DictReader(open(import_file, encoding=file_encoding))

    # Make and export row-by-row a CSV file with PIDs
    with open(export_file, 'w') as output_file:
        # define field names for header row
        fields = []
        fields.append("Inventarisnummer")
        fields.append("Benaming Archiefeenheid")


        # define dictionary for each content row
        export_row = {}
        export_row["Inventarisnummer"] = ""
        export_row["Benaming Archiefeenheid"] = ""

        # create CSV file
        writer = csv.DictWriter(output_file, fieldnames=fields)
        writer.writeheader()

        # create content rows
        for import_row in csv_contents:
            export_row["Inventarisnummer"] = import_row[col_inventarisnummer]
            export_row["Benaming Archiefeenheid"] = import_row[col_benaming]

            writer.writerow(export_row)
