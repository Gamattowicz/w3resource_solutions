''' Python 3.9
13.12.2020

Write a Python program to print the following floating numbers with no decimal
places.'''


def no():
    num = float(input('Enter your number: '))
    print('{:.0f}'.format(num))


no()
