def lcm(a,b):
    c=max(a,b)
    while True:
        if c%a==0 and c%b==0:
            return c
        c+=1
    return c

print(lcm(5,10))

# Time complexity of this function is O(a*b-max(a,b))