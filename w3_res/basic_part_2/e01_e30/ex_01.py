"""
Write a Python function that takes a sequence of numbers and determines whether
all the numbers are different from each other.
"""

"""
Solution:
Сравниваю длину массива с длинной этого массива переведенного в множество SET
"""


def determine(arr):
    return True if len(arr) == len(set(arr)) else False


print(determine([2, 3, 4, 5, 6, 9]))
print(determine([2, 4, 7, 7, 0]))
print(determine([4, 5, 1, 0, 11, 8]))
