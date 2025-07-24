"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution
"""

def minmax(data: list) -> tuple:
    # assign the first index as a min and max
    minNum: int = data[0]
    maxNum: int = data[0]

    for i in data:
        if i > maxNum:
            maxNum = i
        elif i < minNum:
            minNum = i
    return (minNum, maxNum)
