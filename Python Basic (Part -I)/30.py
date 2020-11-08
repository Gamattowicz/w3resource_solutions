''' Python 3.9
8.11.2020

Write a Python program that will accept the base
and height of a triangle and compute the area.
Go to the editor'''


def triangle():
    base = int(input('Enter base of triangle: '))
    height = int(input('Enter height of triangle: '))
    return (0.5*base*height)


print(triangle())
