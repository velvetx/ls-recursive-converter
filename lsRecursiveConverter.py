import argparse
import sys
from src import reader
from src import parser
from src import writer


class Program:
    def __init__(self):
        self.args = None
        self.tree_file = None
        self.files_list = None
        self.directories_list = None
        self.execution()

    def parses_args(self):
        args_parser = argparse.ArgumentParser(description='A very simple and lightweight program that converts the '
                                                          'output of "ls -R > filename.txt" to a wordlist for '
                                                          'dirbuster.')
        args_parser.add_argument('-p', '--path', help='Define path to the created file', required=True)
        args_parser.add_argument('-o', '--outfile', help='Define outfile for result', required=True)
        args_parser.add_argument('-f', '--files', help='Parse files', action='store_true')
        args_parser.add_argument('-d', '--directories', help='Parse directories', action='store_true')
        self.args = args_parser.parse_args()

    def reads_tree_file(self):
        self.tree_file = reader.Reader().execution(self.args.path)

    def parses_tree_file(self):
        self.files_list, self.directories_list = parser.Parser().execution(self.tree_file)

    def writes_output_files(self):
        return writer.Writer().execution(self.args, self.files_list, self.directories_list)

    def execution(self):
        self.parses_args()
        print(f'Ok, starting...')
        self.reads_tree_file()
        self.parses_tree_file()
        print(f'Done!\nCheck your {self.writes_output_files()}/ directory.')
        sys.exit(0)


if __name__ == '__main__':
    Program()
