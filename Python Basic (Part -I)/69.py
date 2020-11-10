''' Python 3.9
10.11.2020

Write a Python program to sort three integers without using conditional
statements and loops. Go to the editor'''


def sort(list):
    a = min(list)
    b = max(list)
    c = sum(list) - a - b
    return 'Sorted numbers: {} {} {}'.format(a, b, c)


print(sort([3, 5, 1]))
