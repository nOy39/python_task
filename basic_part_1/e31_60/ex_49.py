""" Write a Python program to list all files in a directory in Python"""

import os
file_list = os.listdir()
print(*file_list, sep='\n')
