''' Python 3.9
9.12.2020

Write a Python function to get a string made of 4 copies of the last two
characters of a specified string (length must be at least 2).'''


def main(s):
    if len(s) > 1:
        return s[-2:] * 4


print(main('eggs'))
