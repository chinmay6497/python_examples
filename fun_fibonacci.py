#  Fibonacci series in which the preceding term of the series is the addition of the last two terms

num=int(input("Enter a term till which you want series:"))


def fibonacci(num):
    n1=0
    n2=1

    if num==0:
        print(n1)

    elif num==1:
        print(n1,n2)

    else:  
        print(n1,n2, end=" ")  
        for i in range(0,num-2):
            n3=n1+n2
            n1=n2
            n2= n3
            print(n2, end=" ")
           
        
       

fibonacci(num)