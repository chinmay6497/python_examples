def divisor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=' ')
    
divisor(25)

# Here time complexity is O(n) and space complexity is O(1)