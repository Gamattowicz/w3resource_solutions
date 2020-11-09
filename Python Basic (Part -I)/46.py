''' Python 3.9
9.11.2020

Write a python program to get the path and name of
the file that is currently executing. Go to the editor'''

import os

print(os.path.realpath(__file__))
