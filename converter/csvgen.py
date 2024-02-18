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
    if config['ColumnBenamingArchiefeenheid'] != "":
        col_benaming = config['ColumnBenamingArchiefeenheid']
    else:
        raise ValueError("A column for 'benaming archiefeenheid' is required.")
    col_soortBenaming = config["ColumnSoortBenaming"] if config["ColumnSoortBenaming"] != "" else ""
    if config['ColumnPeriodeStartVanaf'] != "":
        col_periodeStart = config['ColumnPeriodeStartVanaf']
    else:
        raise ValueError("A column for 'periode start vanaf' is required.")


    # Required values
    val_benamingGeautoriseerd = config["ValueIsBenamingGeautoriseerd"] if config["ValueIsBenamingGeautoriseerd"] != "" else 1

    # Import CSV file with object numbers and optional extra information
    csv_contents = csv.DictReader(open(import_file, encoding=file_encoding))

    # Make and export row-by-row a CSV file with PIDs
    with open(export_file, 'w') as output_file:
        # define field names for header row
        fields = []
        fields.append("Inventarisnummer")
        fields.append("Benaming Archiefeenheid")
        fields.append("Soort benaming")
        fields.append("Is Benaming Geautoriseerd")

        
        fields.append("Periode Start Vanaf")


        # define dictionary for each content row
        export_row = {}
        export_row["Inventarisnummer"] = ""
        export_row["Benaming Archiefeenheid"] = ""
        export_row["Soort benaming"] = ""
        export_row["Is Benaming Geautoriseerd"] = ""


        export_row["Periode Start Vanaf"] = ""

        # create CSV file
        writer = csv.DictWriter(output_file, fieldnames=fields)
        writer.writeheader()

        # create content rows
        row_number = 1
        for import_row in csv_contents:
            export_row["Inventarisnummer"] = import_row[col_inventarisnummer] if col_inventarisnummer != "" else row_number
            export_row["Benaming Archiefeenheid"] = import_row[col_benaming]
            export_row["Soort benaming"] = import_row[col_soortBenaming] if col_soortBenaming != "" else "Toegekende Titel"
            export_row["Is Benaming Geautoriseerd"] = val_benamingGeautoriseerd


            export_row["Periode Start Vanaf"] = import_row[col_periodeStart]

            writer.writerow(export_row)
            row_number += 1
