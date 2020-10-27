# Here time complexity is O(n^1.5)
# def prime(n):
#     if n==1:
#         return False
#     else:
#         i=2
#         while (i*i<=n):
#             if n%i!=0:
#                 return True
#             else:
#                 return False
#             i+=1

# # print(prime(8))
# def prime_count(n):
#     for i in range(2,n+1):
#         if prime(i):
#             print(i)

# prime_count(8)

def eratorthenes(n):
    prime=[True for i in range(n+1)]
    i=2
    while (i*i<=n):
        if prime[i]==True:
            for i in range(i*2,n+1,i):
                prime[i]=False
        i+=1
    prime[0]=False
    prime[1]=False

    for i in range(n+1):
        if prime[i]:
            print(i)

eratorthenes(30)
# Time complexity here is O(nloglogn)