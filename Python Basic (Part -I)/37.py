''' Python 3.9
9.11.2020

Write a Python program to display your details like
name, age, address in three different lines. Go to the editor'''


def info():
    name = 'Przemek'
    age = 25
    address = 'Cracov'

    return 'Name: {}\nAge: {}\nAddress: {}'.format(name, age, address)


print(info())
