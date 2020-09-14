# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

amt=float(input(("Enter the amount here:")))
print(f"Amount in saving account after 1 year is {amt+((amt*4)/100)}")
print(f"Amount in saving account after 2 year is {round(amt *(pow((1 + 4/ 100),2)),2)}")
print(f"Amount in saving account after 3 year is {round(amt *(pow((1 + 4/ 100),3)),2)}")