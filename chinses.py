n=int(input("Enter the birth year here:"))

if n%12==8:
    y='Dragon'

elif n%12==9:
    y='Snake'

elif n%12==10:
    y='Horse'

elif n%12==11:
    y='Sheep'

elif n%12==0:
    y='Monkey'

print(y)