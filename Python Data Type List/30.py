''' Python 3.9
12.12.2020

Write a Python program to print the following floating numbers upto 2 decimal
places.'''


def fl():
    ft = float(input('Enter your number: '))
    print('{:.2f}'.format(ft))


fl()
