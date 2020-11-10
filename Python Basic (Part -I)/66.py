''' Python 3.9
10.11.2020

Write a Python program to calculate body mass index. Go to the editor'''


def bmi():
    w = float(input('Enter your weight in kilograms: '))
    h = float(input('Enter your height in meters: '))
    return 'Your body mass index is: {}'.format(round(w / (h ** 2), 2))


print(bmi())
