# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.

def numbers(fNumber, sNumber, thNumber):
    sum = fNumber + sNumber + thNumber
    if fNumber == sNumber == thNumber:
        return sum * 3
    else:
        return sum


print(numbers(1, 2, 3))
print(numbers(2, 2, 2))
