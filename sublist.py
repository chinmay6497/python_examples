def sublist(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

print(sublist([1,2,3,[1,2],[2,3]]))