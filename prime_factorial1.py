def prime_factorial(n):
    if n<=1:
        return

    while n%2==0:
        print(2)
        n=n/2

    while n%3==0:
        print(3)
        n=n/3

    for i in range(5,int(n**0.5),6):
        while n%i==0:
            print(i)
            n=n/i

        while n%(i+2)==0:
            print(i+2)
            n=n/(i+2)

    if n>3:
        print(n)

prime_factorial(12)

# Here time complexity is less than O(n^0.5)