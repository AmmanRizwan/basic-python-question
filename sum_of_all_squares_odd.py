"""
Write a short Python function that takes a positive integer n and return
the sum of the square of all the odd positive integers smaller than n
"""

def sum_of_all_squares_odd(num: int) -> int | str:
    listNum: list = []
    if num <= 0:
        return "Please Enter a Positive Number"
    else:
        for i in range(num, 0, -1):
            if i & 1 != 0:
                listNum.append(i)
    return sum(listNum)