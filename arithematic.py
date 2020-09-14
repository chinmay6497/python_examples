# Create a program that reads two integers, a and b, from the user.Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab

from math import log10

a=int(input("Enter 1 Number here:"))
b=int(input("Enter 2nd Number here:"))

print(f"Sum of number is {a+b}")
print(f"Product of number is {a*b}")
print(f"Quotient of number when a is divided by b is {a//b}")
print(f"Remainder of number when a is divided by b is {a%b}")
print(f"Base 10 log of {a} is {log10(a)} ")
print(f"A power b is {a**b}")
