"""
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1
squares disposed in the same manner as in the drawing:
"""


def perimeter(n):
    n_0 = 1
    n_1 = 0
    sum_fib = 0
    for i in range(n + 1):
        n_2 = n_0 + n_1
        n_0 = n_1
        n_1 = n_2
        sum_fib += n_2
    return sum_fib * 4


print(perimeter(5))
