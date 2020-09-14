n=float(input("ENter the magnitude of earthquake here:"))

if n<=2:
    y='Micro'

elif n>2 and n<3:
    y='Very Minor'

elif n>3 and n<4:
    y='minor'

elif n>4 and n<5:
    y='Light'

elif n>5 and n<6:
    y='moderate'

elif n>6 and n<7:
    y='Strong'

elif n>7 and n<8:
    y='Major'

elif n>8 and n<9:
    y='great'

else:
    y='Meteroic'

print(y)