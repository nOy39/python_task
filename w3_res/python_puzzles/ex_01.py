"""
Write a Python program find a list of 
integers with exactly two occurrences of nineteen and at least three occurrences of five.
"""


arr1 = [19, 18, 5, 5, 5, 5, 5]
arr2 = [19, 19, 5, 5, 2, 3, 4]
arr3 = [19, 19, 5, 5, 5]


def list_of_num(arr):
    return True if arr.count(19) == 2 and arr.count(5) >= 3 else False


print(list_of_num(arr1))
print(list_of_num(arr2))
print(list_of_num(arr3))
