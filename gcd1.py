def gcd(n1,n2):
    r=min(n1,n2)
    while r>=0:
        if (n1%r==0) and (n2%r==0):
            break
        r-=1
    return r

print(gcd(4,8))

# O(min(n1,n2))