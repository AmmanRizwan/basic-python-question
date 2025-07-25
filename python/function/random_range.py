"""
Python's random module include a function choice(data) that return a
random element from a non-empty sequence. The random module include
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""

import random

def my_choice(data: list) -> int:
    if not data:
        raise IndexError("cannot choose from an empty sequence")
    index = random.randrange(len(data))
    return data[index]