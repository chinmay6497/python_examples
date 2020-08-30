# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
x=input("Enter a string here:")
y=input("Enter a string here:")

new_x= y[:2]+ x[2:]
new_y= x[:2]+ y[2:]

print(new_x+" "+new_y)