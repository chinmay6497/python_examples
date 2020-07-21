# You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 

# Note: In case of decimal values, round-off to two decimal places.

A=float(input("Enter the temperature in degree celcius :"))
print(round((1.8*A)+32),2)