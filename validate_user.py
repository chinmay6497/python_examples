# X company developed a new system to make sure no two usernames are same. So, they hired you as a developer to develop this system. They have set some rules to do the same.
# If you see the same username that already exists, just add a number at the end of that username ,else print "Verified".

# Input Description:
# First line consists of an integer N, denoting number of usernames. Second line consists of N spaced separated Strings, denoting usernames.

# Output Description:
# print the required output in a new line.

# Sample Input :
# 4
# abc aab abc aba
# Sample Output :
# Verified Verified abc1 Verified

names=['abc','aab','abc','aba']

oc_set = [] 
res = [] 
for idx, val in enumerate(names): 
    if val not in oc_set: 
        oc_set.append((val))          
    else: 
        res.append(val)


x=("".join(res))
y=("".join(oc_set))
print(x+str(1)+oc_set)
print(oc_set)
print(type(oc_set))
