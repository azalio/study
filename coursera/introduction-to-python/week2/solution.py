import sys


class FileReader(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename) as fh:
                return fh.read()
        except IOError:
            return ""


if __name__ == '__main__':
    filename = sys.argv[1]
    reader = FileReader(filename)
    print(reader.read())
