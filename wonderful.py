#  You are given a string. You have to print “Wonder” if the string is wonderful and -1 if it is not. A wonderful string is a string,which is made up of exactly 3 different characters.

# Input Description:
# You are given a string

# Output Description:
# Print “Wonder” if it is wonderful and -1 if it is not

# Sample Input :
# aabbcc
# Sample Output :
# Wonder

n=input("Enter a string here:")
i=0


if i<len(n):
    while (i+1<len(n) and n[i]!=n[i+1]):
        i+=1
    i+=1
print('Wonderful')

else :
    print(-1)
