m=input("Enter your birth of month")
d=int(input("Enter date of birth:"))

if m=='dec' and d>22:
    print('Capricorn')

elif m=='jan' and d<19:
    print('Capricorn')

elif m=='jan' and d>20:
    print('Aquarius')

elif m=='feb' and d<18:
    print('Aquarius')

elif m=='feb' and d<18:
    print('Pisces')

elif m=='march' and d<20:
    print('Pisces')

elif m=='march' and d>20:
    print('Pisces')

elif m=='april' and d<19:
    b='Arises'

print(b)