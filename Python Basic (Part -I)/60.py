''' Python 3.9
10.11.2020

Write a Python program to calculate the hypotenuse
of a right angled triangle. Go to the editor'''

import math


def hypo(a, b):
    return 'The lenght of the hypotenuse of triangle is {}'.format(math.sqrt(a**2 + b**2))


print(hypo(3, 4))
