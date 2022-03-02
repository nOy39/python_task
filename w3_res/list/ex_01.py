"""Write a Python program to sum all the items in a list."""


def sum_list_values(lst: list):
    result = 0
    for i in lst:
        result += i
    return result


print(sum_list_values([1, 2, 3, 4, 5]))
