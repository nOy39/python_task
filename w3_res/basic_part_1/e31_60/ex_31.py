# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
#
# The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive integer d
# such that d is a divisor of both a and b; that is, there are integers e and f such that a = de and b = df,
# and d is the largest such integer. The GCD of a and b is generally denoted gcd(a, b).

num_1 = 311
num_2 = 336
gsd = num_1 % num_2 \
    if num_1 > num_2 \
    else num_2 % num_1

print(f'(GCD) for {num_1} and {num_2} is '
      f'{gsd}')
