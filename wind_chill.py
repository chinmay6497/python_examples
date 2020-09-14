# When the wind blows in cold weather, the air feels even colder than it actually is
# because the movement of the air increases the rate of cooling for warm objects, like
# people. This effect is known as wind chill.
# In 2001, Canada, the United Kingdom and the United States adopted the following
# formula for computing the wind chill index. Within the formula Ta is the
# air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
# A similar formula with different constant values can be used with temperatures in
# degrees Fahrenheit and wind speeds in miles per hour.
# WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
# Write a program that begins by reading the air temperature and wind speed from the
# user. Once these values have been read your program should display the wind chill
# index rounded to the closest integer.

import math

t=float(input("Enter temperature here:"))
v=float(input("Enter velocity here:"))

print(f"Wind chill is {13.12+(0.6215*t)-(11.37*(pow(v,0.16)))+(0.3965*t*(pow(v,0.16)))}")
