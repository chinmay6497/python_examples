# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

d=int(input("Enter the number of days"))
h=int(input("Enter the number of Hours"))
m=int(input("Enter the number of minutes"))
s=int(input("Enter the number of second"))

print(f"The total number of second is {s+(m*60)+(h*60*60)+(d*24*60*60)}")