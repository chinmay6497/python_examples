# Write a Python function to reverses a string if it's length is a multiple of 4

def reverse_multiple(l):
    if len(l)%4==0:
        return l[::-1]
    else:
        return l
    
print(reverse_multiple('abcd'))