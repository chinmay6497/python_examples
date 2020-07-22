#  This is the program to generate odd number of stars in the pattern. 
number=int(input("Enter the value of rows:"))
k=1

for i in range(1,number+1):   # This is for row
    for j in range(1,k+1):       # this is for column
        print("*",end=" ")
    k=k+2    
    print()
