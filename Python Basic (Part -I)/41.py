''' Python 3.9
9.11.2020

Write a Python program to check whether a file exists. Go to the editor'''

import os


def file_check(name):
    return os.path.isfile(name)


print(file_check('7.py'))
