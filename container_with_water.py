def container(arr):
    f=0
    l=len(arr)-1

    area=0

    while f < l:
        area=max(area,min(arr[f],arr[l])*(l-f))

        if arr[f] < arr[l]:
            f+=1
        else:
            l-=1

    return area

print(container([1,3,17,2,18,15,13,6,11,7]))