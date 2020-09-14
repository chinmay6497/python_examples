# You are given a paragraph.Your task is to print the words that come just after articles.

# Input Description:
# You are given a string ‘s’

# Output Description:
# print the words that come just after articles and -1 if there are no articles

# Sample Input :
# The sun rises in the east

# Sample Output :
# sun east

# s=input(" ")
# article=["a","an","the"]
# s=s.lower()

# for i in s.split():
#     if i in article:
#         A=s.index('a')
#         print(s[A+1])
#         # A=s.find('a')
#         # B=A+1
#         # print(s[:])
    

s=input("Enter string:")
article=["a","an","the"]
s=s.lower().split()

words=[s[i+1] for i,x in enumerate(s) if x in article]
if words:
    print("".join(words))

else:
    print(-1)