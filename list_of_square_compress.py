"""
Demonstrate how to use Python's list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

def list_of_square_compress() -> list:
    return [2 ** x for x in range(9)]

print(list_of_square_compress())