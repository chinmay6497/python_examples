def reverse(l):
    r=[]
    for i in range(len(l)):
        poped_item=l.pop()
        r.append(poped_item)
    return r

print(reverse([1,2,3,4]))
























