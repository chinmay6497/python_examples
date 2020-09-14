# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

t=float(input("Enter temperature here:"))

print(f"Temp in faranheit is {((9/5)*t)+32}")
print(f"Temp in kelvin is {273+t}")