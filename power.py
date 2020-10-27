def power(a,b):
    if b==0:
        return 1

    temp=power(a,b//2)

    temp=temp*temp
    if b%2==0:
        return temp

    else:
        return temp*b

print(power(3,4))