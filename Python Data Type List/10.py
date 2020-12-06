''' Python 3.9
6.12.2020

Write a Python program to change a given string to a new string where the
first and last chars have been exchanged.'''


def main(s):
    return s[-1] + s[1:-1] + s[0]


print(main('sprint'))
