import os
import tempfile


class File(object):
    def __init__(self, *args):
        self.path_to_file = args[0]

    def write(self, line):
        try:
            with open(self.path_to_file, 'w') as fh:
                fh.write(line)
        except IOError:
            print('file not found')

    def __add__(self, other):
        new_dir_path = tempfile.gettempdir()
        tf = tempfile.NamedTemporaryFile().name
        new_file_name = os.path.basename(tf)
        new_path = os.path.join(new_dir_path, new_file_name)
        with open(new_path, 'w') as new_fh:
            with open(self.path_to_file, 'r') as self_fh:
                with open(other.path_to_file, 'r') as other_fh:
                    new_fh.write(self_fh.read())
                    new_fh.write(other_fh.read())
        return File(new_path)

    def __iter__(self):
        fh = open(self.path_to_file)
        self.fh = fh
        return self

    def __next__(self):
        line = self.fh.readline()
        if line == '':
            self.fh.close()
            raise StopIteration
        return line

    def __str__(self):
        return self.path_to_file


if __name__ == '__main__':

    obj = File('/tmp/file.txt')
    obj2 = File('/tmp/file2.txt')

    # print(obj)

    obj3 = obj + obj2
    # print(obj3)

    # print("iteration")
    for line in obj3:
        print(line)

