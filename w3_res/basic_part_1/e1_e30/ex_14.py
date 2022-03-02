# Write a Python program to calculate number of days between two dates.

from datetime import date
print(date.today())
firstDate = date(2022, 1, 11)
secondDate = date.today()
print(secondDate - firstDate)