# A polygon is regular if its sides are all the same length and the angles between all of
# the adjacent sides are equal. The area of a regular polygon can be computed using
# the following formula, where s is the length of a side and n is the number of sides:
# area = n × s2
# 4 × tan
# 
# π
# n
# 
# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.

import math

s=int(input("ENter value of s:"))
n=int(input("ENter value of n:"))

x=math.pi/4

print(f"Area of polygon is {(n*(s*s))/4*math.tan(x)}")