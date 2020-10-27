def lucky(n):
    next_position=n
    if lucky.counter>n:
        return 1
    if n%lucky.counter==0:
        return 0
    
    next_position=next_position-next_position/lucky.counter
    lucky.counter+=1
    return next_position


lucky.counter=2
x=5
if lucky(x):
    print(f'Number {x} is a lucky number')
else:
    print(f'{x} is not a lucky number')
