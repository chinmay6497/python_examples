# Here time complexity is log(n)

# def reverse(n):
#     while n!=0:
#         x=n%10
#         print(x,end='')
#         n=n//10

# reverse(123)

def reverse(n):
    t=0
    while n!=0:
        x=n%10
        t=(t*10)+x
        n=n//10
    return t

print(reverse(132))