import random

def my_choice(data: list) -> int:
    if not data:
        raise IndexError("cannot choose from an empty sequence")
    index = random.randrange(len(data))
    return data[index]