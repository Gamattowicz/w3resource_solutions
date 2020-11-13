''' Python 3.9
13.11.2020

Write a Python program to count the number occurrence of a specific character
in a string. Go to the editor'''


def calc():
    str = input('Enter your string: ')
    s = input('Enter your character: ')
    return str.count(s)


print(calc())
