# You are provided with a number check whether its odd or even. Print "Odd" or "Even" for the corresponding cases.
# Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".

n=float(input("Enter a number:"))

n=round(n,2)

if n/2==0:
    print("Number is even")

else:
    print("Number is odd")