# The following table lists an octave of music notes, beginning with middle C, along
# with their frequencies.
# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed
# previously.
# Once you have your program working correctly for the notes listed previously you
# should add support for all of the notes from C0 to C8. While this could be done by
# adding many additional cases to your if statement, such a solution is cumbersome,
# inelegant and unacceptable for the purposes of this exercise. Instead, you should
# exploit the relationship between notes in adjacent octaves. In particular, the frequency
# of any note in octave n is half the frequency of the corresponding note in octave n+1.
# By using this relationship, you should be able to add support for the additional notes
# without adding additional cases to your if statement.

n=input("Enter a name here:")

n1=n[0]
oct=int(n[1])

if n1=='c':
    freq=261.63

elif n1=='d':
    freq=293.66

elif n1=='e':
    freq=329.63

elif n1=='f':
    freq=349.23

elif n1=='g':
    freq=392

elif n1=='a':
    freq=440

elif n1=='b':
    freq=493.88

freq=freq/2 **(4-oct)

print(f"the frequency is {freq}")