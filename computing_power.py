# Here time complexity is O(n)
# def pow(a,b):
#     return a**b

# print(pow(2,4))

# TIme complexity is O(logn) and space complexity is O(n)
# def power(a,b):
#     if b==0:
#         return 1

#     if b%2==0:
#         return power(a,0.5*b)*power(a,0.5*b)
#     return power(a,b-1)*a

# print(power(2,5))


# Iterative Solution

def power(a,b):
    while b!=0:
        if b%2==0:
            return (a*b/2)*(a*b/2)
        return (a*(b-1)/2)*a*(a*(b-1)/2)
        b=b/2

print(power(2,5))
# Time complexity is O(logn) and space complexity is O(1
# )