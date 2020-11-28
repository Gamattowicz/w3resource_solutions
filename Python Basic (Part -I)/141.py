''' Python 3.9
28.11.2020

Write a python program to convert decimal to hexadecimal.

Sample decimal number: 30, 4
Expected output: 1e, 04'''


def main(n):
    return '{0:x}'.format(int(n))


print(main(30))
