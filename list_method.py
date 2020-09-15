f=['apple','mango','apple']

print(f.count('apple'))

f.sort()
print(f)
#  Sort method will sort the original list whereas sorted will create a new list with sorted
print(sorted(f))

#  Clear
# f.clear()
# print(f)

# Copy

f1=f.copy()
print(f1)