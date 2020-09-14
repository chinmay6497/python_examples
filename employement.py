n=float(input("Here grade:"))

if n==0.0:
    y='Unacceptable'
    x='null'

elif n==0.4:
    y='Acceptable'
    x=0.4*2400

elif n>0.6 and n<=1:
    y='Meritious'
    x=0.6*2400

else:
    y='Enter valid syntax'

print(f"For your grade {n} you {y} with bonus of amount{x} $")