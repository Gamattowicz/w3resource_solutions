''' Python 3.9
10.11.2020

Write a Python to find local IP addresses using Python's
stdlib Go to the editor'''

import socket

print(socket.gethostbyname(socket.gethostname()))
