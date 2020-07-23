# You are given three numbers A, B & C. Print the largest amongst these three numbers.

a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))

if a>b and a>c:
    print(f"The greatest number is {a}")

elif b>a and b>c:
    print(f"The greatest number is {b}")

else:
    print(f"The greatest number is {c}")