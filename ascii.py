# Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.

# Input Description:
# You are given a string ‘s’

# Output Description:
# Print weight

# Sample Input :
# abc
# Sample Output :
# 294

s=input("Enter a text here:")
a=0

for i in range(len(s)):
    a+=ord(s[i])

print(f"ASCII of {s} is {a}")