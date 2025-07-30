### Solve Question



>1. Write a short Python function, `is_multiple(n, m)`, that takes two integer
>
>   values and returns. True if n is a multiple of m, that is, n = mi for some 
>
>   integer i and False otherwise



```python
def is_multiple(n: int, m: int) -> bool:
	if n % m == 0:
		return True
	else:
		return False
```

>2. Write a short Python function, `is_even(k)`, that takes an integer value and
>
>   return True if k is even, and False otherwise. However, your function cannot use
>
>   the multiplication, module, or division operators.



```python
def is_even(k: int) -> bool:
    if k & 1 == 0:
        return True
    else:
        return False
```

> 3. Write a short Python function, `minmax(data)`, that takes a sequence of 
>
>    one or more numbers, and returns the smallest and largest numbers, in the
>
>    form of a tuple of length two. Do not use the built-in functions min or 
>
>    max in implementing your solution



```python
def minmax(data: list) -> tuple:
    minNum: int = data[0]
    maxNum: int = data[0]
    
    for i in data:
        if i > maxNum:
            maxNum = i
        elif i < minNum:
            minNum = i
    return (minNum, maxNum)
```

> 4. Write a short Python function that takes a positive integer n and returns
>
>    the sum of the squares of all the positive integer smaller than n.



```python
def sum_squares(num: int) -> list | str:
    listNum: list = []
    if num <= 0:
        return "Please Enter a positive Number"
    else:
        for i in range(num, 0, -1):
            listNum.append(i * i)
	return listNum
```

> 5. Give a single command that computes the sum from Question No. 4, relying
>
>    on Python's comprehension syntax and the built-in sum function.



```python
def sum_of_all_sequares(num: int) -> int | str:
    listNum: list | str = sum_squares(num)
    if type(listNum) == list:
        return sum(listNum)
    else:
        return listNum
```

> 6. Write a short Python function that takes a positive integer n and returns
>
>    the sum of the squares of all the odd positive integers smaller than n.



```python
def sum_of_all_squares_odd(num: int) -> int | str:
    listNum: list = []
    if num <= 0:
        return "Please Enter a Positive Number"
    else:
        for i in range(num, 0, -1):
            if i & 1 != 0:
                listNum.append(i)
    return sum(listNum)
```

> 7. Give a single command that computes the sum from Question No. 6 relying
>
>    on Python's comprehension syntax and the built-in sum function

```python
def sum_of_all_squares_odd_one_line(num: int) -> int:
    return sum(x ** 2 for x in range(num, 0, -1) if x & 1 != 0)
```



> 9. What parameters should be sent to the range constructor, to produce a 
>
>    range with values 50, 60, 70, 80

```python
def custom_rangeV1() -> list:
    listNum: list = []
    for i in range(50, 81, 10):
        listNum.append(i)
    return listNum
```



> 10. What parameters should be sent to the range constructor, to produce a 
>
>     range with values 8, 6, 4, 2, 0, -2, -4, -6, -8?

```python
def custom_rangeV2() -> list:
    listNum: list = []
    for i in range(8, -9, -2):
        listNum.append(i)
    return listNum
```



> 11. Demonstrate how to use Python's list comprehension syntax to produce
>
>     the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

```python
def list_of_square_compress() -> list:
    return [x ** 2 for x in range(1, 10, 2)]
```



> 12. Python's random module include a function choice(data) that return a
>
>     random element from a non-empty sequence. The random module in-
>
>     clude a more basic function randrange, with parameterization similar to
>
>     the built-in range function, that return a random choice from the given
>
>     range. Using only the randrange function, implement your own version
>
>     of the choice function.

```python
def my_choice(data: list) -> int:
    if not data:
        raise IndexError("cannot choose from an empty sequence")
    index = random.randrange(len(data))
    return data[index]
```



> 13. Write a pseudo-code description of a function that reverses a list of n
>
>     integers, so that the numbers are listed in the opposite order than they 
>
>     were before, and compare this method to an equivalent Python function 
>
>     for doing the same thing.

```python
def reverse_list(data: list) -> list:
    # Create an empty list that will store data in reverse
    listNum: list = []
    
    # Loop through the data into reverse order
    for i in range(len(data) - 1, 0, -1):
        # Store the data into the empty list
        listNum.append(i)
    
    return listNum
```

> 24. Write a short Python function that counts the number of vowels in a given
>     character string.

```python
def count_vowels(data: str) -> int:
    vowel = 'aeiou'
    count = 0
    for i in data:
        if i.lower() in vowel:
            count += 1
    return count
```

> 25. Write a short Python function that takes a string s, representing a sentence,
>     and returns a copy of the string with all punctuation removed. For example,
>     if given the string "Let's try, Mike.", this function would return
>     "Lets try Mike".

```python
import re

def remove_punctuation(data: str) -> str:
    return re.sub(r'[^\w\s]', '', data)
```

> 26. Write a short program that takes as input three integers, a, b, and c, from
>     the console and determines if they can be used in a correct arithmetic
>     formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”

```python
def determine_the_equation() -> bool:
    try:
        correct_arith: bool | None = None
        a = int(input("Enter a integer for a: "))
        b = int(input("Enter a integer for b: "))
        c = int(input("Enter a integer for c: "))

        if a + b == c:
            correct_arith = True
        elif b - c == a:
            correct_arith = True
        elif a * b == c:
            correct_arith = True
        else:
            correct_arith = False
        return correct_arith

    except ValueError:
        print("Please Enter a Valid Integer")
```

