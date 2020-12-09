''' Python 3.9
9.12.2020

Write a Python function to get a string made of its first three characters
of a specified string. If the length of the string is less than 3 then return
the original string.'''


def main(s):
    if len(s) >= 3:
        return s[:3]
    return s


print(main('eggs'))

print(main('es'))
