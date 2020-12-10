''' Python 3.9
10.12.2020

Write a Python function to convert a given string to all uppercase if it
contains at least 2 uppercase characters in the first 4 characters.'''


def main(s):
    up = 0
    for i in s[:4]:
        if i.isupper():
            up += 1
    if up >= 2:
        return s.upper()
    return s


print(main('Spam'))
