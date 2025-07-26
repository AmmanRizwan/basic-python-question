"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""

import random

def permutation_string() -> list:
    character: list = ['c', 'a', 't', 'd', 'o', 'g']
    listString: list = []

    for char in range(len(character) * len(character)):
        text = ''
        for form_char in range(len(character)):
            text += random.choice(character)
        listString.append(text)

    return listString