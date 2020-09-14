# You are given a string ‘s’.Your task is to print the string in alternate lowercase and uppercase order.

# Input Description:
# You are given a string

# Output Description:
# Print the string according to given criteria

# Sample Input :
# abcd efgh ijkl
# Sample Output :
# ABCD efgh IJKL

s=input("Enter a text here:")
s=s.split()
output=[]

for i in range(len(s)):
    if i%2==0:
        output.append(s[i].upper())
    else:
        output.append(s[i].lower())

print(" ".join(output))

# s=input("Enter Input String :")
# s=s.split()
# #used list comprehension 
# output=[s[i].upper() if i%2==0 else s[i].lower() for i in range(len(s))]
# print(" ".join(output))

