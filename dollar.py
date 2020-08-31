# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself

l=input("Enter a string here:")
x=l[0]
l=l.replace(x,'$')
l=x+l[1:]

print(l)