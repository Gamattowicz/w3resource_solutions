''' Python 3.9
18.11.2020

Write a Python program to extract the filename from a given path.'''

import os


def extr(name):
    return os.path.basename(name)


print(extr('C:\Programming\Python\Exercise\Exercism'))
