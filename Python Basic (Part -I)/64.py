''' Python 3.9
10.11.2020

Write a Python program to get file creation and
modification date/times. Go to the editor'''

import os.path
import time


def check(name):
    print('Last time modified: {}'.format(time.ctime(os.path.getmtime(name))))
    print('Created: {}'.format(time.ctime(os.path.getctime(name))))


check('7.py')
