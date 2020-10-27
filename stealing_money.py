def money(n,k):
    if n%2==0:
        a=n//2
    else:    
        a=n//2+1

    return a*k

print(money(2,12))
