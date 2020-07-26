#  We have to take input from the user and we have to state whether the string is palindrome or not.
#  Note: Palindrome is string which by reversing also gives the same string.

n=input("Enter a text here:")

def palindrome(n):
    if n==n[::-1]:
        print("It is palindrome")
    else:
        print("It is not palindrome")

palindrome(n)


