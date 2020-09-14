# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

n=int(input("Enter the side here:"))

if n>3 and n<10:
    if n==3:
        print("Object is Triangle")
    elif n==4:
        print("Object is Square")
    elif n==5:
        print("Object is Pentagon")
    elif n==6:
        print("Object is Hexagon")
else:
    print("Entered Valid side")