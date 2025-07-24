"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integer smaller than n.
"""

def sum_squares(num: int) -> list | str:
    listNum: list = []
    if num <= 0:
        return "Please Enter a Positive Number"
    else:
        for i in range(num, 0, -1):
            listNum.append(i*i)
    return listNum
