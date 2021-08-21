import os


class Writer:
    def __init__(self):
        self.args = None
        self.path = None

    def creates_directory(self):
        self.path = os.path.join(self.args.outfile, 'ls-recursive-converter-logs')
        try:
            os.mkdir(self.path)
        except FileExistsError:
            pass

    def writes_in_text_file(self, list_with_content, files=False):
        with open(f'{self.path}/{"files" if files else "directories"}.txt', 'w') as writer:
            for line in list_with_content:
                writer.write(line+'\n')

    def execution(self, args, files_list, directories_list):
        self.args = args
        self.creates_directory()
        if args.files:
            self.writes_in_text_file(files_list, files=True)
        if args.directories:
            self.writes_in_text_file(directories_list, files=False)
        if not args.files and not args.directories:
            self.writes_in_text_file(files_list, files=True)
            self.writes_in_text_file(directories_list, files=False)
        return self.path
