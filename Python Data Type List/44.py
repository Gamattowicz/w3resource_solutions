''' Python 3.9
18.12.2020

Write a Python program to print the index of the character in a string.'''


def countingChar(s):
    st = enumerate(s)
    for i, j in st:
        print('{} is at {} position'.format(j, i))


countingChar('eggs')
