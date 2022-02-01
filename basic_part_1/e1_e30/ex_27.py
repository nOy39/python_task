# Write a Python program to concatenate all elements in a list into a string and return it.

list = (1, 5, 12, 2)


def concatenate(_list):
    _str = ''
    for i in list:
        _str += str(i)
    return _str


string = concatenate(list)
print(string)
