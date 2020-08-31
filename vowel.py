# Given a string S, print 'yes' if it has a vowel in it else print 'no'.
# Sample Testcase :
# INPUT
# codekata
# OUTPUT
# yes

s=input("Enter a string here:")
vowels=['a','e','i','o','u']
x=[]
y=[]
for i in s:
    if i in vowels:
        x.append(i)

    else:
        y.append(i)

if len(x)!=0:
    print('Yes')

else:
    print("No")


