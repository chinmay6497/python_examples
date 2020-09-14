# You are given a string ‘s’.Your task is to print the string in the order they are present and then sum of digits.

# Input Description:
# You are given a string ‘s’.

# Output Description:
# Print the string and then at last sum of all the digits

# Sample Input :
# AC30BD40
# Sample Output :
# ACBD7
 
s="AC30BD40"
sum=0
digit=[]
for i in s:
    if i.isdigit()==True:
        sum+=int(i)

    else:
        y=digit.append(i)

digit=''.join(digit)
sum=str(sum)
print(digit+sum)
