"""Write a Python program to get the smallest number from a list."""


def smallest_number_of_list(lst: list):
    lst.sort()
    return lst[0]


print(smallest_number_of_list([1, 35, -3, 17, 9, 0]))
