''' Python 3.9
20.11.2020

Write a Python program to filter the positive numbers from a list.'''


def positive(num):
    result = [i for i in num if i > 0]
    return result


print(positive([2, 4, -5, 10]))
