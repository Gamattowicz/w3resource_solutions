''' Python 3.9
9.11.2020

Write a Python program to sum of three given integers.
However, if two values are equal sum will be zero. Go to the editor'''


def summ(a, b, c):
    if a == b or a == c or b == c:
        return 0
    return (a + b + c)


print(summ(1, 1, 3))
