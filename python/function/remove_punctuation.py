"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""

import re

def remove_punctuation(data: str) -> str:
    return re.sub(r'[^\w\s]', '', data)