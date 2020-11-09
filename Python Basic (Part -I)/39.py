''' Python 3.9
9.11.2020

Write a Python program to compute the future value of
a specified principal amount, rate of interest, and a
number of years. Go to the editor
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79'''


def fut(amt, int, years):
    return round(amt*((1+(0.01*int)) ** years), 2)


print(fut(10000, 3.5, 7))
