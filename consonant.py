# You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1

# Input Description:
# You are given a string ‘s’.

# Output Description:
# Print only consonants.

# Sample Input :
# I am shrey 
# Sample Output :
#  m shry

n=input("Enter the string here:")
vowels=('a','e','i','o','u')

for i in n.lower():
    if i in vowels:
        n=n.replace(i,"")

print(n)        
    