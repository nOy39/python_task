# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

month = input('Enter month: ')
year = input('Enter year: ')
print(calendar.month(int(year), int(month)))