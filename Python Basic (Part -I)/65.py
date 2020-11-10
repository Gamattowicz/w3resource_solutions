''' Python 3.9
10.11.2020

Write a Python program to convert seconds to day, hour, minutes and seconds.
Go to the editor'''


def time_s():
    s = int(input('Enter time in seconds: '))
    d = s // (24 * 3600)
    s = s % (24 * 3600)
    h = s // 3600
    s = s % 3600
    m = s // 60
    s = s % 60
    return '{} days, {} hours, {} minutes, {} seconds'.format(d, h, m, s)


print(time_s())
