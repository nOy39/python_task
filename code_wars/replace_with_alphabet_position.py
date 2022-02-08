"""
    In this kata you are required to, given a string, replace every letter with its position in the alphabet.
    If anything in the text isn't a letter, ignore it and don't return it.

    "a" = 1, "b" = 2, etc.
"""


from collections import *

#
# def alphabet_position(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     list_of_char = list(text)
#     result = list()
#     for c in list_of_char:
#         if c.isalpha():
#             result.append(alphabet.find(c.lower()))
#     return " ".join(str(e) for e in result)


def alphabet_position(text):
    return " ".join(str(ord(c.lower()) - 96) for c in text if c.isalpha())


print(alphabet_position('Aneofthi'))
print(alphabet_position('The sunset sets at twelve o\'clock.'))
print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
