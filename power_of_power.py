def power(n):
    s=0
    for i in range(1,n*2+1):
        if i%2==0:
            s+=i**2
    return s

print(power(1))