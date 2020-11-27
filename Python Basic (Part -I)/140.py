''' Python 3.9
27.11.2020

Write a Python program to convert an integer to binary keep leading zeros.

Sample data : x=12
Expected output : 00001100
0000001100'''


def main(n):
    return "{0:08b}\n{0:010b}".format(n, n)


print(main(12))
