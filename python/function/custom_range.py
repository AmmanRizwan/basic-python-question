"""
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80
"""

def custom_rangeV1() -> list:
    listNum: list = []
    for i in range(50, 81, 10):
        listNum.append(i)
    return listNum

def custom_rangeV2() -> list:
    listNum: list = []
    for i in range(8, -9, -2):
        listNum.append(i)
    return listNum

print(custom_rangeV2())