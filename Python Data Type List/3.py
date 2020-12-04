''' Python 3.9
4.12.2020

Write a Python program to get a string made of the first 2 and the
last 2 chars from a given a string. If the string length is less than
2, return instead of the empty string.'''


def main(s):
    if len(s) >= 2:
        return s[0:2] + s[-2:]
    return ''


print(main('s'))
