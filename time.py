# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds
# respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

s=int(input("Enter the total second"))

day=s/86400
s=s%86400

hour=s/3600
s=s%3600

minute=s/60
s=s%60

print(f"Duration is {round(day,1)} Days,{round(hour,1)} hours,{round(minute,1)} minute,{round(s,1)} second")