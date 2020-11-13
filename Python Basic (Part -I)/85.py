''' Python 3.9
13.11.2020

Write a Python program to check whether a file path is a file or a directory.
Go to the editor'''

import os


def check(name):
    if os.path.isfile(name):
        return "It's file"
    elif os.path.isdir(name):
        return "It's directory"
    else:
        return "It's not file nor directory"


print(check('Python'))
