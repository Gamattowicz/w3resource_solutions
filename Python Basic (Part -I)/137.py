''' Python 3.9
27.11.2020

Write a Python program to extract single key-value pair of a dictionary
in variables.'''


def main(d):
    for key, value in d.items():
        print('Key is {}, value is {}'.format(key, value))


main({'Color': 'Blue', 'Shape': 'Heart'})
