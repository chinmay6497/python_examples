# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.

v=input("Enter a word here:")
vowel=['a','e','i','o','u']

if v in vowel:
    print("Entered word is vowel")

else:
    print("Entered word is not vowel")