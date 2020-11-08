''' Python 3.9
8.11.2020

Write a Python program which accepts a sequence of comma-separated
numbers from user and generate a list and a tuple with those numbers.
Go to the editor
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23') '''


num = input('Enter a numbers: ')


list = list(num.split(', '))
tuple = tuple(list)

print('List: {}'.format(list))
print('Tuple: {}'.format(tuple))
