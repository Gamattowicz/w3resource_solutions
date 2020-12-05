''' Python 3.9
5.12.2020

Write a Python function that takes a list of words and returns the length of
the longest one.'''


def main(list):
    result = ''
    for i in list:
        if len(i) > len(result):
            result = i
    return result


print(main(['something', 'spam', 'egg']))
