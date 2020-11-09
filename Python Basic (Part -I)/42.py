''' Python 3.9
9.11.2020

Write a Python program to determine if a Python shell is
executing in 32bit or 64bit mode on OS. Go to the editor'''

import struct

print(struct.calcsize('P')*8)
