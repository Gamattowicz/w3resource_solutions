''' Python 3.9
19.11.2020

Write a Python program to input a number, if it is not a number generate
an error message.'''


def func():
    while True:
        try:
            n = int(input('Input a number: '))
            print("{} is a number".format(n))
            break
        except ValueError:
            print("It's not a number!")


func()
