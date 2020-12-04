''' Python 3.9
4.12.2020

Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string'''


def main(s1, s2):
    s1, s2 = s2[0:2] + s1[2:], s1[:2] + s2[2:]
    return '{} {}'.format(s1, s2)


print(main('spam', 'egg'))
