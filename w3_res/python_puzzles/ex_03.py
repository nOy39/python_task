"""
Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
"""


def check_number(num):
    return 4 ** 4 < num and num % 34 == 4


print(check_number(854))
print(check_number(922))
print(check_number(914))
