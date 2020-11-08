''' Python 3.9
7.11.2020

Write a Python program which accepts the radius of a
circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504 '''

import math

r = float(input('Enter the radius of circle: '))

area = math.pi * pow(r, 2)

print('Area of the circle is {}'.format(area))
