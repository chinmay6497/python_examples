# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.

import math

r=float(input("Enter radius of circle:"))

print(f"Area of circle is {2*math.pi*r}")
print(f"Volume of circle is {(4/3)*math.pi*r**3}")