''' Python 3.9
13.11.2020

Given variables x=30 and y=20, write a Python program to print "30+20=50".
Go to the editor'''


def main():
    X = int(input('Enter value of X: '))
    Y = int(input('Enter value of Y: '))
    return '{} + {} = {}'.format(X, Y, (X + Y))


print(main())
