def trialing_zero(n):
    result=0
    i=5
    while n/i>=1:
        result+=n//i
        i*=5
    return result

print(trialing_zero(9))
