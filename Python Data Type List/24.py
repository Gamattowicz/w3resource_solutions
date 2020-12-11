''' Python 3.9
11.12.2020

Write a Python program to check whether a string starts with specified
characters.'''


def main(s, char):
    return s.startswith(char)


print(main('eggs', 'e'))
