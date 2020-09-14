# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.

import math

x=int(input("Enter the radius of cylinder here:"))
y=int(input("Enter the Height of cylinder here:"))

print(f"Volume of cylinder is {round(math.pi*(x*x)*y,1)}")