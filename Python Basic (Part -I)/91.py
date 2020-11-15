''' Python 3.9
15.11.2020

Write a Python program to swap two variables.'''


def swap(a, b):
    a, b = b, a
    return '{} its a, {} its b'.format(a, b)


print(swap('spam', 'meat'))