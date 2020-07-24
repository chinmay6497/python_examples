# You will be provided with a number. Print the number of days in the month corresponding to that number.

n=int(input("Enter the number:"))

if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("Number of days are 31")

elif n==2:
    print("Number of days are 28 or 29")

else:
    print("Number of days are 30")
