# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' 
# instead If the string length of the given string is less than 3, leave it unchanged

n=input("Enter a sentence here:")

if len(n)<3:
    print(n)

else:
    if n[-3:]=='ing':
        print(n.replace(n[-3:],'ly'))

    else:
        print(n.replace(n[-3:],'ing'))