# def trailing_zero(n):
#     r=1
#     for i in range(1,n+1):
#         r*=i
    
#     p=0
#     for i in range(5,r,i*5):
#         p+=n//i
#     return p

# print(trailing_zero(100))
    

# p=0
# r=9332621544394415268169923885626670049071596826438162146859296389521759999322991560894146397615651828625369720827223758251185210916840000000000000000000000000
# for i in range(5,r,i*5):
#     p+=n//i
# print(p)
# import math

def findTrailingZeros(n): 
    count = 0
    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
    return int(count)
# r=math.factorial(100)
print(findTrailingZeros(100))