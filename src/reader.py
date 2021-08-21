class Reader:
    def __init__(self):
        self.tree_file = []

    def reads_file(self, path):
        with open(path, 'rb') as reader:
            try:
                for line in reader.read().splitlines():
                    self.tree_file.append(line.decode('utf-8'))
            except UnicodeDecodeError:
                pass
        return self.tree_file

    def execution(self, path):
        return self.reads_file(path)
