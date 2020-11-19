''' Python 3.9
19.11.2020

Write a Python program to remove the first item from a specified list.'''


def rem(list):
    del list[0]
    return list


print(rem([5, 10, 15]))
