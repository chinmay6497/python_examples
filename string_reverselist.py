def rev(l):
    r=[]
    for i in l:
        r.append(i[::-1])
    return r

print(rev(['abc','def']))