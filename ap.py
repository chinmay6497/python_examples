# You are provided with a number "N", Find the Nth term of the series: 1, 4, 7, 10 .......

n=int(input("Enter the term which we want to find in the series:"))
a=1
d=3

print(f"The nth term of the series is {a+((n-1)*d)}")
