"""
Give a single command that computes the sum from Question No. 6 relying
on Python's comprehension syntax and built-in sum function
"""

def sum_of_all_squares_odd_one_line(num: int) -> int:
    return sum(x ** 2 for x in range(num, 0, -1) if x & 1 != 0)
