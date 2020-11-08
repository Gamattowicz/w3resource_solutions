''' Python 3.9
8.11.2020

Write a Python program to test whether a passed
letter is a vowel or not. Go to the editor'''


def vowel(s):
    vowels = 'aeiou'
    return s.lower() in vowels


print(vowel('c'))
