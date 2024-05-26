class Reader:
    def __init__(self, path, parser):
        self.path = path
        self.parser = parser

    def read_all(self):
        for line in open(self.path, 'r'):
            self.parser(line)

