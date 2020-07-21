# You are provided with the radius of a circle "A". Find the length of its circumference.

# Note: In case the output is coming in decimal, roundoff to 2nd decimal place. In case the input is a negative number, print "Error".

A=float(input("Enter the radius of the circle"))

if A>0:
    L=2*3.14*A
    print(round(L,2))

else:
    print("Error")