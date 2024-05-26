class Reader:
    def __init__(self, path, parser):
        self.path = path
        self.parser = parser

    def read_all(self):
        stream = open(self.path, 'r')
        for line in stream:
            self.parser(line)

        stream.close()
