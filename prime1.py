def prime(n):
    if n==1:
        return False
    else:
        i=2
        while (i*i<=n):
            if n%i!=0:
                return True
            else:
                return False
            i+=1

print(prime(2))

# Time complexity of this code is O(n^1/2)