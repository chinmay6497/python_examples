# def mice(n,m,h):
#     m=sorted(m)
#     h=sorted(h)
#     l=[]
#     for i in range(len(m)):
#         for j in range(len(h)):
#             l.append(m[i]-h[j])
#     return max(l)
# m=[4,2]
# n=[1,7]

# print(mice(2,m,n))

def mice(n,m,h):
    m.sort()
    h.sort()

    ans=-1

    for i in range(n):
        ans=max(ans,abs(m[i]-h[i]))
    return ans

m=[4,-4,2]
h=[4,0,5]

print(mice(2,m,h))