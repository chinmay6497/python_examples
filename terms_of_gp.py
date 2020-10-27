def terms_of_gp(a,b,n):
    r=b/a
    x=a*(r**(n-1))
    return x

print(terms_of_gp(2,4,6))