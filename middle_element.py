# Given a string S, print it after changing the middle element to * (if the length of the string is even, change the 2 middle elements to *).
# Sample Testcase :
# INPUT
# hello
# OUTPUT
# he*lo

s='hello'
y=len(s)
if y%2!=0:
    z=s[y//2]
    if (s[(y//2)]!=s[(y//2)+1]):
        s=s.replace(z,'$')
        print(s)
    else:
        for i in s:
            if 



        # s=s.split(',')
        # print(s)
        # s=s.replace(,'$')
        # print(s)












    # for i in s:
    #     if s[(y-1)//2:(y+2)//2]!=s[(y//2)+1]:
    #         x=s[(y-1)//2:(y+2)//2]
    #         z=s.replace(x,'$')
    #     print(z)

# print(5//2)











#     s.replace('l','$')

# else:
#     s.replace('ll','$')

# print(s)


