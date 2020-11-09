''' Python 3.9
9.11.2020

Write a Python program to compute the distance between
the points (x1, y1) and (x2, y2). Go to the editor'''

import math


def distance(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2 ))


print(distance([4, 0], [6, 6]))
