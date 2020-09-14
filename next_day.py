y=int(input("Enter a year here:"))

if y%4==0:
    leap_year==True

m=int(input("Enter a month here:"))

if m==1 or m==3 or m==5 or 7 or m==8 or m==10 or m==12:
    month_lenght=31
elif m==2:
    if leap_year:
        month_lenght=29
    else:
        month_lenght=28
else:
    month_lenght=30

d=int(input("Enter a date here:"))

if d<month_lenght:
    d+=1
else:
    d=1
    if m==12:
        m=1
        y+=1
    else:
        m+=1

print(f"The next date is {y,m,d}")

