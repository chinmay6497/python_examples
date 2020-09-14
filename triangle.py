# (Solved—20 Lines)
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

n1=int(input("Enter the side 1 of triangle:"))
n2=int(input("Enter the side 2 of triangle:"))
n3=int(input("Enter the side 3 of triangle:"))

if n1==n2 and n2==n3:
    print("Triangle is Equivalent triangle")
elif (n1==n2 and n2!=n3) or (n1!=n2 and n2==n3) or (n1==n3 and n2!=n1):
    print("Triangle is isosceles")
else:
    print("Scalene")