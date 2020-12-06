''' Python 3.9
6.12.2020

Write a Python program to remove the characters which have odd index values of
a given string.'''


def main(s):
    result = ''
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]
    return result


print(main('spamegg'))
