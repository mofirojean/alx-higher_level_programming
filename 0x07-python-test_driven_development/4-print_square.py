#!/usr/bin/python3

def print_square(size):
    """Prints a square

    Args:
        size (int): length of square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end='') for j in range(size)]
        print()
