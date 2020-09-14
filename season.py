# The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the
# way that the calendar is constructed, we will use the following dates for this exercise:
# ason from Month and Day 21
# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

m=input("Enter the month here:")
d=int(input("Enter the date here:"))

if m=='jan' or m=='feb':
    season='Winter'

elif m=='march':
    if d<20:
        season='Winter'

elif m=='march':
    if d>=20:
        season='spring'

elif m=='april' or m=='may':
    season='spring'

elif m=='june':
    if d<21:
        season='spring'

elif m=='june':
    if d<=21:
        season='spring'

print(season)