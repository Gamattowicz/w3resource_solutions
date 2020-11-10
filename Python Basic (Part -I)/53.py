''' Python 3.9
10.11.2020

Write a python program to access environment variables. Go to the editor'''

import os


print(os.environ, '\n')

print(os.environ['USERPROFILE'], '\n')

os.environ['NEW VAR'] = 'THIS IS NEW VAR'
print('NEW VAR: ', os.environ['NEW VAR'])
