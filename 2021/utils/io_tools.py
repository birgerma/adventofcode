
from .transform import as_ints

def read_file_lines(file_name):
    with open(file_name) as f:
        lines = f.read()
    return lines.split('\n')


def read_ints(file_name):
    return as_ints(read_file_lines(file_name))
