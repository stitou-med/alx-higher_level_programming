#!/usr/bin/python3
import dis
import sys


def print_hidden_names(pyc_file_path):
    with open(pyc_file_path, 'rb') as pyc_file:
        code = pyc_file.read()
    try:
        instructions = dis.get_instructions(code)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    for i in instructions:
        if i.opname == 'LOAD_NAME' and not i.argval.startswith('__'):
            print(i.argval)


if __name__ == "__main__":
    pyc_file_path = 'hidden_4.pyc'
    print_hidden_names(pyc_file_path)
