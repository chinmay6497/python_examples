def palindrome(n):
    rev=0
    temp=n

    while temp != 0:
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    return rev==n

print(palindrome(7))


