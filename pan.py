# Indian PAN card issuing authority have found some fake PAN cards. They have hired you so that you can validate PAN card for them. Your task is to develop a suitable algorithm which could check if pan is valid or not

# 1)Pan must have uppercase letters only.

# 2)It must be of 10 character only

# 3)From index 1 to 5 all must be letters(A-Z),last index must be letter

# 4)Rest all must be integer Starting from 1

# Input Description:
# You are given a input string which indicates the PAN number

# Output Description:
# Print 'pan' if it is valid PAN number, else print 'not pan'

# Sample Input :
# HXTPS2142R
# Sample Output :
# pan

pan=input("Enter a PAN Card number here:")
x=pan[:5]
y=pan[9:10]
z=pan[5:9]

if len(pan)==10:
    if pan.isupper()==True and x.isalpha()==True and y.isalpha()==True and  z.isdigit()==True:
        print("Your pan card is valid")

else:
    print("Enter valid Pan card number")