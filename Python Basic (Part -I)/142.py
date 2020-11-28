''' Python 3.9
28.11.2020

Write a Python program to find the operating system name, platform and
platform release date.'''

import os, platform

print('Operating system name is {}'.format(os.name))
print('Platform name is {}'.format(platform.system()))
print('Platform release is {}'.format(platform.release()))
