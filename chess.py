# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# a b c d e f g h
# Write a program that reads a position from the user. Use an if statement to determine
# if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking.
# Exercise

s=input("ENter here:")

if s=='a1' or s=='a3' or s=='a5' or s=='s7' or s=='b2' or s=='b4' or s=='b6' or s=='b8' or s=='c1' or s=='c3' or s=='c5' or s=='c7':
    print('Black') 

else:
    print("White")