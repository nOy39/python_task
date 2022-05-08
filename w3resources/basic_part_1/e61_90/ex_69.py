"""Write a Python program to sort three integers without using conditional statements and loops."""

x = int(input('First number: '))
y = int(input('Second number: '))
z = int(input('Third number: '))

a_min = min(x, y, z)
c_max = max(x, y, z)
b_mid = (x + y + z) - (a_min + c_max)
print(f'{a_min}, {b_mid}, {c_max}')
