def mulitpy(a,b,m,n):
    prod=[0]*(m+n-1)

    for i in range(m):
        for j in range(n):
            prod[i+j]+=a[i]*b[j]
    return prod

def print_poly(poly,n):
    for i in range(n):
        print(poly[i],end=' ')
        if i!=0:
            print('x^',i ,end=' ')
        if (i!=n-1):
            print('+',end=' ')
 
a=[5,0,10,6]
b=[1,2,4]

m=len(a)
n=len(b)

prod=mulitpy(a,b,m,n)
print_poly(prod,m+n-1)
