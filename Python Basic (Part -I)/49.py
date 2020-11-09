''' Python 3.9
9.11.2020

Write a Python program to list all files in a directory in Python.
Go to the editor'''

import os
import os.path


def list(name):
    dir = []
    for i in os.listdir(name):
        if os.path.isfile(os.path.join(name, i)):
            dir.append(i)
    return dir


print(list('C:\Programming\Python\Exercise\w3resource\Python Basic (Part -I)'))
