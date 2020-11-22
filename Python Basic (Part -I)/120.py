''' Python 3.9
22.11.2020

Write a Python program to format a specified string to limit the number
of characters to 6.'''


def st(s):
    return '{:.6s}'.format(s)


print(st('wasdfghjkzx'))
