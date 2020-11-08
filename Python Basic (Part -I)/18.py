''' Python 3.9
8.11.2020

Write a Python program to calculate the sum of three
given numbers, if the values are equal then return
three times of their sum. Go to the editor '''


def sum_three(a, b, c):
    if a == b == c:
        return a*3
    return a + b + c


print(sum_three(1, 1, 1))
