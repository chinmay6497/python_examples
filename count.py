
def even_divisible(x,y,z):
    l=[]
    w=range(x,y+1)
    for i in w:
        if i%z==0:
            l.append(i)
    return sum(l)
        

print(even_divisible(1,10,2))