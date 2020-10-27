# def factorial(n):
#     if n==0 or n==1:
#         return 1

#     else:
#         return n*factorial(n-1)

# print(factorial(4))
# Time complexity is O(n) and space complexity is O(n)

def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r

print(factorial(100))
# Time complexity is 0(n) and space complexity is O(1)