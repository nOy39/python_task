"""TODO test by linux and windows"""
"""Write a python program to get the path and name of the file that is currently executing."""


from os import path

filename = path.relpath(__file__)
path_to_file = path.abspath(filename)
print('Current file name: ', path_to_file)
