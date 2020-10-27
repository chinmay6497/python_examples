def amstrong(n):
    temp=n
    x=temp%10
    a=x**3
    f=temp//10

    y=f%10
    b=y**3
    z=f//10

    c=z**3
    return n==(a+b+c)

print(amstrong(158))