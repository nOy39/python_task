# Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero.

def print_sum(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 \
        if num_1 != num_2 and num_1 != num_3 and num_2 != num_3\
        else 0


print(print_sum(1, 1, 2))
print(print_sum(2, 6, 9))
print(print_sum(2, 2, 2))
