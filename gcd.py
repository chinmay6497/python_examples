# def gcd(n1,n2):
g=[]   
n=8 
for i in range(1,n):
    if n%i==0:
        g.append(i)

# print(g)

n1=4
r=[]
for i in range(1,n1+1):
    if n%i==0:
        r.append(i)
    
o=[i for i in g if i in r]
print(max(o))