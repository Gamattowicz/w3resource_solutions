''' Python 3.9
10.11.2020

Write a program to get execution time for a Python method. Go to the editor'''

import time


def some_test():
    start = time.time()
    result = 0
    for i in range(1000):
        result += i ** 2 + i**3 + i**523
    end = time.time()
    return result, end - start


print(some_test())
