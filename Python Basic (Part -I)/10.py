''' Python 3.9
8.11.2020

Write a Python program that accepts an integer (n)
and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615 '''

num = input('Enter a digital: ')
result = int(num) + int(num+num) + int(num+num+num)
print(result)
