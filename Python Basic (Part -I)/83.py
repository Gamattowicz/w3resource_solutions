''' Python 3.9
12.11.2020

Write a Python program to test whether all numbers of
a list is greater than a certain number. Go to the editor'''

import random

list = sorted(random.sample(range(1, 100), 7))


def check(list):
    num = int(input('Enter your number: '))
    for i in list:
        if num < i:
            return "Your number {} isn't greater than numbers in list: {}".format(num, list)
    return "Your number {} is greater than numbers in list: {}".format(num, list)


print(check(list))
