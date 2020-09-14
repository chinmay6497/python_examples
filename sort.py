# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))

print(min(n1,n2,n3))
print(n1+n2+n3-max(n1,n2,n3)-min(n1,n2,n3))
print(max(n1,n2,n3))
