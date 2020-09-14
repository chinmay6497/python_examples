# Write a program to get a string S, Type of conversion (1 - Convert to Lowercase, 2 - Convert to Uppercase) T, and integer P . 
# Convert the case of the letters in the positions which are multiples of P.(1 based indexing).

# Input Description:
# Given a string S, Type of conversion T, and integer P

# Output Description:
# Convert the case of the letters and print the string

# Sample Input :
# ProFiLe
# 1
# 2
# Sample Output :
# Profile

# 2 indicates the place of the letter to change

# so, you have to change in the place of the letter(Profile -r,F,L)

# r,F,L are changed into lowercases

s='Profile'
x=int(input("Select 1 or 2:"))

if x==1:
    s=s.lower()
    print(s)

elif x==2:
    s=s.upper()
    s=s.replace("R",'r')
    s=s.replace("F",'f')
    s=s.replace("L",'l')
    print(s)
