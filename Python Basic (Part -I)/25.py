''' Python 3.9
8.11.2020

Write a Python program to check whether a specified
value is contained in a group of values.
Go to the editor
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''


def check(list, num):
    return num in list


print(check([3, 7, 5], 4))
