''' Python 3.9
8.11.2020

Write a Python program to accept a filename from the
user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java '''

name = input('Enter the filename: ')
filename = name.split('.')
print(filename[1])
