# Given a number ‘n’, your task is to  generate all n-bit grey code sequences, “a grey code sequence is a sequence such that successive patterns in it differ by one bit”

# Input Description:
# You are given an number ‘n’.

# Output Description:
# Print the grey code sequence

# Sample Input :
# 2
# Sample Output :
# 00 01 11 10

def binary(n): 
    if (n <= 0): 
        return 

    arr =[] 
    arr.append("0") 
    arr.append("1") 
  
    i = 2
    j = 0
    while(True): 
        if i >= 1 << n: 
            break
       
        for j in range(i - 1, -1, -1): 
            arr.append(arr[j]) 
   
        for j in range(i): 
            arr[j] = "0" + arr[j] 
        
        for j in range(i, 2 * i): 
            arr[j] = "1" + arr[j] 
        i = i << 1

   
    for i in range(len(arr)): 
        print(arr[i]) 

binary(3)
