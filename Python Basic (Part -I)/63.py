''' Python 3.9
10.11.2020

Write a Python program to get an absolute file path. Go to the editor'''

import os


def abs_path(name):
    return os.path.abspath(name)


print(abs_path('7.py'))
