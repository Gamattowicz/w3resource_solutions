''' Python 3.9
10.11.2020

Write a Python program to convert pressure in kilopascals
to pounds per square inch, a millimeter of mercury
(mmHg) and atmosphere pressure. Go to the editor'''


def cal():
    p = float(input('Enter pressure in kilopascals: '))
    psi = round((p / 6.89475729), 2)
    mmhg = round(p * 760 / 101.325, 2)
    atm = round(p / 101.325, 2)

    print('Pressure in pounds per square inch is {}'.format(psi))
    print('Pressure in mmillimeter of mercury is {}'.format(mmhg))
    print('Atmosphere pressure is {}'.format(atm))


cal()
