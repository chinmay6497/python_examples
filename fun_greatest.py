def greatest (a,b,c):
    if a>b and a>c:
        print("A is greatest")

    elif b>a and b>c:
        print("B is greatest")

    print("C is greatest")

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))

greatest(a,b,c)