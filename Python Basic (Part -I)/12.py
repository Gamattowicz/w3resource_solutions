''' Python 3.9
8.11.2020

Write a Python program to print the calendar
of a given month and year.
Note : Use 'calendar' module. '''

import calendar

y = int(input('Enter year: '))
m = int(input('Enter month: '))

print(calendar.month(y, m, w=5, l=2))
