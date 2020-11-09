''' Python 3.9
9.11.2020

Write a Python program to get the least common
multiple (LCM) of two positive integers. Go to the editor'''


def lcm(n1, n2):
    if n1 > n2:
        m = n1
    else:
        m = n2

    while True:
        if m % n1 == 0 and m % n2 == 0:
            break
        m += 1
    return m


print(lcm(5, 19))
