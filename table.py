# def table(n):
#     # ans=1
#     l=[]
#     for i in range(1,11):
#         ans=n*i
#         l.append(ans)
#     return ans

# print(table(6))

def table(n):
    i=1
    l=[]
    while i!=11:
        ans=n*i
        l.append(ans)
        i+=1
    return l

print(table(7))