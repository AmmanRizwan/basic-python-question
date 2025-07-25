"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

def reverse_list(data: list) -> list:
    # Create an empty list that will store data in reverse
    listNum: list = []

    # Loop through the data into reverse order
    for i in range(len(data) - 1, 0, -1):
        # Store the data into the empty list
        listNum.append(i)

    return listNum