def divisor(n):
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            print(i)
        j=i

    while j!=1:
        if n%j==0:
            print(n//j)
        j-=1

divisor(100)

# A O(sqrt(n)) java program that prints 
# all divisors in sorted order
# import math 

# def printDivisors(n) :
# 	list = [] 
	
# 	# List to store half of the divisors
# 	for i in range(1, int(math.sqrt(n) + 1)) :
		
# 		if (n % i == 0) :
			
# 			# Check if divisors are equal
# 			if (n / i == i) :
# 				print (i, end =" ")
# 			else :
# 				# Otherwise print both
# 				print (i, end =" ")
# 				list.append(int(n / i))
				
# 	# The list will be printed in reverse 
# 	for i in list[::-1] :
# 		print (i, end =" ")
		
# print ("The divisors of 100 are: ")
# printDivisors(100)
