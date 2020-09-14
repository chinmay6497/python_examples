# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

length=float(input("Enter the length of Field in feet:"))
width=float(input("Enter the width of Field in feet:"))

print(f"Area of field is {(length*width)/43560}")