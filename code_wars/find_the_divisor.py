"""Create a function named divisors/Divisors that takes an integer n > 1
    and returns an array with all of the integer's divisors(except for 1
     and the number itself), from smallest to largest.
     If the number is prime return the string '(integer) is prime'
     """


def divisor(num: int):
    a = []
    for i in range(2, num):
        if num % i == 0:
            a.append(i)
    return a if len(a) > 0 else f"{num} is prime"


print(divisor(15))
print(divisor(29))
print(divisor(17))

