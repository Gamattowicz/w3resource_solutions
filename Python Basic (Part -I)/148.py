''' Python 3.9
1.12.2020

Write a Python function to find the maximum and minimum numbers from a
sequence of numbers.
Note: Do not use built-in functions.'''


def main(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i > max:
            max = i
        elif i < min:
            min = i
    return max, min


print(main([1, 2, 4, 7, 10]))
