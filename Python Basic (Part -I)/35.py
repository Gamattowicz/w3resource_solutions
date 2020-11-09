''' Python 3.9
9.11.2020

Write a Python program that will return true if the
two given integer values are equal or their sum or
difference is 5. Go to the editor'''


def sum(a, b):
    dif = abs(a-b)
    sum = a + b
    return a == b or dif == 5 or sum == 5


print(sum(5, 1))
