n=input("Enter the grade here:")

if n=='A+':
    y=4.0
elif n=='A':
    y=4.0
elif n=='A-':
    y=3.7
elif n=='B+':
    y=3.3
elif n=='B':
    y=3.0
elif n=='B-':
    y=2.7
elif n=='C+':
    y=2.3
elif n=='C':
    y=2.0
elif n=='C-':
    y=1.7
elif n=='D+':
    y=1.3
elif n=='D':
    y=1.0
elif n=='F':
    y=0
else:
    y="Enter valid"
print(y)