f=['apple','mango','berry']

# for i in f:
#     print(i)

# i=0
# while i<len(f):
#     print(f[i])
#     i+=1

#  List Inside List
matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0][2])

# for i in matrix:
#     for j in i:
#         print(j)

l=list(range(1,11))
# print(l)

# y=l.pop()
# print(l)
# print(y)

# print(l.index(10,1))


def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list([1,2,3,4,5,6]))