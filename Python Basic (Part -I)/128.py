''' Python 3.9
24.11.2020

Write a Python program to check whether lowercase letters exist in a string.'''


def main(s):
    for i in s:
        if i.islower():
            return True
    return False


print(main('SPAM12'))
