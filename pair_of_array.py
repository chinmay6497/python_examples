# Given an array of pairs of strings, find if there are mirror pairs.
# (s1, s2) & (s3, s4) are mirror pairs, if s1 = s4 and s2 = s3. The first string in each pair is distinct.

# Input Description:
# The first line contains the number string pairs N. Then N string pairs follow.

# Output Description:
# Print YES, if a mirror pair exists, print NO otherwise.

# Sample Input :
# 3
# raja kili
# pan quil
# kili raja
# Sample Output :
# YES

s1=['raja', 'kili']
s2=['pan', 'quil']
s3=['kili', 'raja']
s4=['quil', 'pan']

if s1[0]==s3[1] and s1[1]==s3[0]:
    print("Yes")

else:
    print("No")
