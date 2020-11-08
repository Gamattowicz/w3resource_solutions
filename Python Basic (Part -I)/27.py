''' Python 3.9
8.11.2020

Write a Python program to concatenate all elements
in a list into a string and return it.
Go to the editor'''


def stick(list):
    result = ''
    for i in list:
        result += str(i)
    return result


print(stick([4, 5, 7]))
