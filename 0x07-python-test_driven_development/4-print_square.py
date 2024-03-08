#!/usr/bin/python3

"""Module that prints square of a value as `#`"""


def print_square(size):
    """Function that prints ``#`` in place of the square of the given size

    Args:
        size(int): The size of ``#`` to be printed
                    if size is not int raise TypeError with message
                    if size is less than 0 raise ValueError with message
                    else print # in place of square of size
                    followed by newline
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
