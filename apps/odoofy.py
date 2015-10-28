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


__docs__ = """
Limitations:
* Assumes the first column is the `id`field for Odoo
* Assumes 1st row is always the header
* Not prepared for CSVs with inconsistent rows item counts
* If Output CSV path's parent directory does not exist, user will need to create it
* Can only handle many2one Relationships
"""

# TODO the help documentation


class Odoofier:
    FLAGS_available = "fm:i:o:"
    PATTERN_invalidIdCharacters = compile(r"[^a-z0-9_]", IGNORECASE)
    FORMAT_askingRelationship = u"[{}] {}: "

    def __init__(self):
        self._setAttributes()
        self._askIfOutputOkay()
        self._eatCSVFiles()
        self._sayCompletion()

    def _askIfOutputOkay(self):
        # PREPARE
        file_directory, file_name = split(self.output_file_path)
        # PROCESS
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
        self.module_name = opt_dict.get('-m', u'odoofy')
        self.is_force_override_output = opt_dict.get('-f', False)
        # HANDLE
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
        pprint(relation_data)

        output_csv_rows = []
        # PROCESS
        for row in input_csv_iterator:




            # PREPARE
            das_id = row.pop(0)
            #

            das_id_str = u"{}.{}_{}".format(self.module_name, self.file_name_id, das_id)


            # CONCLUDE
            # output_csv_rows.append([das_id_str] + row)
        # CONCLUDE
        # self._boxCSVFile(header_row, output_csv_rows)

    def _askUserRelationPrefix(self, header_row):
        # PREPARE
        output_relationships = []
        das_id_prefix = u"{}.{}_".format(self.module_name, self.file_name_id)
        # SHOW
        print(u"[{}] {}: {}".format(0, header_row[0], das_id_prefix))
        # PROCESS
        output_relationships.append((0, das_id_prefix))
        for index, header in enumerate(header_row[1:]):
            # PREPARE
            index += 1
            # ASK
            relationship_prefix = raw_input(u"[{}] {}: ".format(index, header)) or False
            # PROCESS
            output_relationships.append((index + 1, relationship_prefix))
        # CONCLUDE
        return output_relationships

    def _boxCSVFile(self, csv_header, csv_rows):
        with open(self.output_file_path, mode='w+') as file_stream:
            # PREPARE
            output_csv_stream = csv.writer(file_stream, lineterminator=u"\n")
            # PROCESS
            output_csv_stream.writerow(csv_header)
            output_csv_stream.writerows(csv_rows)

    def _sayCompletion(self):
        info(u"Odoo-fication of CSV files are done!")

if __name__ == '__main__':
    Odoofier()
