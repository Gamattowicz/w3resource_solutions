''' Python 3.9
10.11.2020

Write a python program to find the sum of the first
n positive integers. Go to the editor'''


def sum():
    num = int(input('Enter number: '))
    result = 0
    for i in range(1, num + 1):
        result += i
    return result


print(sum())
