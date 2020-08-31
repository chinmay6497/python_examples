# Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1

# Input Description:
# You are given input string 'S'

# Output Description:
# Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left

# Sample Input :
# I am john cena cena john
# Sample Output :
# I am

n=input("Enter a string here:")
output=[]

# for i in n.split():
#     if i not in output:
#         output.append(i)

for i in n.split():
    if i in output:
        output.replace(i,'')


print(' '.join(output))