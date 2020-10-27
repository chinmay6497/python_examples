def prime(n):
    if (n==1):
        return False
    for i in range(2,1+int(n**0.5)):
        if n%i==0:
            return False
    return True

def divisor(n):
    c=0
    for j in range(1,int(n**0.5)+1):
        if prime(j):
            c+=1
    return c

print(divisor(6))


















