''' Python 3.9
10.11.2020

Write a Python program to sort files by date. Go to the editor'''

import os
import glob

list = glob.glob('*.py')
list.sort(key=os.path.getmtime)
for i in list:
    print(i)
