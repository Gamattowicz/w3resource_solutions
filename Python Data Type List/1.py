''' Python 3.9
3.12.2020

Write a Python program to sum all the items in a list.'''

list = [1, 2, 5, 7]


def main(list):
    result = 0
    for i in list:
        result += i
    return result


print(main(list))
