''' Python 3.9
8.11.2020

Write a Python program to get the n (non-negative
integer) copies of the first 2 characters of a
given string. Return the n copies of the whole
string if the length is less than 2. Go to the editor'''


def copy(str, n):
    if len(str) < 2:
        return str*n
    return str[:2]*n


print(copy('surdut', 3))
