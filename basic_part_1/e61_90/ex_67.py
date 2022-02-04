"""Write a Python program to convert pressure in kilopascals to pounds per square inch,
   a millimeter of mercury (mmHg) and atmosphere pressure."""

kPa = 1000
pounds_square_inch = kPa / 6.895
mmHg = 1 * 7.501
bar = 1 / 101

print(f'{kPa} KPa = {pounds_square_inch} psi = {mmHg} mmHg = {bar} bar')
