# You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

# Input Description:
# You are given a long string of digits

# Output Description:
# Print the desired result print -1 if result length is 0

# Sample Input :
# 1331
# Sample Output :
# 11

n=input("Enter a number here:")
i=0
Output=''

while  i<len(n):
    Output+=n[i]
    
    while  (i+1<len(n) and n[i]==n[i+1]):
        i+=1
    i+=1

print(Output)