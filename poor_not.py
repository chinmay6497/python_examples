# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

n=input("Enter a string here with not poor:")
x=n.find('not')
y=n.find('poor')

if y>x and x>0 and y>0:
    n=n.replace(n[x:(y+4)],'good')

print(n)