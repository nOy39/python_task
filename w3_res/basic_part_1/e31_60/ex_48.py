""" Write a Python program to parse a string to Float or Integer"""

string = '3.141516'
if string.find('.') == 1:
    print(float(string))
    print(int(float(string)))
else:
    print(int(string))
