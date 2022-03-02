"""
Write a Python program to multiply all the items in a list.
"""


def multiple_values_of_list(lst: list):
    mult = 1
    for n in lst:
        mult *= n
    return mult


print(multiple_values_of_list([1, 2, 3]))
