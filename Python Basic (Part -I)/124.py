''' Python 3.9
23.11.2020

Write a Python program to check whether multiple
variables have the same value.'''


def main(list):
    for i in range(len(list)-1):
        if list[i] != list[i+1]:
            return False
    return True


print(main([2, 2, 2, 2]))
