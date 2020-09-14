# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. 
# The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.

# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.

import math

l1=int(input("Enter a latitude of point1:"))
l2=int(input("Enter a longitude of point1:"))

t1=int(input("Enter a latitude of point2:"))
t2=int(input("Enter a longitude of point2:"))

a=math.sin(l1)
b=math.sin(t1)
a1=math.cos(l1)
a2=math.cos(t1)

c=math.cos(t2-t1)

print(f"Distance between given two points is {6371.01*(math.acos((a*b)+(a1+a2)*c))}")