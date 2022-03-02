# Write a Python program to solve (x + y) * (x + y).

x = 3
y = 4.1
print('(%s + %s)^2 = %f' % (x, y, (x + y)**2))

result = x * x + 2 * x * y + y * y
print(f'(%s + %s)^2 = {result}' % (x, y))
