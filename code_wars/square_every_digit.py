"""In this kata, you are asked to square every digit of a number and concatenate them.

    For example, if we run 9119 through the function, 811181 will come out,
    because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer"""


# My
def square_digits(num):
    result = ''
    for i in num.__str__():
        result += int(i).__pow__(2).__str__()
    return int(result)

    print(result)


square_digits(9119)
print("END")
