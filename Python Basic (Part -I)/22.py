''' Python 3.9
8.11.2020

Write a Python program to count the number
4 in a given list. Go to the editor'''


def counting(list):
    count = 0
    for i in list:
        if i == 4:
            count += 1
    return count


print(counting([10, 4, 22, 4, 25]))
