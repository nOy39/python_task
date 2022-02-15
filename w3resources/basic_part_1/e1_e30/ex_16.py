# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

# num = input('Enter number: ')
# if int(num) <= 17:
#     print(f'Difference between 17 and {num} is {17 - int(num)}')
# else:
#     print(f'Double difference between 17 and {num} is {abs(17-int(num))*2}')

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n-17) * 2


print(difference(14))
print(difference(22))
