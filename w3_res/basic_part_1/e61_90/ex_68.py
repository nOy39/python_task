"""Write a Python program to calculate the sum of the digits in an integer."""
num: int = 123987
sum_of_digits = 0
cycle_count = 0


while num >= 1:
    sum_of_digits = sum_of_digits + num % 10
    num = num // 10

print(f'Sum of the digit is {sum_of_digits}')

