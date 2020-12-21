''' Python 3.9
21.12.2020

Write a Python program to find the first repeated character of a given string
where the index of first occurrence is smallest.'''


def repeated_small(s):
    str1 = []
    for i in s:
        if i in str1:
            return i, str1.index(i)
        else:
            str1.append(i)


print(repeated_small('eggs'))
