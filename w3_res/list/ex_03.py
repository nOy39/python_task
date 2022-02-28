"""Write a Python program to get the largest number from a list."""


def largest_number_of_list(lst: list):
    lst.sort()
    return lst[-1]


print(largest_number_of_list([1, 35, -3, 17, 9, 0]))
