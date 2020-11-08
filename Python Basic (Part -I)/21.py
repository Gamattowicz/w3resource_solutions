''' Python 3.9
8.11.2020

Write a Python program to find whether a given
number (accept from the user) is even or odd,
print out an appropriate message to the user.
Go to the editor'''


def test_number():
    num = int(input('Enter your number: '))
    if num % 2 == 0:
        return '{} is an even number'.format(num)
    return '{} is an odd number'.format(num)


print(test_number())
