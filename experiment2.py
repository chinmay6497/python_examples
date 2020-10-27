def trailing_zero(n):
    r=1
    for i in range(1,n+1):
        r*=i

    p=0
    i=5
    while (n/i>=1):
        p+=n//i
        i*=5
    return p

print(trailing_zero(100))