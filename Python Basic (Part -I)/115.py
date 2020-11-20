''' Python 3.9
20.11.2020

Write a Python program to compute the product of a list of integers
(without using for loop).'''


def product(list):
    if not list:
        return 1
    else:
        return list[0] * product(list[1:])


print(product([10, 20, 30]))
