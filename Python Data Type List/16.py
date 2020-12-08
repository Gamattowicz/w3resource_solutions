''' Python 3.9
8.12.2020

Write a Python function to insert a string in the middle of a string.'''


def main(n1, n2):
    mid = len(n1)//2
    return n1[:mid] + n2 + n1[mid:]


print(main('[[[]]]', 'egg'))
