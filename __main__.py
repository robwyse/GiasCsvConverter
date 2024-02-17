#!/usr/bin/env python

from argparse import ArgumentParser
from os import path

from converter.csvgen import generate_gias_csv


def main(args):
    import_file = args.csv
    export_file = args.dest if args.dest else path.dirname(path.realpath(import_file)) + 'gias.csv'
    config_file = args.config

    generate_gias_csv(import_file, export_file, config_file)
    print("GIAS-adapted CSV exported to:", export_file)

    print("Finished.")


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate GIAS-adapted CSV-file from existing CSV-file.")
    parser.add_argument('csv', required=True, help="Path to existing CSV-file. Required")
    parser.add_argument('-c', '--config', required=True,
                        help="Path to configuration file. Required.")
    parser.add_argument('-d', '--dest',
                        help="Path to destination file")
    args = parser.parse_args()
    main(args)
