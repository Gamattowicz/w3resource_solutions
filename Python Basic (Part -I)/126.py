''' Python 3.9
23.11.2020

Write a Python program to get the actual module object for a given object.'''


from inspect import getmodule

import random

print(getmodule(random.randrange))
