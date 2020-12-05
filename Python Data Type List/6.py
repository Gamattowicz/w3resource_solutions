''' Python 3.9
5.12.2020

Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead. If the string length of the given string is less than 3, leave
it unchanged.'''


def main(s):
    if s.endswith('ing'):
        return s+'ly'
    elif len(s) >= 3:
        return s+'ing'
    return s


print(main('seng'))
