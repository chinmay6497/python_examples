import math

def digit_in_factorial(n):
    # if n==1:
    #     return 0
    # x=math.log(n)+math.log(n-1)
    # return math.floor(x+1)

    sum=0
    j=1
    while j<=n:
        sum+=math.log10(j)
        j+=1
    return 1+math.floor(sum)

print(digit_in_factorial(5))