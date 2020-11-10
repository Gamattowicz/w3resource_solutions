''' Python 3.9
10.11.2020

Write a Python program to calculate the sum of the digits in an integer.
Go to the editor'''


def cal():
    n = input('Enter the digits: ')
    sum = 0
    n = [n[i: i+1] for i in range(0, len(n))]
    for i in n:
        sum += int(i)
    return sum


print(cal())
