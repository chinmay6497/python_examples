a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if a>=2 and a<3:
    y=2

elif a==0 and b>1:
    y=1

else:
    y=0

r1=(-b+pow((b*b)-(4*a*c),0.5)/2*a)
r2=(-b-pow((b*b)-(4*a*c),0.5)/2*a)

print(f"The equation has {y} root and solutions are {r1,r2}")