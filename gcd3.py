def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    # print(ty)

print(gcd(4,8))
print(type(gcd))