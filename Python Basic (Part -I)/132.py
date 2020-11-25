''' Python 3.9
25.11.2020

Write a Python program to list home directory without absolute path.'''

import os.path

print(os.path.expanduser('~'))
