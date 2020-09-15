def odd_even(l):
    odd=[]
    even=[]
    for i in range(len(l)):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    z=[odd] + [even]
    return z

print(odd_even([1,2,3,4,5,6,7])) 