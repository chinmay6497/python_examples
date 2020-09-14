# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3+1+4+1=9.

number=int(input("Enter any natural number" ))
sum=0

while number!=0:
    sum = sum + number%10
    number=number//10

print(sum)

