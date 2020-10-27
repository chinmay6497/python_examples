def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    # return (a/gcd(a,b))*b
    return (a*b / gcd(a,b))

print(lcm(5,10))
# # print(type(gcd))
# # Time complexity is O(log(min(a,b)))
