# It is common for images of a country’s previous leaders, or other individuals of historical
# significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in Table 2.1.
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the

s=int(input("Enter a currency in $"))

if s==1:
    print("George Washington")

elif s==2:
    print("Thomson Jefferson")

elif s==5:
    print("Abharam Lincon")

elif s==10:
    print("Alexender Hamilton")

elif s==20:
    print("Andrew Jackson")

elif s==50:
    print("Ulsess S Grant")

elif s==100:
    print("Benjamin Franklin")

else:
    print("Enter Valid Demonitazion")