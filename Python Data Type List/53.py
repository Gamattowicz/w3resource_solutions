''' Python 3.9
21.12.2020

Write a Python program to find the first repeated character in a given
string.'''


def repeated(s):
    str1 = []
    for i in s:
        if i in str1:
            return i
        else:
            str1.append(i)


print(repeated('eggs'))
