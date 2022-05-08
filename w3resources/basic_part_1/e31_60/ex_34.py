# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def check_sum(num_1, num_2):
    sum = num_1 + num_2
    return sum \
        if sum not in range(15, 20) \
        else 20


print(check_sum(12, 11))
print(check_sum(5, 11))
print(check_sum(9, 3))