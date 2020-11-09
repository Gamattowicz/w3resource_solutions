''' Python 3.9
9.11.2020

Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20. Go to the editor'''


def sum(a, b):
    sum = a + b
    if 15 < sum < 20:
        return 20
    return sum


print(sum(5, 8))
