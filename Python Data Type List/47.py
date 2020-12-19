''' Python 3.9
19.12.2020

Write a Python program to lowercase first n characters in a string.'''


def lowerString(s, n):
    return s[:n].lower() + s[n:]


print(lowerString('SPAM EGGS', 3))
