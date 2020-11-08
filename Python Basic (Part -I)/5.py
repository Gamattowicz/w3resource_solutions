''' Python 3.9
7.11.2020

Write a Python program which accepts the user's first
and last name and print them in reverse order with a space between them.  '''

name = input('Enter your First and Last Name: ')
name = name.split(' ')
print('Hi {} {}'.format(name[1], name[0]))
