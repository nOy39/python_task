# 36. Write a Python program to add two objects if both objects are an integer type.

def add_numbers(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        return 'Inputs must be integers!'


print(add_numbers(3, 5))
print(add_numbers(3, 20.23))
print(add_numbers(3, '5'))
print(add_numbers('3', '5'))
