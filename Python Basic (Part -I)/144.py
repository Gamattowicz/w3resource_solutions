''' Python 3.9
30.11.2020

Write a Python program to check whether a variable is integer or string.'''


def main(n):
    return (isinstance(n, int) or isinstance(n, str))


print(main('n'))
