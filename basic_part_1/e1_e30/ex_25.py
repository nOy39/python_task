# 25. Write a Python program to check whether a specified value is contained in a group of values.

array = [1, 3, 5, 9, 13]
num = 5


def test_data(_arr, _num):
    _str = f'num -> {array} : '
    result = num in array
    return _str + str(result)


print(test_data(array, num))
