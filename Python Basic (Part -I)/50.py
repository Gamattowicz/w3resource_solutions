''' Python 3.9
9.11.2020

Write a Python program to print without newline or space. Go to the editor'''


def printing(s):
    print(s.replace('\n', '').replace(' ', ''))


printing('there is something\n even')
