''' Python 3.9
10.11.2020

Write a Python program to convert height (in feet
and inches) to centimeters. Go to the editor'''


def conv_cm():
    ft = int(input('Enter the height in feets: '))
    inch = int(input('Enter the remaining height in inches: '))
    inch += ft * 12
    return 'Heigh in cm is {}.'.format(round(inch * 2.54, 1))


print(conv_cm())
