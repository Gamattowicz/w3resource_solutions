''' Python 3.9
6.12.2020

Write a Python program to remove the nth index character from a nonempty
string.'''


def main(s, n):
    return s[:n] + s[n+1:]


print(main('spam', 3))
