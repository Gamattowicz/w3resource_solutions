''' Python 3.9
2.12.2020

Write a Python function that takes a positive integer and returns the sum of
the cube of all the positive integers smaller than the specified number.

Ex.: 8 = 73+63+53+43+33+23+13 = 784'''


def main(n):
    result = 0
    for i in range(1, n):
        result += pow(i, 3)
    return result


print(main(8))
