# Naive Method time complexity is O(n)
# import datetime

# t0=datetime.datetime.now()
def zero(n):
    r=1
    for i in range(1,n+1):
        r*=i

    recursive=0
    while (r%10==0):
        recursive+=1
        r=r//10
    return recursive

print(zero(100))
# t1=datetime.datetime.now()
# t=int((t1-t0).total_seconds()*1000)

# print(f'Time execution for this program is {t}')
