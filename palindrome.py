#  Radha newly learnt about palindromic strings.A palindromic string is a string which is same when read from left to right and also from right to left.Help her in implementing the logic.

 

# Input Description:
# You are given a String ‘s’

# Output Description:
# Print 1 if String is palindrome or 0 if not

# Sample Input :
# NITIN
# Sample Output :
# 1

s=input("Enter a text here:")

if s==s[::-1]:
    print("Yes")

else:
    print("No")