''' Python 3.9
8.11.2020

Write a Python program to get a new string from
a given string where "Is" has been added to the
front. If the given string already begins with
"Is" then return the string unchanged. Go to the editor'''


def new_string(s):
    if s.startswith('Is'):
        return s
    return 'Is'+s


print(new_string('lscos'))
