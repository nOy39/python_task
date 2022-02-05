"""
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
    which is the number of times you must multiply the digits in num until you reach a single digit
"""
import math


# def persistence(n):
#     cycle = 0
#     while n > 9:
#         ls = list(str(n))
#         num_list = list(map(int, ls))
#         n = math.prod(num_list)
#         cycle += 1
#     return cycle


def persistence(n):
    cycle = 0
    while n > 9:
        num_list = list(
            map(int, list(str(n)))
        )
        n = math.prod(num_list)
        cycle += 1
    return cycle


print(persistence(39))
print(persistence(999))
