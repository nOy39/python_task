"""
    In this kata you are required to, given a string, replace every letter with its position in the alphabet.
    If anything in the text isn't a letter, ignore it and don't return it.

    "a" = 1, "b" = 2, etc.
"""


from collections import *
def alphabet_position(text):
    pass


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alphabet)
dict_alpha = OrderedDict.fromkeys(alpha_list)
print(dict_alpha)
