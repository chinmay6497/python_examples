# (18 Lines)
# Canada has three national holidays which fall on the same dates each year.
# Holiday Date
# New year’s day January 1
# Canada day July 1
# Christmas day December 25
# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.

n=input("Enter month here:")
s=int(input("ENter date here:"))

if n=='jan' and s==1:
    print('Holiday')

elif n=='july' and s==1:
    print("Holiday")

elif n=='Dec' and s==25:
    print("Holiday")

else:
    print("Working day")