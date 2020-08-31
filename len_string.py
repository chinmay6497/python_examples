# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Go to the editor 
# Sample String : 'w3resource' Expected Result : 'w3ce' 
# Sample String : 'w3' Expected Result : 'w3w3' 
# Sample String : ' w' Expected Result : Empty String

l=input("Enter a string here:")

if len(l)>2:
    a=l[:2]
    b=l[-2:]
    print(a+b)

elif len(l)==2:
    print(l*2)

else:
    print('')