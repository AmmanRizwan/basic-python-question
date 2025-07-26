"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

def count_vowels(data: str) -> int:
    vowel = 'aeiou'
    count = 0
    for i in data:
        if i.lower() in vowel:
            count += 1
    return count
