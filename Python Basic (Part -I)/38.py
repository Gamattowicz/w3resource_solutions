''' Python 3.9
9.11.2020

Write a Python program to solve (x + y) * (x + y). Go to the editor
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49'''


def test(x, y):
    result = (x + y) * (x + y)
    return '({} + {}) ^ 2) = {}'.format(x, y, result)


print(test(4, 3))
