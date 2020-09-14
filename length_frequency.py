n=int(input("Enter the frequency:"))
n=float(("{:.3e}".format(n)))
print(n)

if n<=3.0e+09:
    y='Radio Waves'

elif n>3.0e+09 and n<3e+12:
    y='Microvae'

elif n>3.0e+12 and n<4.3e+14:
    y='InfraredRed Light'

elif n>4.3e+14 and n<7.5e+14:
    y='Visible Light'

elif n>7.5e+14 and n<3e+17:
    y='Ultra Violet Light'

elif n>3e+17 and n<3e+19:
    y='X-Rays'

elif n>3e+19:
    y='Gamma Rays'

else:
    y='ENter valid Spectrum'
    
print(y)
