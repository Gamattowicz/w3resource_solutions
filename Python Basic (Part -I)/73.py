''' Python 3.9
11.11.2020

Write a Python program to calculate midpoints of a line. Go to the editor'''


def mid(a, b):
    x = (a[0] + b[0])/2
    y = (a[1] + b[1])/2
    return "The midpoint's value is {} and y is {}".format(x, y)


print(mid([2, 3], [4, 5]))
