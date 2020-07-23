# You are provided with a number, "N". Find its factorial.

n=int(input("Enter a positive number:"))
fac=1

for i in range(1,n+1):
    fac = fac*i
    
print(fac)