''' Python 3.9
13.11.2020

Write a Python program to get the size of a file.
Go to the editor'''

import os


def size(name):
    return 'The size of {} is {}B'.format(name, os.path.getsize(name))


print(size('7.py'))
