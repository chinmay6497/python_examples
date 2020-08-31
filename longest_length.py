# Write a Python function that takes a list of words and returns the length of the longest one.

n=[]

def longest_length(l):
    for i in l:
        n.append(len(i))
    return max(n)

print(longest_length(['chinmay','abc','x']))        
