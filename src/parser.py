import re


class Parser:
    def __init__(self):
        self.tree_file = None
        self.files_list = []
        self.directories_list = []

    def parses_tree_file(self):
        directory = ''
        for line in self.tree_file[self.tree_file.index(''):]:
            if re.findall(r'^./', line):
                directory = line
                self.directories_list.append(f'{line.replace("./", "").replace(":", "")}')
            else:
                if len(line) != 0:
                    self.files_list.append(f'{directory}/{line}'.replace('./', '').replace(':', ''))

    def execution(self, tree_file):
        self.tree_file = tree_file
        self.parses_tree_file()
        return self.files_list, self.directories_list


