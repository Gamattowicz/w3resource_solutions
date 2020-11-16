''' Python 3.9
16.11.2020

Write a Python program to convert a byte string to a list of integers.'''


def B_int(B):
    n = bytes(B, 'utf-8')
    return list(n)


print(B_int('Abc'))
