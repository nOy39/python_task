# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def copy_string(str, num):
    result = ""
    for i in range(num):
        result = result + str
    return result


empty_word = copy_string('word ', 4)
print(copy_string('.test', 3))
