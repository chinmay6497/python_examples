# def is_prime(n):
#     for i in range(2,n):
#         if n%i!=0:
#             return True
#         return False

# def prime_factor(n):
#     for i in range(2,n):
#         if is_prime(i):
#             x=i
#             while (n%x==0):
#                 print(i)
#                 x=x*i

# print(prime_factor(12))

# # Time Complexity here is O(n^2logn)

def prime_factor(n):
    while n%2==0:
        print(2,end=' ')
        n=n/2

    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            print(i,end=' ')
            n=n/i
    
    if n>2:
        print(int(n),end=' ')

print(prime_factor(315))

# This code has time complexity of O(n^0.5)