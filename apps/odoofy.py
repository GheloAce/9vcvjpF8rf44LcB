# Reference:  http://fr.slideshare.net/Audaxis/opendays-import-csv-2013v5
# DEBUG
from logging import info, error
# noinspection PyUnresolvedReferences
from pprint import pprint
# ESSENTIAL
from os.path import isfile, isdir, split, splitext
from sys import argv
from getopt import getopt
from re import compile, IGNORECASE
import csv


"""
Limitations:
* Assumes 1st row is always the header
* Not prepared for CSVs with inconsistent rows item counts
* If Output CSV path's parent directory does not exist, user will need to create it
"""


class Odoofier:
    FLAGS_available = "fhm:i:o:"
    PATTERN_invalidIdCharacters = compile(r"[^a-z0-9_]", IGNORECASE)
    PATTERN_validPrefix = compile(r"^[a-z][a-z0-9_\.]*[a-z0-9_]$", IGNORECASE)

    def __init__(self):
        self._setAttributes()
        if self.is_asking_help:
            self._sayHelp()
        else:
            self._askIfOutputOkay()
            self._eatCSVFiles()
            self._sayCompletion()

    def _askIfOutputOkay(self):
        # PREPARE
        file_directory, file_name = split(self.output_file_path)
        # PROCESS
        if not isfile(self.input_file_path):
            error(u"The Input CSV file does not exist.  Check the spelling of you r path.")
            exit()
        if not isdir(file_directory):
            error(u"The Directory for the Output CSV does not exist, create it first.")
            exit()
        if not self.is_force_override_output and isfile(self.output_file_path):
            error(u"The output file exist, use `-f` option to override it.")
            exit()

    def _setAttributes(self):
        # PREPARE
        opt_list, args = getopt(argv[1:], self.FLAGS_available)
        opt_list = [(flag, True if value == '' else value) for flag, value in opt_list]
        opt_dict = dict(opt_list)
        self.is_force_override_output = opt_dict.get('-f', False)
        self.is_asking_help = opt_dict.get('-h', False)
        # HANDLE
        if not self.is_asking_help:
            try:
                self.input_file_path = opt_dict.get('-i', args and args.pop(0))
                self.output_file_path = opt_dict.get('-o', args and args.pop(0))
            except IndexError:
                error(
                    u"You need to specify the Input and Output file paths, "
                    u"by using the `-i` and `-o` arguments respectively.")
                exit()
            # PREPARE
            file_head, file_tail = splitext(split(self.input_file_path)[1])
            self.file_name_id = self.PATTERN_invalidIdCharacters.sub(u"_", file_head)

    def _eatCSVFiles(self):
        # PREPARE
        file_stream = open(self.input_file_path)
        input_csv_iterator = csv.reader(file_stream)
        header_row = input_csv_iterator.next()
        relation_data = self._askUserRelationPrefix(header_row)
        output_csv_rows = []
        # PROCESS
        for row in input_csv_iterator:
            # PREPARE
            final_row = []
            # PROCESS
            for index, relation_prefix in relation_data:
                # PREPARE
                final_value = row[index]
                # PROCESS
                if relation_prefix:
                    final_value = u",".join([
                        (relation_prefix + str(id_value))
                        for id_value in final_value.split(',')])
                # CONCLUDE
                final_row.append(final_value)
            # CONCLUDE
            output_csv_rows.append(final_row)
        # CONCLUDE
        self._boxCSVFile(header_row, output_csv_rows)

    def _askUserRelationPrefix(self, header_row):
        # METHOD
        def askRelationshipPrefix(das_index, das_header):
            try:
                input_prefix = raw_input(u"[{}] {}: ".format(das_index, das_header))
                assert input_prefix == u'' or self.PATTERN_validPrefix.search(input_prefix)
                return input_prefix or False
            except AssertionError:
                print(
                    u"*Error* The Relationship Prefix may only:  \n"
                    u"  (1) contain underscores and alphanumeric characters\n"
                    u"  (2) start with a letter; \n"
                    u"  (3) contain at least a single dot, but end with it.\n")
                askRelationshipPrefix(das_index, das_header)
        # PREPARE
        output_relationships = []
        # SHOW
        print(
            u"# External ID Prefixes #\n"
            u"Directions:  This will prompt you with all of the CSV columns, \n"
            u"  if they are a Relationship field, input the Relationship Prefix. \n"
            u"  Leave blank otherwise.")
        # PROCESS
        for index, header in enumerate(header_row):
            output_relationships.append(
                (index, askRelationshipPrefix(index, header)))
        # CONCLUDE
        return output_relationships

    def _boxCSVFile(self, csv_header, csv_rows):
        with open(self.output_file_path, mode='w+') as file_stream:
            # PREPARE
            output_csv_stream = csv.writer(file_stream, lineterminator=u"\n")
            # PROCESS
            output_csv_stream.writerow(csv_header)
            output_csv_stream.writerows(csv_rows)

    @staticmethod
    def _sayCompletion():
        info(u"Odoo-fication of CSV files are done!")

    @staticmethod
    def _sayHelp():
        print(u"""
This Program will convert your ordinary CSV to Odoo compatible CSV.

Usage:

    $ odoofy.py -i `input_CSV_path` -o `output_CSV_path`

        """)

if __name__ == '__main__':
    Odoofier()
