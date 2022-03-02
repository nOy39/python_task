# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.
def create_new_string(_str, num):
    _new_str = _str[:2] * num if len(_str) > 2 else _str * num
    return _new_str


string = 'i'
new_string = create_new_string(string, 5)
print(new_string)
