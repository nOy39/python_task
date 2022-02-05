"""In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

    Notes
    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space,
    and highest number is first.
"""

string = "1 2 -3 4 5"
test = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"


# def high_and_low(numbers):
#     arr = []
#     for elem in numbers.split(' '):
#         arr.append(int(elem))
#     numbers = f'{max(arr)} {min(arr)}'
#     return numbers

def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    numbers = f'{max(nn)} {min(nn)}'
    return numbers


print(high_and_low(string))
print(high_and_low(test))
