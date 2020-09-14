# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

w=int(input("Enter the Number of Widgets here:"))
g=int(input("Enter the Number of Gizmos here:"))

print(f"Total weight is {(w*75)+(g*112)} grams")