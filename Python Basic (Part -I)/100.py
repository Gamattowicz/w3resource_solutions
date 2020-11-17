''' Python 3.9
17.11.2020

Write a Python program to get the name of the host on which the routine
is running.'''

import socket
host = socket.gethostname()

print(host)
