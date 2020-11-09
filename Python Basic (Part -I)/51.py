''' Python 3.9
9.11.2020

Write a Python program to determine profiling of
Python programs. Go to the editor
Note: A profile is a set of statistics that describes
how often and for how long various parts of the program
executed. These statistics can be formatted into reports
via the pstats module.'''

import cProfile


def iteraction():
    for i in range(1, 10000, 5):
        print(i*50)


cProfile.run('iteraction()')
