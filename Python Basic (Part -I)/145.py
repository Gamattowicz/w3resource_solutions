''' Python 3.9
30.11.2020

Write a Python program to test if a variable is a list or tuple or a set.'''


def main(n):
    if type(n) is list:
        print('Variable is a list')
    elif type(n) is set:
        print('Variable is a set')
    elif type(n) is tuple:
        print('Variable is a tuple')
    else:
        print('Variable is not list, nor set, nor tuple.')


main([2, 3])
