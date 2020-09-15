f=['mango','banana']
f.append('apple')
print(f)
# Insert method it is used to insert the object at a particular location
f.insert(2,'grapes')
# If we provide index which is greater than len than the item will be inserted at last position
print(f)

#  Concatenate list
f1=['apple','mango']
f2=['banana','grapes']
print(f1+f2)

#  Extent Method
f1.extend(f2)
print(f2)
print(f1)

# Append
f1.append(f2)
print(f2)
print(f1)

#  If we does append than we will get list inside list whereas in extend we will get both of them combined together only