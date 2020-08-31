# you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.If they are balanced print 1 else print 0

# Input Description:
# You are given a string ‘s’

# Output Description:
# Print 1 for balanced and 0 for imbalanced

# Sample Input :
# {({})}
# Sample Output :
# 1
# brackets=['()',"[]",'{}']
# def paranthesis_checker(l):
#     # while any (l) in brackets:
#     if any(l) in brackets:
#         print(1)
#     else:
#         print(0)
    
    
    
# if (l=='(' and ')') or (l=='{' and '}') or  (l=='[' and ']'):
#         return True
#     else:
#         return False

# print(paranthesis_checker('{}'))  

# s=[({})]
# brackets=['()','[]','{}']
# for i in s:
#     if i in brackets:
#         print("Balanced")
#     else:
#         print("Unbalanced")


# # Why this problem is not getting solved using the loop or conditional statement ?
#  This problem can solved using the stack method here we have kept two list open and close bracket now first i have given () s input initially value of i will be ( so for this the if condition will work and now again 
# the for loop will work and this time we will get the ) now the position of ) will be seen from the close bracket list, at open bracket list it must be at the same position if it is then it will be popped from n
open_brackets = ["[","{","("] 
close_brackets = ["]","}",")"] 
n=[]

def paranthesis_checker(l):  
    for i in l: 
        if i in open_brackets: 
            n.append(i) 
        elif i in close_brackets: 
            pos = close_brackets.index(i) 
            if ((len(n) > 0) and (open_brackets[pos] == n[len(n)-1])): 
                n.pop() 
            else: 
                return "Unbalanced"
    if len(n) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"

print(paranthesis_checker("()"))