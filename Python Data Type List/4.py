''' Python 3.9
4.12.2020

Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except
the first char itself.'''


def rep(s):
    return s[0] + s[1:].replace(s[0], '$')


print(rep('spamspamspam'))
