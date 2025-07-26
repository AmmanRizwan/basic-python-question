"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
"""

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
