""" Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)."""

# L = SQRT((X1-X2)^2 + (Y1-Y2)^2)


from math import sqrt

a = [4, 0]
b = [6, 6]
result = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
print(result)

