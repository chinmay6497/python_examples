# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

x=float(input("Enter the Cost of your meal:"))

print(f"Tax of your meal is %.f {round(0.1*x,2)}$")
print(f"TIp of your meal is {0.18*x}$")
print(f"Total amount  of your meal is  {round((0.1*x)+(0.18*x)+x,2)}$")