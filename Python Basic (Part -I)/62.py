''' Python 3.9
10.11.2020

Write a Python program to convert all units of time into seconds.
Go to the editor'''


def conv_time():
    d = int(input("Input days: "))
    h = int(input("Input hours: "))
    m = int(input("Input minutes: "))
    s = int(input("Input seconds: "))
    time = d * 3600 * 24 + h * 3600 + m * 60 + s

    return '{} seconds'.format(time)


print(conv_time())
