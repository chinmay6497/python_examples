def common(l1,l2):
    c=[]
    for i in l1:
        if i in l2:
            c.append(i)
    return c

print(common([1,2,3,4],[1,2,67]))