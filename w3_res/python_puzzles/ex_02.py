"""
Write a Python program that accept a list of integers and check the length and the fifth element. 
Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
"""

arr1 = [11, 12, 14, 13, 14, 13, 15, 14]
arr2 = [11, 12, 14, 13, 14, 13, 15]
arr3 = [11, 12, 14, 13, 14, 13, 1, 14]


def check_array(arr):
    return True if len(arr) == 8 and arr.count(arr[4]) >= 3 else False


print(check_array(arr1))
print(check_array(arr2))
print(check_array(arr3))
