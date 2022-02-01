# Write a Python program which will return true if the two given integer values are equal
# or their sum or difference is 5.

def check_values(num_1, num_2):
    if num_1 == num_2 or \
            num_1 + num_2 == 5 or \
            abs(num_1 - num_2) == 5:
        return True
    else:
        return False


print(check_values(2, 3))
print(check_values(8, 3))
print(check_values(4, 4))
print(check_values(2, 9))
