# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. All of the
# values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

d=int(input("Enter how much day old this bread is :"))

print(f"Price of bread is {3.49*d}$")
print(f"Discount is {3.49*d*0.6}")
print(f"Total is {(3.49*d)-(3.49*d*0.6)}")