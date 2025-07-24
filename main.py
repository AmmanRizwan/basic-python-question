"""
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns. True if n is a multiple of m, that is, n = mi for some
integer i and False otherwise
"""

def is_multiple(n: int, m: int) -> bool:
    if n % m == 0:
        return True
    else:
        return False


"""
Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function cannot use
the multiplication, modulo, or division operators.
"""

def is_even(k: int) -> bool:
    if k & 1 == 0:
        return True
    else:
        return False

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

# New
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