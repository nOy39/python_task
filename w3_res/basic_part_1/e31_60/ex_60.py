"""Write a Python program to calculate the hypotenuse of a right angled triangle."""

# From Wikipedia,
# A right triangle or right-angled triangle, or more formally an orthogonal triangle,
# is a triangle in which one angle is a right angle.
# The relation between the sides and angles of a right triangle is the basis for trigonometry.
# The side opposite the right angle is called the hypotenuse.
# If the lengths of all three sides of a right triangle are integers,
# the triangle is said to be a Pythagorean triangle
# and its side lengths are collectively known as a Pythagorean triple.

# AC = SQRT(AB**2 + BC**2)
import math

ab = 3
bc = 4
ac = math.sqrt(pow(ab, 2) + pow(bc, 2))
print(f'Hypotenuse of a right angled triangle. With side AB = {ab}, BC = {bc} equal AC = {ac}')