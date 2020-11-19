''' Python 3.9
19.11.2020

Write a Python program to check if a number is positive, negative or zero.'''


def check_num(num):
    if num > 0:
        return "It's positive number"
    elif num == 0:
        return "It's zero"
    return "It's negative number"


print(check_num(5))
