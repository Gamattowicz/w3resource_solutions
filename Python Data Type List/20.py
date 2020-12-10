''' Python 3.9
10.12.2020

Write a Python function to reverse a string if it's length is a multiple
of 4.'''


def main(s):
    if len(s) % 4 == 0:
        return s[::-1]


print(main('spam'))
