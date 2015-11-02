# Reference:  http://fr.slideshare.net/Audaxis/opendays-import-csv-2013v5
# DEBUG
from logging import info, error
# noinspection PyUnresolvedReferences
from pprint import pprint
# ESSENTIAL
from os.path import isfile, isdir, split, splitext, join
from os import makedirs
from sys import argv
from getopt import getopt
from re import compile, IGNORECASE
import csv
from glob import glob
# ODOOFIER
from settings import Settings

"""
Limitations:
* Assumes 1st row is always the header
* Not prepared for CSVs with inconsistent rows item counts
"""


class Odoofier:
    FLAGS_available = "fhm:i:o:"
    PATTERN_invalidIdCharacters = compile(r"[^a-z0-9_]", IGNORECASE)
    PATTERN_validPrefix = compile(r"^[a-z][a-z0-9_\.]*[a-z0-9_]$", IGNORECASE)

    def __init__(self, input_file):
        self._set_attributes(input_file)
        if self.is_asking_help:
            self._say_help()
        else:
            self._ask_settings_okay()
            self._eat_csv_files()
            self._say_completion()

    def _ask_settings_okay(self):
        # PREPARE
        file_directory, file_name = split(self.output_file_path)
        # HANDLE
        if not isfile(self.input_file_path):
            error(u"The Input CSV file does not exist.  Check the spelling of you r path.")
            exit()
        if not self.is_force_override_output and isfile(self.output_file_path):
            error(u"The output file exist, use `-f` option to override it.")
            exit()
        # PROCESS
        if not isdir(file_directory):
            makedirs(file_directory)

    def _set_attributes(self, input_file):
        # PREPARE
        opt_list, args = getopt(argv[1:], self.FLAGS_available)
        opt_list = [(flag, True if value == '' else value) for flag, value in opt_list]
        opt_dict = dict(opt_list)
        self.is_force_override_output = opt_dict.get('-f', Settings.force_override)
        self.is_asking_help = opt_dict.get('-h', False)
        # HANDLE
        if not self.is_asking_help:
            try:
                self.input_file_path = input_file
                self.output_file_path = join(
                    Settings.output_dir, u"{}_odoo{}".format(*splitext(split(input_file)[1])))
            except IndexError:
                error(
                    u"You need to specify the Input and Output file paths, "
                    u"by using the `-i` and `-o` arguments respectively.")
                exit()
            # PREPARE
            file_head, file_tail = splitext(split(self.input_file_path)[1])
            self.file_name_id = self.PATTERN_invalidIdCharacters.sub(u"_", file_head)

    def _eat_csv_files(self):
        # PREPARE
        file_stream = open(self.input_file_path)
        input_csv_iterator = csv.reader(file_stream)
        header_row = input_csv_iterator.next()
        relation_data = self._get_relation_prefix()
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
                        (relation_prefix.format(id_value))
                        for id_value in final_value.split(',')])
                # CONCLUDE
                final_row.append(final_value)
            # CONCLUDE
            output_csv_rows.append(final_row)
        # CONCLUDE
        self._box_csv_file(header_row, output_csv_rows)

    def _get_relation_prefix(self):
        # PREPARE
        target_file = self.file_name_id
        # PROCESS
        try:
            return Settings.file_columns[target_file]
        except ArithmeticError:
            error(u"The file `{}` does not exist".format(target_file))
            exit()

    def _box_csv_file(self, csv_header, csv_rows):
        with open(self.output_file_path, mode='w+') as file_stream:
            # PREPARE
            output_csv_stream = csv.writer(file_stream, lineterminator=u"\n")
            # PROCESS
            output_csv_stream.writerow(csv_header)
            output_csv_stream.writerows(csv_rows)

    @staticmethod
    def _say_completion():
        info(u"Odoo-fication of CSV files are done!")

    @staticmethod
    def _say_help():
        print(u"""
This Program will convert your ordinary CSV to Odoo compatible CSV.
See the `settings.py` for advance options.
        """)

if __name__ == '__main__':
    for input_file_path in glob(Settings.input_files):
        Odoofier(input_file_path)
