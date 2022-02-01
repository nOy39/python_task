# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

num = input('Enter number: ')


def even_odd(num):
    return 'Number is even' \
        if num % 2 == 0 \
        else 'Number is od'


print(even_odd(int(num)))
