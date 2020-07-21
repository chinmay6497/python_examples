# Print the First 3 multiples of the given number "N". (N is a positive integer)

# Note: print the characters with a single space between them.

a=int(input("Enter a positive number"))
print(a,end=" ")
print(a*2,end=" ")
print(a*3,end=" ")

# Method 2

b=a*2
c=a*3
print(f"{a}{b}{c}")