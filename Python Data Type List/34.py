''' Python 3.9
14.12.2020

Write a Python program to print the following integers with '*' on the right
of specified width.'''


def stars():
    num = input('Enter your number: ')
    print(num+'*'*len(num))


stars()
