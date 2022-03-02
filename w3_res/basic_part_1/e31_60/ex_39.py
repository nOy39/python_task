"""Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years.

Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

# The formula for future value with compound interest is FV = P(1 + r/n)^nt.
# FV = the future value;
# P = specified principal amount;
# r = the annual interest rate expressed as a decimal;
# n = the number of times interest is paid each year(rate of interest);
# t = time in years.


amt = 10000
rate = 3.5
years = 7
future_value = amt*((1 + (0.01 * rate)) ** years)
print(round(future_value, 2))
