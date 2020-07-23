# You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.Print the output up to two decimal places (Round-off if necessary).

p=float(input("Enter the principle amount($) :"))
r=float(input("Enter the interest rate :"))
n=float(input("Enter the time :"))

print(f"The simple interest is {(p*r*n)/100}")