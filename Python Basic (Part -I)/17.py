''' Python 3.9
8.11.2020

Write a Python program to test whether a number
is within 100 of 1000 or 2000. Go to the editor'''


def test(num):
    return ((abs(1000 - num) <= 100) or (abs(2000 - num) <= 100))


print(test(800))
