''' Python 3.9
10.11.2020


Write a Python program to convert the distance (in feet) to inches, yards,
and miles. Go to the editor'''


def conv(ft):
    inch = ft * 12
    yd = ft/3
    ml = ft/5280
    print('The distance in inches is {}'.format(inch))
    print('The distance in yards is {}'.format(yd))
    print('The distance in miles is {}'.format(ml))


conv(5)
