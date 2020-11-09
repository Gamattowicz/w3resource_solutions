''' Python 3.9
9.11.2020

Write a Python program to add two objects if both
objects are an integer type. Go to the editor'''


def checking(a, b):
    if (isinstance(a, int)) and (isinstance(b, int)):
        return a + b
    raise TypeError('You must enter a integer values')


print(checking(1, 5))
