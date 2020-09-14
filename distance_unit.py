# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

x=int(input("Enter the input of the distance in feet:"))

print(f"Distance in inch is {x*12}")
print(f"Distance in yard is {x*0.33}")
print(f"Distance in miles is {x*0.00018}")
