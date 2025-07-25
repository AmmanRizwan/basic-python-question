from sum_squares import sum_squares

"""
Give a single command that computes the sum from Question No. 4, relying
on Python's comprehension syntax and the built-in sum function.
"""

def sum_of_all_squares(num: int) -> int | str:
    listNum: list | str = sum_squares(num)
    if type(listNum) == list:
        return sum(listNum)
    else:
        return listNum
