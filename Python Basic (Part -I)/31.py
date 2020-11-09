''' Python 3.9
9.11.2020

Write a Python program to compute the greatest common
divisor (GCD) of two positive integers. Go to the editor'''


def gcd(n1, n2):
    divisor1 = []
    divisor2 = []
    for i in range(1, n1+1):
        if n1 % i == 0:
            divisor1.append(i)
    for i in range(1, n2+1):
        if n2 % i == 0:
            divisor2.append(i)
    return max(set(divisor1) & set(divisor2))


print(gcd(15, 30))
