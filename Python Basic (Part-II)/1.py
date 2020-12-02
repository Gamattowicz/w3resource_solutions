''' Python 3.9
2.12.2020

Write a Python function that takes a sequence of numbers and determines
whether all the numbers are different from each other.'''


def main(l1):
    return len(l1) == len(set(l1))


print(main([1, 2, 3, 2]))
