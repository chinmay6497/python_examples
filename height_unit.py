# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.

f=int(input("Enter the Height in feet:"))
i=int(input("Enter the Height in inches:"))

print(f"Height in cm is {(f*12*2.54)+(i*2.54)}")